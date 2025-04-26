import psycopg2
import csv
import os
import json
from config import load_config

def create_tables_and_procedures():
    """Создаем таблицы и хранимые процедуры"""
    commands = [
        # Удаляем старые таблицы если существуют
        "DROP TABLE IF EXISTS phonebook_new;",
        # Создаем новую таблицу phonebook_new
        """
        CREATE TABLE phonebook_new (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            phone_number VARCHAR(20) NOT NULL UNIQUE
        );
        """,
        # Создаем функцию поиска по шаблону
        """
        CREATE OR REPLACE FUNCTION public.search_by_pattern(pattern TEXT)
        RETURNS SETOF phonebook_new
        LANGUAGE plpgsql
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook_new
            WHERE first_name ILIKE '%' || pattern || '%'
               OR last_name ILIKE '%' || pattern || '%'
               OR phone_number LIKE '%' || pattern || '%';
        END;
        $$;
        """,
        
        # Создаем процедуру для добавления/обновления
        """
        CREATE OR REPLACE PROCEDURE public.insert_update_user(
            f_name VARCHAR, 
            l_name VARCHAR, 
            p_number VARCHAR
        )
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook_new WHERE phone_number = p_number) THEN
                UPDATE phonebook_new 
                SET first_name = f_name, last_name = l_name
                WHERE phone_number = p_number;
            ELSE
                INSERT INTO phonebook_new (first_name, last_name, phone_number)
                VALUES (f_name, l_name, p_number);
            END IF;
        END;
        $$;
        """,
        
        # Создаем функцию для массового добавления
        """
        CREATE OR REPLACE FUNCTION public.insert_many_users(users_data JSONB)
        RETURNS TABLE(incorrect_data JSONB)
        LANGUAGE plpgsql
        AS $$
        DECLARE
            user_record JSONB;
            phone_pattern TEXT := '^[0-9]{10,20}$';
        BEGIN
            FOR user_record IN SELECT * FROM jsonb_array_elements(users_data)
            LOOP
                IF (user_record->>'phone_number') ~ phone_pattern THEN
                    CALL public.insert_update_user(
                        user_record->>'first_name',
                        user_record->>'last_name',
                        user_record->>'phone_number'
                    );
                ELSE
                    incorrect_data := user_record;
                    RETURN NEXT;
                END IF;
            END LOOP;
        END;
        $$;
        """,
        
        # Создаем функцию для пагинации
        """
        CREATE OR REPLACE FUNCTION public.get_paginated_contacts(
            lim INTEGER, 
            offs INTEGER
        )
        RETURNS SETOF phonebook_new
        LANGUAGE plpgsql
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook_new
            ORDER BY last_name, first_name
            LIMIT lim OFFSET offs;
        END;
        $$;
        """,
        
        # Создаем процедуру для удаления
        """
        CREATE OR REPLACE PROCEDURE public.delete_user(
            IN f_name VARCHAR DEFAULT NULL,
            IN l_name VARCHAR DEFAULT NULL,
            IN p_number VARCHAR DEFAULT NULL
        )
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF p_number IS NOT NULL THEN
                DELETE FROM phonebook_new WHERE phone_number = p_number;
            ELSIF f_name IS NOT NULL AND l_name IS NOT NULL THEN
                DELETE FROM phonebook_new 
                WHERE first_name = f_name AND last_name = l_name;
            END IF;
        END;
        $$;
        """
    ]
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    try:
                        cur.execute(command)
                    except Exception as e:
                        print(f"Ошибка при выполнении команды: {e}")
                        conn.rollback()
                        raise
                conn.commit()
                print("Таблицы и хранимые процедуры успешно созданы")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка при создании таблиц: {error}")

def search_by_pattern():
    """Поиск по шаблону"""
    pattern = input("Введите шаблон для поиска: ")
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
                results = cur.fetchall()
                
                if not results:
                    print("Контакты не найдены")
                else:
                    print("\nНайденные контакты:")
                    for contact in results:
                        print(f"ID: {contact[0]}")
                        print(f"Имя: {contact[1]}")
                        print(f"Фамилия: {contact[2]}")
                        print(f"Телефон: {contact[3]}")
                        print("------")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка при поиске: {error}")

def insert_update_user():
    """Добавление/обновление контакта"""
    print("\nДобавление/обновление контакта:")
    first_name = input("Имя: ").strip()
    last_name = input("Фамилия: ").strip()
    phone = input("Номер телефона: ").strip()
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Явно указываем схему public
                cur.execute("CALL public.insert_update_user(%s, %s, %s)", 
                          (first_name, last_name, phone))
                conn.commit()
                print("Операция успешно выполнена")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка: {error}")

def insert_many_users():
    """Добавление нескольких контактов"""
    print("\nВведите данные в формате: Имя,Фамилия,Телефон")
    print("Каждый контакт с новой строки, пустая строка - завершение")
    
    users = []
    while True:
        line = input("> ").strip()
        if not line:
            break
        parts = [part.strip() for part in line.split(',')]
        if len(parts) == 3:
            users.append({
                "first_name": parts[0],
                "last_name": parts[1],
                "phone_number": parts[2]
            })
    
    if not users:
        print("Нет данных для добавления")
        return
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Преобразуем в JSON для передачи в функцию
                users_json = json.dumps(users)
                
                # Вызываем функцию для добавления
                cur.execute("SELECT * FROM public.insert_many_users(%s::jsonb)", (users_json,))
                incorrect = cur.fetchall()
                
                if incorrect:
                    print("\nНекорректные данные (не добавлены):")
                    for item in incorrect:
                        data = json.loads(item[0])
                        print(f"Имя: {data['first_name']}, Фамилия: {data['last_name']}, Телефон: {data['phone_number']}")
                
                conn.commit()
                print(f"\nУспешно обработано: {len(users) - len(incorrect)} из {len(users)}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка: {error}")

def get_paginated_contacts():
    """Просмотр с пагинацией"""
    try:
        limit = int(input("Количество записей на странице: "))
        page = int(input("Номер страницы (начиная с 1): "))
        offset = (page - 1) * limit
    except ValueError:
        print("Некорректный ввод чисел")
        return
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.get_paginated_contacts(%s, %s)", 
                          (limit, offset))
                results = cur.fetchall()
                
                if not results:
                    print("Контакты не найдены")
                else:
                    print(f"\nСтраница {page}:")
                    for contact in results:
                        print(f"{contact[0]}. {contact[1]} {contact[2]} - {contact[3]}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка: {error}")

def delete_user():
    """Удаление контакта"""
    print("\nУдаление контакта:")
    print("1. По номеру телефона")
    print("2. По имени и фамилии")
    choice = input("Выберите вариант (1/2): ")
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    phone = input("Введите номер телефона: ").strip()
                    cur.execute("CALL public.delete_user(NULL, NULL, %s)", (phone,))
                elif choice == '2':
                    first = input("Введите имя: ").strip()
                    last = input("Введите фамилию: ").strip()
                    cur.execute("CALL public.delete_user(%s, %s, NULL)", (first, last))
                else:
                    print("Неверный выбор")
                    return
                
                conn.commit()
                print("Операция удаления выполнена")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка: {error}")

def show_menu():
    """Главное меню"""
    while True:
        print("\nТелефонная книга - Главное меню:")
        print("1. Поиск по шаблону")
        print("2. Добавить/обновить контакт")
        print("3. Добавить несколько контактов")
        print("4. Просмотр с пагинацией")
        print("5. Удалить контакт")
        print("6. Выход")
        
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == '1':
            search_by_pattern()
        elif choice == '2':
            insert_update_user()
        elif choice == '3':
            insert_many_users()
        elif choice == '4':
            get_paginated_contacts()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == '__main__':
    # Сначала создаем все таблицы и процедуры
    create_tables_and_procedures()
    
    # Затем запускаем меню
    show_menu()
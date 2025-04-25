import psycopg2
import csv
import os
from config import load_config

def create_tables():
    """Создаем таблицу phonebook с правильными ограничениями"""
    commands = (
        """
        DROP TABLE IF EXISTS phonebook;
        """,
        """
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL,
            phone VARCHAR(30) NOT NULL UNIQUE
        );
        """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                print("Таблица phonebook успешно создана")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка при создании таблицы: {error}")

def insert_from_csv(filename):
    """Добавляем данные из CSV файла"""
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден!")
        print(f"Текущая папка: {os.getcwd()}")
        print(f"Файлы в папке: {os.listdir()}")
        return
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    header = next(reader)  # Пропускаем заголовок
                    
                    success = 0
                    duplicates = 0
                    errors = 0
                    
                    for row in reader:
                        if len(row) < 2:
                            errors += 1
                            continue
                            
                        full_name, phone = row[0].strip(), row[1].strip()
                        
                        try:
                            cur.execute(
                                """INSERT INTO phonebook (full_name, phone)
                                VALUES (%s, %s)""",
                                (full_name, phone)
                            )
                            success += 1
                        except psycopg2.IntegrityError:
                            duplicates += 1
                            conn.rollback()
                        except Exception as e:
                            errors += 1
                            print(f"Ошибка при добавлении {full_name}: {e}")
                    
                    print("\nИтог импорта:")
                    print(f"Успешно добавлено: {success}")
                    print(f"Пропущено дубликатов: {duplicates}")
                    print(f"Ошибок при добавлении: {errors}")
                    
    except Exception as error:
        print(f"Ошибка при загрузке из CSV: {error}")

def insert_from_console():
    """Добавляем данные через консоль"""
    print("\nДобавление нового контакта:")
    while True:
        full_name = input("Полное имя: ").strip()
        if full_name:
            break
        print("Имя не может быть пустым!")
    
    while True:
        phone = input("Телефон: ").strip()
        if phone:
            break
        print("Телефон не может быть пустым!")
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO phonebook (full_name, phone)
                    VALUES (%s, %s)""",
                    (full_name, phone)
                )
                print("Контакт успешно добавлен")
    except psycopg2.IntegrityError:
        print("Ошибка: такой телефон уже существует")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка при добавлении: {error}")

def update_contact():
    """Обновляем данные контакта"""
    print("\nОбновление контакта")
    phone = input("Введите телефон контакта для изменения: ").strip()
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверяем существование контакта
                cur.execute("SELECT 1 FROM phonebook WHERE phone = %s", (phone,))
                if not cur.fetchone():
                    print("Контакт с таким телефоном не найден")
                    return
                
                print("Что вы хотите изменить?")
                print("1. Полное имя")
                print("2. Телефон")
                choice = input("Выберите вариант (1/2): ")
                
                if choice == '1':
                    new_name = input("Новое имя: ").strip()
                    cur.execute(
                        "UPDATE phonebook SET full_name = %s WHERE phone = %s",
                        (new_name, phone)
                    )
                    print("Имя успешно обновлено")
                elif choice == '2':
                    new_phone = input("Новый телефон: ").strip()
                    cur.execute(
                        "UPDATE phonebook SET phone = %s WHERE phone = %s",
                        (new_phone, phone)
                    )
                    print("Телефон успешно обновлен")
                else:
                    print("Неверный выбор")
    except psycopg2.IntegrityError:
        print("Ошибка: такой телефон уже существует")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка при обновлении: {error}")

def query_contacts():
    """Поиск контактов"""
    print("\nПоиск контактов:")
    print("1. По имени")
    print("2. По телефону")
    print("3. Показать все контакты")
    choice = input("Выберите вариант (1/2/3): ")
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    name = input("Введите имя для поиска: ").strip()
                    cur.execute(
                        "SELECT * FROM phonebook WHERE full_name ILIKE %s",
                        (f'%{name}%',)
                    )
                elif choice == '2':
                    phone = input("Введите телефон для поиска: ").strip()
                    cur.execute(
                        "SELECT * FROM phonebook WHERE phone LIKE %s",
                        (f'%{phone}%',)
                    )
                elif choice == '3':
                    cur.execute("SELECT * FROM phonebook")
                else:
                    print("Неверный выбор")
                    return
                
                contacts = cur.fetchall()
                if not contacts:
                    print("Контакты не найдены")
                else:
                    print("\nНайденные контакты:")
                    for contact in contacts:
                        print(f"ID: {contact[0]}, Имя: {contact[1]}, Телефон: {contact[2]}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка при поиске: {error}")

def delete_contact():
    """Удаление контакта"""
    print("\nУдаление контакта:")
    print("1. По имени")
    print("2. По телефону")
    choice = input("Выберите вариант (1/2): ")
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    name = input("Введите имя для удаления: ").strip()
                    cur.execute(
                        "DELETE FROM phonebook WHERE full_name = %s",
                        (name,)
                    )
                elif choice == '2':
                    phone = input("Введите телефон для удаления: ").strip()
                    cur.execute(
                        "DELETE FROM phonebook WHERE phone = %s",
                        (phone,)
                    )
                else:
                    print("Неверный выбор")
                    return
                
                if cur.rowcount > 0:
                    print(f"Удалено контактов: {cur.rowcount}")
                else:
                    print("Контакты не найдены")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка при удалении: {error}")

def show_menu():
    """Главное меню"""
    while True:
        print("\nТелефонная книга - Главное меню:")
        print("1. Добавить из CSV файла")
        print("2. Добавить вручную")
        print("3. Обновить контакт")
        print("4. Найти контакты")
        print("5. Удалить контакт")
        print("6. Выход")
        
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == '1':
            filename = input("Введите имя CSV файла: ").strip()
            insert_from_csv(filename)
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == '__main__':
    create_tables()
    show_menu()
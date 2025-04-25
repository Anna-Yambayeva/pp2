import psycopg2

conn = psycopg2.connect(
    host     = "localhost",
    database = "phonebook",
    user     = "postgres",
    password = "Fyyf1012"       
)

# SQL‑код создания объектов
create_f_find = """
CREATE OR REPLACE FUNCTION f_phonebook_find(pattern text)
RETURNS TABLE(id int, full_name text, phone text)
LANGUAGE sql
AS $$
    SELECT id, full_name, phone
    FROM   phonebook
    WHERE  full_name ILIKE '%'||pattern||'%'
       OR  phone     ILIKE '%'||pattern||'%'
    ORDER  BY full_name;
$$;
"""

create_p_upsert = """
CREATE OR REPLACE PROCEDURE p_phonebook_upsert(
    p_name  text,
    p_phone text
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook(full_name, phone)
    VALUES (p_name, p_phone)

    -- ключ теперь имя!
    ON CONFLICT (full_name)
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$;

"""

create_f_page = """
CREATE OR REPLACE FUNCTION f_phonebook_page(p_limit int, p_offset int)
RETURNS TABLE(id int, full_name text, phone text)
LANGUAGE sql
AS $$
    SELECT id, full_name, phone
    FROM   phonebook
    ORDER  BY id
    LIMIT  p_limit
    OFFSET p_offset;
$$;
"""

def execute_query(sql: str):
    try:
        with conn, conn.cursor() as cur:
            cur.execute(sql)
    except (psycopg2.DatabaseError, Exception) as err:
        print("ERROR:", err)

def upsert_contact(name: str, phone: str):
    """Вставить / обновить запись (процедура)"""
    with conn, conn.cursor() as cur:
        cur.execute("CALL p_phonebook_upsert(%s, %s);", (name, phone))

def find_contacts(pattern: str):
    """Вернёт список, совпадающих с шаблоном"""
    with conn, conn.cursor() as cur:
        cur.callproc("f_phonebook_find", (pattern,))
        return cur.fetchall()

def get_page(limit: int, offset: int):
    """Вернёт LIMIT/OFFSET страницу"""
    with conn, conn.cursor() as cur:
        cur.callproc("f_phonebook_page", (limit, offset))
        return cur.fetchall()

if __name__ == "__main__":
    # ─ один раз раскомментировать для создания объектов
    # execute_query(create_f_find)
    # execute_query(create_p_upsert)
    # execute_query(create_f_page)

    # ─ upsert
    upsert_contact("Ima Phamilia", "+70010020304")      
    upsert_contact("Alice Cooper", "+73167897496")             

    # ─ поиск
    print("=== find '777' ===")
    for row in find_contacts("777"):
        print(row)

    # ─ пагинация
    print("=== first 5 ===")
    for row in get_page(5, 0):
        print(row)

    conn.close()
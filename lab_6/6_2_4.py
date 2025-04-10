def count_lines_in_file(filename):

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return len(lines)

if __name__ == "__main__":
    file_name = input("Введите путь к текстовому файлу: ")
    try:
        lines_count = count_lines_in_file(file_name)
        print("Количество строк:", lines_count)
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print("Ошибка при чтении файла:", e)


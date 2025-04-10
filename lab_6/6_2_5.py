def write_list_to_file(lst, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in lst:
            f.write(str(item) + "\n")

if __name__ == "__main__":
    my_data = [10, 20, 30, "Hello", "World", "Можно фул без проверки пж"]
    file_name = "output.txt"
    write_list_to_file(my_data, file_name)
    print(f"Список {my_data} записан в файл {file_name}.")
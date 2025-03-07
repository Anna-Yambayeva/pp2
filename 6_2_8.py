import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"Файл '{path}' удалён.")
        else:
            print("Нет прав на удаление (нет записи).")
    else:
        print("Файл не существует.")

if __name__ == "__main__":
    file_path = input("Укажите путь к файлу для удаления: ")
    delete_file(file_path)
import os

def analyze_path(path):
    if os.path.exists(path):
        file_name = os.path.basename(path)
        dir_name = os.path.dirname(path)
        return file_name, dir_name
    else:
        return None, None

if __name__ == "__main__":
    user_path = input("Введите путь: ")
    fname, dname = analyze_path(user_path)
    if fname is not None:
        print("Путь существует.")
        print("Имя файла/последнего каталога:", fname)
        print("Директория:", dname)
    else:
        print("Путь не существует.")
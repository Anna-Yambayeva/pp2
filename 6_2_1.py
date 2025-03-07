import os

def list_dirs_files(path):
    dirs = []
    files = []
    all_items = os.listdir(path)
    for item in all_items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            dirs.append(item)
        elif os.path.isfile(full_path):
            files.append(item)
    
    return dirs, files, all_items

if __name__ == "__main__":
    user_path = input("Введите путь: ")
    if os.path.exists(user_path):
        dirs_list, files_list, all_list = list_dirs_files(user_path)
        print("Directories:", dirs_list)
        print("Files:", files_list)
        print("All items:", all_list)
    else:
        print("Указанный путь не существует.")
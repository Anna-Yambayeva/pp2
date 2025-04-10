import os

def check_access(path):
    result = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
    return result

if __name__ == "__main__":
    user_path = input("Введите путь: ")
    access_info = check_access(user_path)
    print("Path exists:", access_info["exists"])
    print("Readable:", access_info["readable"])
    print("Writable:", access_info["writable"])
    print("Executable:", access_info["executable"])
import string
import os

def generate_alphabet_files(path):
    if not os.path.exists(path):
        os.makedirs(path)

    for letter in string.ascii_uppercase: 
        filename = os.path.join(path, f"{letter}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"This is file {letter}.txt\n")

if __name__ == "__main__":
    target_path = r"C:\Users\User\OneDrive\Рабочий стол\pp22025\lab6\for-dir-6py"
    generate_alphabet_files(target_path)
    print(f"Файлы A.txt ... Z.txt созданы в каталоге: {target_path}")
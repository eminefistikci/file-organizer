#main.py
from pathlib import Path
import shutil

print("====================")
print("FILE ORGANIZER")
print("====================")

def get_directory():
    while True:
        path = Path(input("\nEnter a directory path: "))
        if path.is_dir():
            print("This path exists.")
            print("This is a directory.")
            return path
        else:
            if path.is_file():
                print("This is a file, not a directory.")
            else:
                print("This path does not exist.")


categories = {"Images":[".jpg", ".jpeg", ".png", ".bmp"],
              "Documents":[".pdf", ".doc", ".docx",".txt"],
              "Audio": [".mp3",".wav"],
              "Videos":[".mp4",".mov"],
              "Programming Languages":[".py",".js",".java",".cs",".cpp",".html",".css"]
              }


def get_category(extension):
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    return "Others"


def categorize_files(path):
    files_by_category = {}

    for file in path.iterdir():
        if file.is_file():
            file_name = file.name
            file_category = get_category(file.suffix)
            if file_category in files_by_category:
                files_by_category[file_category].append(file_name)
            else:
                files_by_category[file_category] = [file_name]

    return files_by_category


def create_category_folders(path, files_by_category):
    for category in files_by_category:
        category_path = path / category
        category_path.mkdir(exist_ok=True)


def move_files(path, files_by_category):
    for category, files in files_by_category.items():
        category_path = path / category
        for file in files:
            source_path = path / file
            destination_path = category_path / file
            try:
                shutil.move(source_path, destination_path)
            except (FileNotFoundError, PermissionError) as e:
                print("Could not move:", source_path)
                print("Reason:", e)
                continue


def print_summary(files_by_category):
    print("====================")
    print("ORGANIZATION COMPLETE")
    print("====================")

    for category,files in files_by_category.items():
        if len(files) > 1:
            print(f"{category}: {len(files)} files")
        else:
            print(f"{category}: {len(files)} file")


path = get_directory()
files_by_category = categorize_files(path)
create_category_folders(path, files_by_category)
move_files(path, files_by_category)
print_summary(files_by_category)

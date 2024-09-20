import os
import shutil
from file_types import file_types

folder_to_organize = r'D:\Internships\CodeAlpha(1 Month)\Task_Automation_project\Target_folder'

def create_directories():
    for category in file_types.keys():
        dir_path = os.path.join(folder_to_organize, category)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f'Created directory: {category}')

def organize_files():
    for file in os.listdir(folder_to_organize):
        file_path = os.path.join(folder_to_organize, file)
        if os.path.isfile(file_path):
            move_file(file_path, file)

def move_file(file_path, file):
    file_extension = os.path.splitext(file)[1].lower()
    moved = False
    for category, extensions in file_types.items():
        if file_extension in extensions:
            dest_dir = os.path.join(folder_to_organize, category)
            shutil.move(file_path, dest_dir)
            print(f'Moved {file} to {category}')
            moved = True
            break
    if not moved:
        others_dir = os.path.join(folder_to_organize, 'Others')
        if not os.path.exists(others_dir):
            os.makedirs(others_dir)
        shutil.move(file_path, others_dir)
        print(f'Moved {file} to Others')


create_directories()
organize_files()

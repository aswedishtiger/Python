import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(directory, ext.upper())
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(ext_folder, filename))

directory_path = "/path/to/your/directory"
organize_files(directory_path)
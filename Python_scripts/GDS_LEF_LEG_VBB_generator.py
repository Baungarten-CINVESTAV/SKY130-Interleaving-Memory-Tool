import shutil
import os

def Copy_macro_files(Folder_name):
    current_directory = os.getcwd()
   # print(current_directory)

    source_path = f'{current_directory}/Python_scripts/macro_files'
    destination_path = f'{current_directory}/designs/{Folder_name}'
    
    folders = [folder for folder in os.listdir(source_path) if os.path.isdir(os.path.join(source_path, folder))]

    # Copy each folder to the destination path
    for folder in folders:
        source_folder = os.path.join(source_path, folder)
        destination_folder = os.path.join(destination_path, folder)
        shutil.copytree(source_folder, destination_folder)

    return

import webbrowser
import os
import shutil
from keyboard import send
from AppOpener import open as open_app
from pathlib import Path
from lexicon.lexicon import APPS, SITES, COMMANDS_CLEAN_FOLDER, COMMANDS_SYS_FOLDERS, COMMANDS_APPS, COMMANDS_SCREENSHOT, COMMANDS_CLEAN_FILE
from services.services import cleaning_file_name, cleaning_folder_name, cleaning_name_c
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from services.services import cleaning_set_volume

def handles_apps(user_input):
    user_input.lower()
    for text in COMMANDS_APPS:
        if text in user_input:
            user_input = user_input.replace(text, "").strip()
    for key, value in APPS.items():
        for text in value:
            if text in user_input:
                open_app(key, throw_error=True)
                break
    
def handles_websites(user_input):
    webbrowser.register('Firefox', None, webbrowser.BackgroundBrowser('C:/Program Files/Mozilla Firefox/firefox.exe'))
    for text in COMMANDS_APPS:
        if text in user_input:
            user_input = user_input.replace(text, "").strip()

    for key, value in SITES.items():
        if user_input in value:
            webbrowser.get('Firefox').open_new_tab(f'https://www.{key}.com/')
            print("Successfully opened. Enjoy!")

    for value in SITES.values():
        if value not in SITES.values():
            webbrowser.get('Firefox').open_new_tab('https://www.google.com/search?q={}'.format(user_input))
            print("Couldn't understand of what you're saying, maybe Google can help you.")

def handles_sorting_files():
    categories_dict = {
        "Documents": [".docx", ".pdf", ".txt", ".doc", ".xlsx", ".pptx"],
        "Images": [".png", ".jpg", ".jpeg", ".gif", ".heif"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Video": [".mp4", ".mpeg", ".avi"],
        "Archives": [".zip", ".rar", ".7z"],
        "Web Page": [".html"],
    }
    
    other_categ = "Other"
    input_path = input("Write your directory (e.g. /Users/Admin/Desktop/Folder): ")
    os.chdir(input_path)

    print("Moving your files...")

    for file in Path().iterdir():
        if file.is_file() == True:
            for category, extensions in categories_dict.items():
                if file.suffix in extensions:
                    dir_path = Path(category)
                    dir_path.mkdir(exist_ok=True)
                    shutil.move(file, dir_path)
                    
    for file in Path().iterdir():
        if file.is_file() == True:
            if not file.suffix in categories_dict.values():
                other_path = Path(other_categ)
                other_path.mkdir(exist_ok=True)
                shutil.move(file, other_path)
    print("Successfully moved.")

def handles_create_folder(user_input):
    text = cleaning_folder_name(user_input)
    input_path = "/Users/Friday/" + text[0]
    os.chdir(input_path)

    name_folder = Path(text[1])
    name_folder.mkdir(exist_ok=True)
    print(f"{name_folder} successfully created in {input_path}.")

def handles_find_folder(user_input):
    found_folders = []
    command_text = user_input
    folder_text = cleaning_folder_name(command_text)
    for root, dirs, _ in os.walk('C:/Users/Friday/{}'.format(folder_text[0])):
        for dir in dirs:
            if folder_text[1] in dir:
                found_folders.append(dir)
                print(f"Название папки: {dir}")
                print(f"Путь: {os.path.join(root, dir)}")                           
    print(f"Найдено папок: {len(found_folders)}")

def handles_find_file(user_input):
    found_files = []
    file_text = cleaning_file_name(user_input)
    for root, _, files in os.walk('C:/Users/Friday/{}'.format(file_text[0])):
        for file in files:
            if file_text[1] in file:
                found_files.append(file)
                print(f"Название файла: {file}")
                print(f"Путь: {os.path.join(root, file)}")
    print(f"Найдено файлов: {len(found_files)}")

def handles_find_disk(user_input):
    found_files = []
    found_folders = []
    command_text = user_input
    text = cleaning_name_c(command_text)
    for root, dirs, files in os.walk("C:/"):
        for dir in dirs:
            if text[1].lower() in dir.lower():
                found_folders.append(dir)
                print(f"Название папки: {dir}")
                print(f"Путь: {os.path.join(root, dir)}")                           
        
        for file in files:
            if text[1].lower() in file.lower():
                found_files.append(file)
                print(f"Название файла: {file}")
                print(f"Путь: {os.path.join(root, file)}")
    print(f"Найдено папок: {len(found_folders)}")
    print(f"Найдено файлов: {len(found_files)}")

def handles_set_volume(user_input):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(cleaning_set_volume(user_input), None)
    current_volume = float(volume.GetMasterVolumeLevelScalar())
    print(f"Громкость поставлен на: {current_volume:.2f}")

def handles_increase_volume(user_input):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume.GetMasterVolumeLevelScalar() + 0.03, None)
    current_volume = float(volume.GetMasterVolumeLevelScalar())
    print("Громкость прибавлена")
    print(f"Громкость поставлен на: {current_volume:.2f}")

def handles_decrease_volume(user_input):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume.GetMasterVolumeLevelScalar() - 0.03, None)
    current_volume = float(volume.GetMasterVolumeLevelScalar())
    print("Громкость снижена")
    print(f"Громкость поставлена на: {current_volume:.2f}")

def handles_mute_volume(user_input):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(0, None)
    current_volume = float(volume.GetMasterVolumeLevelScalar())
    print("Без звука")
from lexicon.lexicon import LEXICON, COMMANDS_SYS_FOLDERS

def cleaning_folder_create_name(text_input):
    clean_folder_name_destination = []
    command_text = text_input
    for text in LEXICON["folders_create"]["keywords"]:
        if text in command_text:
            command_text = command_text.replace(text, "")
            for key, value in COMMANDS_SYS_FOLDERS.items():
                for ph in value:
                    if ph in command_text:
                        clean_folder_name_destination.append(key)
                for phrase in value:
                    if phrase in command_text:
                        command_text = command_text.replace(phrase, "").strip()
                        clean_folder_name_destination.append(command_text)
    return clean_folder_name_destination

def cleaning_folder_find_name(text_input):
    clean_folder_name_destination = []
    command_text = text_input
    for text in LEXICON["folders_find"]["keywords"]:
        if text in command_text:
            command_text = command_text.replace(text, "")
            for key, value in COMMANDS_SYS_FOLDERS.items():
                for ph in value:
                    if ph in command_text:
                        clean_folder_name_destination.append(key)
                for phrase in value:
                    if phrase in command_text:
                        command_text = command_text.replace(phrase, "").strip()
                        clean_folder_name_destination.append(command_text)
    return clean_folder_name_destination

def cleaning_file_name(text_input):
    clean_file_name_destination = []
    command_text = text_input
    for text in LEXICON["files"]["keywords"]:
        if text in command_text:
            command_text = command_text.replace(text, "")
            for key, value in COMMANDS_SYS_FOLDERS.items():
                for ph in value:
                    if ph in command_text:
                        clean_file_name_destination.append(key)
                for phrase in value:
                    if phrase in command_text:
                        command_text = command_text.replace(phrase, "").strip()
                        clean_file_name_destination.append(command_text)
    return clean_file_name_destination

def cleaning_name_c(text_input):
    clean_disk_name_destination = []
    command_text = text_input
    for text in LEXICON["disks"]["keywords"]:
        if text in command_text:
            command_text = command_text.replace(text, "").strip()
            for key, value in COMMANDS_SYS_FOLDERS.items():
                for ph in value:
                    if ph in command_text:
                        clean_disk_name_destination.append(key)
                for phrase in value:
                    if phrase in command_text:
                        command_text = command_text.replace(phrase, "").strip()
                        clean_disk_name_destination.append(command_text)
    return clean_disk_name_destination

def cleaning_set_volume(text_input):
    volume_number: int
    command_text = text_input
    for text in LEXICON["volume_set"]["keywords"]:
        if text in command_text:
            command_text = command_text.replace(text, "").strip()
            volume_number = float(command_text)
            volume_number /= 100
    return volume_number

def cleaning_set_brightness(text_input):
    command_text = text_input
    for text in LEXICON["brightness_set"]["keywords"]:
        if text in command_text:
            command_text = command_text.replace(text, "").strip()
            brightness_number = int(command_text)
    return brightness_number

from lexicon.lexicon import COMMANDS_CLEAN_FILE, COMMANDS_CLEAN_FOLDER, COMMANDS_SYS_FOLDERS, COMMANDS_CLEAN_DISK, COMMANDS_SET_VOLUME

def cleaning_folder_name(text_input):
    clean_folder_name_destination = []
    command_text = text_input
    for text in COMMANDS_CLEAN_FOLDER:
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
    for text in COMMANDS_CLEAN_FILE:
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
    for text in COMMANDS_CLEAN_DISK:
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
    for text in COMMANDS_SET_VOLUME:
        if text in command_text:
            command_text = command_text.replace(text, "").strip()
            volume_number = float(command_text)
            volume_number /= 100
    return volume_number
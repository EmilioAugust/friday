from commands.speech_recog import recognize_text
from commands.commands import (handles_apps, handles_websites, handles_sorting_files,
                               handles_create_folder, handles_find_folder, handles_find_file,
                               handles_find_disk, handles_set_volume, handles_increase_volume, handles_decrease_volume, handles_mute_volume)
from lexicon.lexicon import (COMMANDS_APPS, COMMANDS_SORT_FILES, COMMANDS_CREATE_FOLDER,
                             COMMAND_WEBSITES, COMMANDS_CLEAN_DISK, COMMANDS_CLEAN_FILE,
                             COMMANDS_CLEAN_FOLDER, COMMANDS_SET_VOLUME, COMMANDS_VOLUME_UP, COMMANDS_VOLUME_DOWN, COMMANDS_VOLUME_MUTE)

def main():
    while True:
        user_input = recognize_text()
        if any(text in user_input for text in COMMANDS_APPS):
                handles_apps(user_input)

        if any(text in user_input for text in COMMAND_WEBSITES):         
            handles_websites(user_input)

        if user_input.startswith(COMMANDS_SORT_FILES): 
            handles_sorting_files()

        if any(text in user_input for text in COMMANDS_CREATE_FOLDER):
                handles_create_folder(user_input)

        if any(text in user_input for text in COMMANDS_CLEAN_FOLDER):
                handles_find_folder(user_input)

        if any(text in user_input for text in COMMANDS_CLEAN_FILE):
                handles_find_file(user_input)

        if any(text in user_input for text in COMMANDS_CLEAN_DISK):
                handles_find_disk(user_input)

        if any(text in user_input for text in COMMANDS_SET_VOLUME):
                handles_set_volume(user_input)

        if any(text in user_input for text in COMMANDS_VOLUME_UP):
                handles_increase_volume(user_input)

        if any(text in user_input for text in COMMANDS_VOLUME_DOWN):
                handles_decrease_volume(user_input)

        if any(text in user_input for text in COMMANDS_VOLUME_MUTE):
                handles_mute_volume(user_input)

if __name__ == "__main__":
    main()
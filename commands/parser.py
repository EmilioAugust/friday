from lexicon.lexicon import LEXICON
from commands.commands import (handles_apps, handles_websites, handles_sorting_files,
                               handles_create_folder, handles_decrease_volume, handles_find_disk,
                               handles_find_file, handles_find_folder, handles_increase_volume,
                               handles_mute_volume, handles_set_volume, handles_brightness)

HANDLERS = {
    "handles_brightness": handles_brightness,
    "handles_decrease_volume": handles_decrease_volume,
    "handles_increase_volume": handles_increase_volume,
    "handles_mute_volume": handles_mute_volume,
    "handles_set_volume": handles_set_volume,
    "handles_find_file": handles_find_file,
    "handles_find_folder": handles_find_folder,
    "handles_find_disk": handles_find_disk,
    "handles_create_folder": handles_create_folder,
    "handles_sorting_files": handles_sorting_files,
    "handles_apps": handles_apps,
    "handles_websites": handles_websites,
}

def parse_command(user_input):
    candidates = []
    for value in LEXICON.values():
        for keyword in value["keywords"]:
            if keyword in user_input:
                candidates.append((keyword, HANDLERS[value["handler"]]))
    if not candidates:
        return None
    candidates.sort(key=lambda x: len(x[0]), reverse=True)
    return candidates[0][1]

def dispatch(handler, user_input):
    handler(user_input)

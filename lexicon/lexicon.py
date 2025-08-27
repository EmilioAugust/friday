FRIDAY_RESPONSES = {"synonyms": ("пятница", "ассистент", "бот")} # можете поменять на что-то своё

LEXICON = {
    "apps": {
        "keywords": ("запусти", "включи", "сделай"),
        "handler": "handles_apps"
    },
    "websites": {
        "keywords": ("открой", "найди"),
        "handler": "handles_websites"
    },
    "sort_files": {
        "keywords": ("рассортировать", "рассортируй", "организовать файлы", "организуй файлы",
                     "приберись", "навести порядок", "отсортируй", "сортируй"),
        "handler": "handles_sorting_files"
    },
    "folders_create": {
        "keywords": ("создай папку", "создать папку"),
        "handler": "handles_create_folder"
    },
    "folders_find": {
        "keywords": ("найди папку", "найти папку"),
        "handler": "handles_find_folder"
    },
    "files": {
        "keywords": ("найди файл", "найти файл"),
        "handler": "handles_find_file"
    },
    "disks": {
        "keywords": ("найди", "поищи"),
        "handler": "handles_find_disk"
    },
    "volume_set": {
        "keywords": ("поставь громкость на", "установи громкость", "громкость на", "звук на"),
        "handler": "handles_set_volume"
    },
    "volume_up": {
        "keywords": ("громче", "увеличь громкость", "повысь звук", "сделай громче",
                     "подними громкость", "прибавь звук"),
        "handler": "handles_increase_volume"
    },
    "volume_down": {
        "keywords": ("тише", "уменьши громкость", "понижай звук", "сделай тише",
                     "убавь громкость", "сбавь звук"),
        "handler": "handles_decrease_volume"
    },
    "volume_mute": {
        "keywords": ("выключи звук", "отключи звук", "сделай без звука", "заглуши"),
        "handler": "handles_mute_volume"
    },
    "brightness_set": {
        "keywords": ("поставь яркость на", "сделай яркость на"),
        "handler": "handles_brightness"
    },
}

FUNCTION_RESPONSES = {
    "general": [
        "Sure, I'm on it.",
        "Consider it done.",
        "Executing your command now.",
        "Done. Anything else?",
        "I've got it covered.",
        "Your wish is my command.",
        "All set, moving forward.",
        "Command received, taking action.",
        "Processing now."
    ],
    "search": [
        "Searching for that now.",
        "Looking it up.",
        "Let me find that for you.",
        "Finding it as we speak.",
        "I'll locate it right away."
    ],
    "open_app": [
        "Opening it now.",
        "Starting the application.",
        "Launching it for you.",
        "App is on, ready to go."
    ],
    "file_operations": [
        "Handling your files now.",
        "Sorting it out.",
        "Working on that file.",
        "File operation completed."
    ],
    "settings_change": [
        "Adjusting that setting.",
        "Setting it as requested.",
        "Done, settings updated.",
        "Configuration changed."
    ]
}

COMMANDS_SYS_FOLDERS = {
     "Desktop": ["на рабочем столе", "в десктопе"],
     "Downloads": ["в загрузках", "в папке загрузки"],
     "Documents": ["в документах", "в папке документы"],
     "Music": ["в музыке", "в папке музыка"],
     "Pictures": ["в изображениях", "в фотографиях", "в папке фотографии", "в папке изображения"],
     "C:/": ["на компьютере", "везде", "на диске", "в системе", "по диску"]
 }

APPS = {
    "adobe after effects": ["after effects", "адоб афтер эффектс", "афтер эффектс", "afterfx"],
    "adobe photoshop": ["photoshop", "фотошоп", "адоб фотошоп"],
    "amd software adrenalin edition": ["amd", "amd control panel", "amd драйвер", "amd adrenalin", "adrenalin edition"],
    "calculator": ["калькулятор", "счётчик", "calculator"],
    "camera": ["камера", "фото камера", "вебкамера", "camera"],
    "canon print": ["canon", "печать", "canon print", "принтер"],
    "capcut": ["capcut", "капкат", "видеоредактор"],
    "clock": ["часы", "таймер", "будильник", "clock"],
    "cpu-z": ["cpuz", "cpu-z", "cpu z", "система", "характеристики"],
    "cursor": ["cursor", "курсор", "курсор.ai", "дизайн курсор"],
    "database compare": ["сравнение баз", "database compare", "базы данных"],
    "edifier gaming center": ["edifier", "звуковая панель", "edifier gaming"],
    "excel": ["excel", "эксель", "таблицы", "microsoft excel"],
    "figma": ["figma", "дизайн", "фигма", "макеты"],
    "firefox": ["firefox", "файрфокс", "mozilla", "браузер firefox"],
    "github desktop": ["github desktop", "гитхаб десктоп", "репозиторий"],
    "google chrome": ["chrome", "гугл хром", "google chrome", "браузер"],
    "lenovo vantage": ["lenovo", "lenovo vantage", "вантедж", "леново настройки"],
    "lightshot": ["скриншот", "lightshot", "лайтшот", "сделать снимок"],
    "microsoft edge": ["edge", "microsoft edge", "эдж", "браузер edge"],
    "microsoft store": ["магазин", "store", "microsoft store", "приложения"],
    "msi afterburner": ["msi", "afterburner", "разгон", "msi afterburner"],
    "notepad": ["блокнот", "notepad", "записка", "текстовик"],
    "nvidia app": ["nvidia", "nvidia app", "драйвер nvidia", "панель nvidia"],
    "nvidia broadcast": ["nvidia broadcast", "вещание nvidia", "nvidia стрим"],
    "nvidia control panel": ["nvidia control", "nvidia control panel", "панель управления nvidia"],
    "nvidia physx properties": ["physx", "nvidia physx", "физикс", "nvidia physx properties"],
    "photos": ["фото", "photos", "галерея", "просмотр фото"],
    "quicklook": ["quicklook", "быстрый просмотр", "preview"],
    "revo uninstaller": ["revo", "удаление программ", "revo uninstaller", "деинсталлятор"],
    "rivatuner statistics server": ["rivatuner", "статистика", "fps монитор", "rivatuner statistics"],
    "rockstar games launcher": ["rockstar", "рокстар", "gta лаунчер", "rockstar launcher", "гта"],
    "steam": ["steam", "стим", "игры", "лаунчер стим"],
    "ubisoft connect": ["ubisoft", "юби", "ubisoft connect", "юби лаунчер"],
    "unigram": ["unigram", "telegram", "телеграм", "мессенджер", "юниграм", "тг"],
    "visual studio code": ["vscode", "visual studio code", "вс код", "код", "редактор кода"],
    "vivaldi": ["vivaldi", "браузер вивальди", "вивальди"],
    "vlc media player": ["vlc", "влц", "видеоплеер", "vlc media player"],
    "wintoys": ["wintoys", "тюнинг windows", "винтойс", "настройки windows"],
    "word": ["word", "ворд", "документ", "microsoft word", "текстовый редактор"],
    "zoom workplace": ["zoom", "зум", "видеозвонок", "zoom workplace"],
    "opera": ["opera", "опера", "браузер опера"]
}

SITES = {
    "youtube": ["youtube", "ютуб"],
    "google": ["гугл", "google", "интернет"],
    "gmail": ["почта", "gmail", "гугл почта"],
    "chatgpt": ["чатгпт", "chatgpt", "гпт", "чат гпт", "ии"],
    "github": ["github", "гитхаб", "мой github", "репозиторий"],
}
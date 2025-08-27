import asyncio
from commands.speech_recog import recognize_text
from commands.parser import parse_command, dispatch
from commands.communicate import voice_start, handles_friday

def main():
    asyncio.run(voice_start())
    while True:
        user_input = recognize_text()
        command_text = handles_friday(user_input)
        handler = parse_command(command_text)
        if handler:
            dispatch(handler, command_text)
        else:
            print("Команда не найдена!")

if __name__ == "__main__":
     main()
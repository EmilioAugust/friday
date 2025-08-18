import speech_recognition
print("Talk...")
def recognize_text():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio, language="ru-RU")
        text = text.lower()

        return text

    
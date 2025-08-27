import speech_recognition

def recognize_text():
    print("Talk...")
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=1)
        audio = recognizer.listen(mic, timeout=None, phrase_time_limit=None)
        text = recognizer.recognize_google(audio, language="ru-RU")
        text = text.lower()
        return text

    
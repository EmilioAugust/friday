import asyncio
import edge_tts
import io
import sounddevice as sd
import soundfile as sf
import random
from lexicon.lexicon import FRIDAY_RESPONSES, FUNCTION_RESPONSES, LEXICON


async def voice_start():
    volume = "-90%"
    communicate = edge_tts.Communicate("Hi there, it's Friday", "en-US-JennyNeural", volume=volume)
    audio_bytes = b""
    
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_bytes += chunk["data"]

    with io.BytesIO(audio_bytes) as f:
        data, samplerate = sf.read(f, dtype="float32")
        sd.play(data, samplerate)
        sd.wait()

async def say_text(text_input):
    volume = "-90%"
    text = text_input
    communicate = edge_tts.Communicate(text, "en-US-JennyNeural", volume=volume)
    audio_bytes = b""
    
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_bytes += chunk["data"]

    with io.BytesIO(audio_bytes) as f:
        data, samplerate = sf.read(f, dtype="float32")
        sd.play(data, samplerate)
        sd.wait()

def handles_friday(user_input):
    command_text = user_input
    for keyword in FRIDAY_RESPONSES["synonyms"]:
        if keyword.lower() in user_input.lower():
            command_text = command_text.replace(keyword, "").strip()
            random_word = random.choice(FUNCTION_RESPONSES["general"])
            asyncio.run(say_text(random_word))
            return command_text
    return None
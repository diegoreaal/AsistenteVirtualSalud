import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()
    engine.setProperty(
        "voice",
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0"
    )
    engine.say(texto)
    engine.runAndWait()

import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    for voice in voices:
        if "spanish" in voice.name.lower() or "es" in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.say(texto)
    engine.runAndWait()

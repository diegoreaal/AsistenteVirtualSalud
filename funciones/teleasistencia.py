# pasa de texto a voz
import speech_recognition as sr
# integración IA
from funciones.hablar import hablar
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("No se encontró API_KEY en el archivo .env")

# configurar Gemini con la API KEY
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def transformar_audio_texto():
    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzo la grabacion
        print("Ya puedes hablar")

        # Guardar el audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language="es-ES")

            # Imprimir prueba de ingreso
            print(f"Dijiste: {pedido}")

            # Devolver pedido
            return pedido
        except sr.UnknownValueError:
            # Prueba de que no comprendió audio
            print("Ups, no entendí")
            return "Sigo esperando"
        except sr.RequestError:
            # Prueba de que no comprendió audio
            print("Ups, no hay servicio")
            return "Sigo esperando"
        except:
            # Prueba de que no comprendió audio
            print("Ups, algo ha salido mal")
            return "Sigo esperando"

def consulta():
    sintomas = transformar_audio_texto()

    if not sintomas:  # fallback a teclado
        sintomas = input("No entendí tu voz. Por favor, escribe tus síntomas: ")

    if sintomas.strip():
        prompt = f"(en formato simple) Según estos síntomas: {sintomas}, ¿qué podría estar pasando?"
        response = model.generate_content(prompt)

        print("Asistente:", response.text)
        hablar(response.text)
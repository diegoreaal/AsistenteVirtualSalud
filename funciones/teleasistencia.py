# pasa de texto a voz
from funciones.microfono import transformar_audio_texto
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

def consulta():
    sintomas = transformar_audio_texto()

    if not sintomas:  # fallback a teclado
        sintomas = input("No entendí tu voz. Por favor, escribe tus síntomas: ")

    if sintomas.strip():
        prompt = f"(en formato simple) Según estos síntomas: {sintomas}, ¿qué podría estar pasando?"
        response = model.generate_content(prompt)

        print("Asistente:", response.text)
        hablar(response.text)
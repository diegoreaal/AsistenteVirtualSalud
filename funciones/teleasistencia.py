# pasa de texto a voz
import pyttsx3
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

# crear modelo
model = genai.GenerativeModel('gemini-1.5-flash')

def consulta():
    # pedir los síntomas al usuario
    sintomas = input("Por favor, escribe tus síntomas: ")

    if sintomas.strip():
        prompt = "(en formato sin negrita ni items) puedes sugerirme de forma breve y simple qué me está pasando en base a los siguientes síntomas: " + sintomas
        response = model.generate_content(prompt)

        print("\nAsistente:", response.text)
        hablar(response.text)
        return response
    else:
        hablar("No se recibieron síntomas. Intenta de nuevo.")
        return None
import os
from datetime import timedelta
import dateparser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from funciones.hablar import hablar
from funciones.microfono import transformar_audio_texto

# Scopes: lectura + escritura de eventos
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

# Ajusta tu zona horaria
TZ = "America/Argentina/Buenos_Aires"


def get_calendar_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("calendar", "v3", credentials=creds)


def agendar_turno(duracion_min=30,
                  titulo="Turno médico",
                  descripcion="Agendado desde el asistente"):
    # Pedir fecha y hora en una sola frase
    hablar("Dime la fecha y la hora del turno. Por ejemplo: veinticinco de octubre a las tres y cuarto de la tarde.")
    texto = transformar_audio_texto()
    if not texto:
        hablar("No entendí nada. Intenta de nuevo.")
        return None

    # Interpretar fecha y hora en español
    start = dateparser.parse(
        texto,
        languages=["es"],
        settings={"TIMEZONE": TZ, "RETURN_AS_TIMEZONE_AWARE": True}
    )

    if not start:
        hablar("No pude interpretar la fecha y hora. Repítelo, por favor.")
        return None

    # Confirmar lo que entendió
    fecha_hora_str = start.strftime("%d de %B de %Y a las %H:%M")
    hablar(f"He entendido {fecha_hora_str}. ¿Es correcto? Responde sí o no.")
    confirmacion = transformar_audio_texto()

    if confirmacion and "sí" not in confirmacion.lower():
        hablar("De acuerdo, no guardaré el turno.")
        return None

    end = start + timedelta(minutes=duracion_min)

    try:
        event = {
            "summary": titulo,
            "description": descripcion,
            "start": {"dateTime": start.isoformat(), "timeZone": TZ},
            "end": {"dateTime": end.isoformat(), "timeZone": TZ},
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "popup", "minutes": 30},
                    {"method": "popup", "minutes": 10},
                ],
            },
        }

        service = get_calendar_service()
        created = service.events().insert(calendarId="primary", body=event).execute()

        hablar("Turno agendado correctamente en Google Calendar.")
        print("✅ Evento creado:", created.get("htmlLink"))
        return created.get("htmlLink")

    except Exception as e:
        hablar("No se pudo agendar el turno")
        print("Error:", e)
        return None

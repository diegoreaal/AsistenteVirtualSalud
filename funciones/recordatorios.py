import time
import threading
from datetime import datetime
from funciones.hablar import hablar

#Recibimos el input del usuario con un formato válido
def _parse_hhmm(hora_str: str) -> str:
    return datetime.strptime(hora_str.strip(), "%H:%M").strftime("%H:%M")

def recordar_medicina(hora: str):
    """
    Función que recuerda tomar la medicina, si ingresa el horario con el formato correto
    Corre en segundo plano para seguir realizando otras tareas
    """
    try:
        hora_norm = _parse_hhmm(hora)
    except ValueError:
        hablar("Formato de hora inválido. Usa HH:MM, por ejemplo 08:30.")
        return

    hablar(f"Recordatorio de medicina configurado para las {hora_norm}.")

    def _tarea():
        """
        Revisa cada 15 segundos que coinda con el horario para avisar que debe
        tomar la medicina
        """
        while True:
            if time.strftime("%H:%M") == hora_norm:
                hablar("Es hora de tomar tu medicina.")
                break
            time.sleep(15)

    """
    Ejecutamos un hilo con la función tarea, un demon thread terminan cua
    el programa principal finaliza, ejecuta en paralelo       
    """
    threading.Thread(target=_tarea, daemon=True).start()

def recordar_agua(intervalo_min=180):
    """
    Recordatorio recurrente cada X minutos, en segundo plano.
    """
    hablar(f"Te recordaré tomar agua cada {intervalo_min} minutos")

    def _tarea():
        while True:
            time.sleep(intervalo_min)
            hablar("¡Toma un vaso de agua!")

    threading.Thread(target=_tarea, daemon=True).start()

def recordar_ejercicio(intervalo_min=180):
    """
    Recordatorio recurrente cada X minutos, en segundo plano.
    """
    hablar(f"Te recordaré hacer ejercicio cada {intervalo_min} minutos (en segundo plano).")

    def _tarea():
        while True:
            time.sleep(intervalo_min) #termina el programa cada 5 minutos
            hablar("¡Es hora de moverte un poco!")

    threading.Thread(target=_tarea, daemon=True).start()


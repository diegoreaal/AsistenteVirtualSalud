import time
from funciones.hablar import hablar

def recordar_medicina(hora):
    hablar(f"Recordatorio configurado para las {hora}.")
    while True:
        hora_actual = time.strftime("%H:%M")
        if hora_actual == hora:
            hablar("Es hora de tomar tu medicina.")
            break
        time.sleep(30)

def recordar_agua():
    hablar("Te recordaré cada 2 horas que tomes agua.")
    while True:
        time.sleep(7200)  # 2 horas
        hablar("¡Toma un vaso de agua!")

def recordar_ejercicio():
    hablar("Te recordaré hacer ejercicio cada 4 horas.")
    while True:
        time.sleep(14400)  # 4 horas
        hablar("¡Es hora de moverte un poco!")

from funciones.hablar import hablar
from funciones.microfono import transformar_audio_texto
from funciones.recordatorios import recordar_medicina, recordar_agua, recordar_ejercicio
from funciones.monitoreo import mostrar_pasos
from funciones.teleasistencia import consulta
from funciones.turno import agendar_turno


def menu():
    opciones = (
        "\n--- Asistente Virtual Salud ---\n"
        "1. Recordatorio de medicinas\n"
        "2. Recordatorio para tomar agua\n"
        "3. Recordatorio para hacer ejercicio\n"
        "4. Monitoreo de pasos\n"
        "5. Consulta\n"
        "6. Agendar turno en Google Calendar\n"
        "7. Salir\n"
    )
    print(opciones)
    hablar("Dime una opción: medicinas, agua, ejercicio, pasos, consulta, turno o salir.")


def select_option(opcion: str) -> bool:
    opcion = opcion.lower().strip()

    if "medicina" in opcion or opcion == "1":
        hora = input("¿A qué hora debo recordarte tomar la medicina? (HH:MM): ")
        recordar_medicina(hora)

    elif "agua" in opcion or opcion == "2":
        recordar_agua()

    elif "ejercicio" in opcion or opcion == "3":
        recordar_ejercicio()

    elif "pasos" in opcion or opcion == "4":
        mostrar_pasos()

    elif "consulta" in opcion or opcion == "5":
        consulta()

    elif "turno" in opcion or opcion == "6":
        link = agendar_turno()
        if link:
            hablar("He agendado tu turno en Google Calendar.")
            print("Evento creado:", link)

    elif "salir" in opcion or opcion == "7":
        hablar("¡Hasta luego! Cuida tu salud.")
        return False

    else:
        hablar("Opción no válida, intenta nuevamente.")

    return True


def main():
    hablar("Hola, soy tu asistente virtual de salud. ¿En qué puedo ayudarte?")

    while True:
        menu()
        opcion = transformar_audio_texto()

        if not opcion or opcion.lower() in ["sigo esperando", "no entendí"]:
            hablar("No entendí lo que dijiste. Vamos a intentarlo de nuevo.")
            continue

        if not select_option(opcion):
            break


if __name__ == "__main__":
    main()

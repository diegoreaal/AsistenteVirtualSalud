from funciones.hablar import hablar
from funciones.recordatorios import recordar_medicina, recordar_agua, recordar_ejercicio
from funciones.monitoreo import mostrar_pasos
from funciones.teleasistencia import consulta
import speech_recognition as sr


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

def menu():
    opciones = (
        "\n--- Asistente Virtual Salud ---\n"
        "1. Recordatorio de medicinas\n"
        "2. Recordatorio para tomar agua\n"
        "3. Recordatorio para hacer ejercicio\n"
        "4. Monitoreo de pasos\n"
        "5. Registro de síntomas\n"
        "6. Salir\n"
    )
    print(opciones)
    hablar("Dime una opción: medicinas, agua, ejercicio, pasos, síntomas o salir.")


def select_option(opcion):
    if "medicina" in opcion or opcion == "1":
        hora = input("¿A qué hora debo recordarte tomar la medicina? (HH:MM): ")
        recordar_medicina(hora)
    elif "agua" in opcion or opcion == "2":
        recordar_agua()
    elif "ejercicio" in opcion or opcion == "3":
        recordar_ejercicio()
    elif "pasos" in opcion or opcion == "4":
        mostrar_pasos()
    elif "sintoma" in opcion or opcion == "5":
        consulta()  # aquí se vuelve a usar micrófono para síntomas
    elif "salir" in opcion or opcion == "6":
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

        if not opcion:
            opcion = input("No entendí. Escribe tu opción: ")

        if not select_option(opcion):
            break


if __name__ == "__main__":
    main()

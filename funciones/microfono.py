import speech_recognition as sr

def transformar_audio_texto():
    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print("Ya puedes hablar")

        # Guardar el audio
        audio = r.listen(origen)

        try:
            # Buscar en Google
            pedido = r.recognize_google(audio, language="es-ES")

            # Imprimir prueba de ingreso
            print(f"Dijiste: {pedido}")

            return pedido
        except sr.UnknownValueError:
            print("Ups, no entendí")
            return None
        except sr.RequestError:
            print("Ups, no hay servicio")
            return None
        except Exception as e:
            print(f"Ups, algo ha salido mal: {e}")
            return None

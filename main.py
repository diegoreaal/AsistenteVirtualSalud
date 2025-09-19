from funciones.hablar import hablar
from funciones.recordatorios import recordar_medicina, recordar_agua, recordar_ejercicio
from funciones.monitoreo import mostrar_pasos
from funciones.teleasistencia import consulta

def menu():
    print("\n--- Asistente Virtual Salud ---")
    print("1. Recordatorio de medicinas")
    print("2. Recordatorio para tomar agua")
    print("3. Recordatorio para hacer ejercicio")
    print("4. Monitoreo de pasos")
    print("5. Registro de síntomas")
    print("6. Salir")

def select_option(opcion):
    if opcion == "1":
        hora = input("¿A qué hora debo recordarte tomar la medicina? (HH:MM): ")
        recordar_medicina(hora)
    elif opcion == "2":
        recordar_agua()
    elif opcion == "3":
        recordar_ejercicio()
    elif opcion == "4":
        mostrar_pasos()
    elif opcion == "5":
        consulta()
    elif opcion == "6":
        hablar("¡Hasta luego! Cuida tu salud.")
        return False
    else:
        hablar("Opción no válida, intenta nuevamente.")

    return True

def main():
    hablar("Hola, soy tu asistente virtual de salud. ¿En qué puedo ayudarte?")

    while True:
        menu()
        opcion = input("Elige una opción: ")

        if not select_option(opcion):
            break

if __name__ == "__main__":
    main()

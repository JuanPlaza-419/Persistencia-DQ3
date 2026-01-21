import json
import os

ARCHIVO_DB = "dq3_personajes.json"

# ==================================================
# PRESISTENCIA
# ==================================================
def asegurar_archivo():
    if not os.path.exists(ARCHIVO_DB):
        with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)


def leer_archivo():
    with open(ARCHIVO_DB, "r", encoding="utf-8") as f:
        return json.load(f)


def escribir_archivo(data):
    with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def write_personaje(personaje):
    data = leer_archivo()
    data.append(personaje)
    escribir_archivo(data)


def read_all_personajes():
    return leer_archivo()


def delete_personaje(personaje_id):
    data = leer_archivo()
    nuevo_data = [p for p in data if p["id"] != personaje_id]

    if len(nuevo_data) == len(data):
        return False

    escribir_archivo(nuevo_data)
    return True


# ==================================================
# VISUAL
# ==================================================
def imprimir_personaje(personaje):
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Nombre : {personaje['nombre']}")
    print(f"Clase  : {personaje['clase']}")
    print(f"Nivel  : {personaje['nivel']}")
    print("Estadísticas:")
    for stat, valor in personaje["estadisticas"].items():
        print(f"   • {stat.capitalize():12}: {valor}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")


def imprimir_todos():
    personajes = read_all_personajes()
    if not personajes:
        print("No hay personajes guardados.")
        return

    for personaje in personajes:
        imprimir_personaje(personaje)


# ==================================================
# MENÚS
# ==================================================
def crear_personaje():
    try:
        personaje = {
            "id": int(input("ID del personaje: ")),
            "nombre": input("Nombre: "),
            "clase": input("Clase: "),
            "nivel": int(input("Nivel: ")),
            "estadisticas": {
                "fuerza": int(input("Fuerza: ")),
                "agilidad": int(input("Agilidad: ")),
                "resiliencia": int(input("Resiliencia: ")),
                "sabiduria": int(input("Sabiduría: ")),
                "suerte": int(input("Suerte: "))
            }
        }
        write_personaje(personaje)
        print("Personaje añadido correctamente")

    except ValueError:
        print("Error: introduce números donde corresponda")


def eliminar_personaje_menu():
    try:
        personaje_id = int(input("ID del personaje a eliminar: "))
        if delete_personaje(personaje_id):
            print("Personaje eliminado correctamente")
        else:
            print("No existe un personaje con ese ID")
    except ValueError:
        print("El ID debe ser un número")


def menu():
    while True:
        print("\nDRAGON QUEST III - GESTIÓN DE PERSONAJES")
        print("1️ Ver personajes")
        print("2️ Añadir personaje")
        print("3️ Eliminar personaje")
        print("4️ Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            imprimir_todos()

        elif opcion == "2":
            crear_personaje()

        elif opcion == "3":
            eliminar_personaje_menu()

        elif opcion == "4":
            print("¡Hasta la próxima!")
            break

        else:
            print("Opción no válida")


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================
if __name__ == "__main__":
    asegurar_archivo()
    menu()

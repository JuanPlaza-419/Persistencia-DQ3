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

# ==================================================
# READ
# ==================================================

def leer_archivo():
    with open(ARCHIVO_DB, "r", encoding="utf-8") as f:
        return json.load(f)

def read_all_personajes():
    return leer_archivo()

# ==================================================
# WRITE
# ==================================================

def escribir_archivo(data):
    with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def write_personaje(personaje):
    data = leer_archivo()
    data.append(personaje)
    escribir_archivo(data)


# ==================================================
# DELETE
# ==================================================

def delete_personaje(personaje_id):
    data = leer_archivo()
    nuevo_data = [p for p in data if p["id"] != personaje_id]

    if len(nuevo_data) == len(data):
        return False

    escribir_archivo(nuevo_data)
    return True

# ==================================================
# UPDATE
# ==================================================
def update_personaje(personaje_id, nuevos_datos):
    data = leer_archivo()

    for i, personaje in enumerate(data):
        if personaje["id"] == personaje_id:
            data[i].update(nuevos_datos)
           
            escribir_archivo(data)
            return True
    return False

# ==================================================
# CLEAR
# ==================================================

def clear_personajes():

    escribir_archivo([])
    print("Todos los personajes han sido eliminados.")

# ==================================================
# IMPRESION BASICA
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
def actualizar_personaje_menu():

    try:
        personaje_id = int(input("ID del personaje a actualizar: "))
        data = read_all_personajes()
        personaje = next((p for p in data if p["id"] == personaje_id), None)

        if not personaje:
            print("No existe un personaje con ese ID")
            return

        print("Qué quieres actualizar:")
        print("1️ Nombre")
        print("2️ Clase")
        print("3️ Nivel")
        print("4️ Estadísticas")
        opcion = input("Opción: ")

        nuevos_datos = {}

        if opcion == "1":
            nuevos_datos["nombre"] = input("Nuevo nombre: ")
        elif opcion == "2":
            nuevos_datos["clase"] = input("Nueva clase: ")
        elif opcion == "3":
            nuevos_datos["nivel"] = int(input("Nuevo nivel: "))
        elif opcion == "4":

            estadisticas = personaje["estadisticas"]
            for stat in estadisticas:
                nuevo_valor = input(f"{stat.capitalize()} ({estadisticas[stat]}): ")
                if nuevo_valor.strip() != "":
                    estadisticas[stat] = int(nuevo_valor)
            nuevos_datos["estadisticas"] = estadisticas
        else:
            print("Opción no válida")
            return

        if update_personaje(personaje_id, nuevos_datos):
            print("Personaje actualizado correctamente")
        else:
            print("Error al actualizar")

    except ValueError:
        print("Introduce números válidos donde corresponda")


def menu():
    while True:
        print("\nDRAGON QUEST III - GESTIÓN DE PERSONAJES")
        print("1️ Ver personajes")
        print("2️ Añadir personaje")
        print("3️ Actualizar personaje")
        print("4️ Eliminar personaje")
        print("5️ Borrar todos los personajes")
        print("6️ Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            imprimir_todos()
        elif opcion == "2":
            crear_personaje()
        elif opcion == "3":
            actualizar_personaje_menu()
        elif opcion == "4":
            eliminar_personaje_menu()
        elif opcion == "5":
            confirm = input("Esto eliminará todo, ¿seguro? (s/n): ")
            if confirm.lower() == "s":
                clear_personajes()
            else:
                print("Cancelado")
        elif opcion == "6":
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

import os

# ==================================================
# Test 1º Escribir y Leer
# Comprueba que los datos escritos se puedan leer correctamente
# ==================================================
def test_write_and_read():
    # Escribe un diccionario en el archivo JSON

    # Lee el contenido del archivo

    # Verifica que los datos leídos sean iguales a los escritos


# ==================================================
# Test 2º Write sobrescribe el contenido anterior
# Comprueba que write reemplaza completamente los datos existentes
# ==================================================
def test_write_overwrites():
    # Escribe un primer contenido

    # Escribe un nuevo contenido

    # Verifica que el contenido anterior haya sido sobrescrito

# ==================================================
# Test 3º Update agrega una nueva clave
# Comprueba que update puede añadir una clave nueva
# ==================================================
def test_update_adds_key():
    # Inicializa el archivo vacío

    # Agrega una nueva clave con update

    # Verifica que la clave se haya añadido correctamente

# ==================================================
# Test 4º Update modifica una clave existente
# Comprueba que update cambia el valor de una clave ya existente
# ==================================================
def test_update_updates_value():
    # Escribe un valor inicial

    # Actualiza el valor de la clave existente

    # Verifica que el valor haya sido actualizado

# ==================================================
# Test 5º Update guarda valores de tipo lista
# Comprueba que update admite listas como valor
# ==================================================
def test_update_list_value():
    # Inicializa el archivo vacío

    # Guarda una lista como valor

    # Verifica que la lista se haya guardado correctamente

# ==================================================
# Test 6º Clear deja el archivo vacío
# Comprueba que clear elimina todos los datos del archivo
# ==================================================
def test_clear():
    # Escribe datos iniciales

    # Limpia el contenido del archivo

    # Verifica que el archivo esté vacío

# ==================================================
# Test 7º Clear no borra el archivo
# Comprueba que clear no elimina el archivo físico
# ==================================================
def test_clear_does_not_delete_file():
    # Escribe datos iniciales

    # Limpia el contenido

    # Verifica que el archivo siga existiendo

# ==================================================
# Test 8º Delete elimina el archivo
# Comprueba que delete borra el archivo del sistema
# ==================================================
def test_delete_removes_file():
    # Crea el archivo

    # Elimina el archivo

    # Verifica que el archivo ya no existe


# ==================================================
# Test 9º Write crea el archivo si no existe
# Comprueba que write crea el archivo automáticamente
# ==================================================
def test_write_creates_file():
    # Elimina el archivo si existe

    # Escribe datos en el archivo

    # Verifica que el archivo fue creado


# ==================================================
# Test 10º Read no modifica el archivo
# Comprueba que read no altera el contenido del archivo
# ==================================================
def test_read_does_not_change_file():
    # Escribe datos iniciales

    # Lee el archivo (solo lectura)

    # Verifica que el contenido sigue siendo el mismo
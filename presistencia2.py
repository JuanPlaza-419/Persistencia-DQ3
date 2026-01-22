import json
import os

# ==================================================
# READ
# ==================================================

def read(file_path):
    return _open_json(file_path, "r")

# ==================================================
# WRITE
# ==================================================

def write(file_path, data):
    _open_json(file_path, "w", data)

# ==================================================
# UPDATE
# ==================================================

def update(file_path, key, value):
    data = read(file_path)
    data[key] = value
    write(file_path, data)

# ==================================================
# CLEAR
# ==================================================

def clear(file_path):
    write(file_path, {})

# ==================================================
# DELETE
# ==================================================

def delete(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)










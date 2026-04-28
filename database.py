"""
DATABASE MEJORADO: Guarda tareas en archivo JSON
Las tareas se persisten en el disco y se cargan al iniciar
"""

import json
import os
from datetime import datetime

# Nombre del archivo donde se guardan las tareas
DB_FILE = "tareas.json"

# Cargar tareas del archivo o crear lista vacía
def load_tasks():
    """Carga las tareas desde el archivo JSON"""
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data["tasks"], data["next_id"]
        except:
            return [], 1
    return [], 1

# Cargar al iniciar
tasks_db, next_id = load_tasks()

def save_tasks():
    """Guarda las tareas en el archivo JSON"""
    global next_id
    data = {
        "tasks": tasks_db,
        "next_id": next_id,
        "last_save": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_task(task):
    """Agrega una tarea a la base de datos"""
    tasks_db.append(task)
    save_tasks()

def update_task(task_id, updates):
    """Actualiza una tarea"""
    for task in tasks_db:
        if task["id"] == task_id:
            task.update(updates)
            save_tasks()
            return True
    return False

def get_all_tasks():
    """Retorna todas las tareas"""
    return tasks_db

def increment_next_id():
    """Incrementa el contador de IDs"""
    global next_id
    next_id += 1
    save_tasks()
    return next_id - 1

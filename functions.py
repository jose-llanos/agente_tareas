"""
PASO 4: IMPLEMENTAR LAS FUNCIONES
Aquí van las funciones que ejecutan cada herramienta
"""

import json
from datetime import datetime
from database import get_all_tasks, add_task, update_task, increment_next_id

# ==========================================
# FUNCIÓN 1: Crear una nueva tarea
# ==========================================
def create_task(title, description, priority):
    """
    Crea una nueva tarea
    
    Args:
        title: Nombre de la tarea
        description: Descripción (opcional)
        priority: "Alta", "Media" o "Baja"
    
    Returns:
        dict con el resultado
    """
    
    task_id = increment_next_id()
    
    new_task = {
        "id": task_id,
        "title": title,
        "description": description if description else "(sin descripción)",
        "priority": priority,
        "completed": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    add_task(new_task)
    
    return {
        "status": "✅ Tarea creada exitosamente",
        "task_id": new_task["id"],
        "title": title,
        "priority": priority
    }


# ==========================================
# FUNCIÓN 2: Listar tareas con filtro
# ==========================================
def list_tasks(filter_type="todas"):
    """
    Lista tareas con filtro
    
    Args:
        filter_type: "todas", "alta", "media", "baja", "completadas", "pendientes"
    
    Returns:
        dict con las tareas filtradas
    """
    
    tasks_db = get_all_tasks()
    
    if filter_type == "todas":
        result = tasks_db
    elif filter_type == "alta":
        result = [t for t in tasks_db if t["priority"] == "Alta"]
    elif filter_type == "media":
        result = [t for t in tasks_db if t["priority"] == "Media"]
    elif filter_type == "baja":
        result = [t for t in tasks_db if t["priority"] == "Baja"]
    elif filter_type == "completadas":
        result = [t for t in tasks_db if t["completed"]]
    elif filter_type == "pendientes":
        result = [t for t in tasks_db if not t["completed"]]
    else:
        result = []
    
    # Formatear tareas para mostrar
    formatted_tasks = []
    for task in result:
        status = "✅ Hecha" if task["completed"] else "⏳ Pendiente"
        formatted_tasks.append({
            "id": task["id"],
            "titulo": task["title"],
            "prioridad": task["priority"],
            "estado": status,
            "descripcion": task["description"]
        })
    
    return {
        "filtro": filter_type,
        "cantidad": len(formatted_tasks),
        "tareas": formatted_tasks
    }


# ==========================================
# FUNCIÓN 3: Marcar tarea como completada
# ==========================================
def complete_task(task_id):
    """
    Marca una tarea como completada
    
    Args:
        task_id: ID de la tarea
    
    Returns:
        dict con el resultado
    """
    
    tasks_db = get_all_tasks()
    
    # Buscar la tarea
    task = next((t for t in tasks_db if t["id"] == task_id), None)
    
    if task:
        update_task(task_id, {"completed": True})
        return {
            "status": f"✅ Tarea {task_id} marcada como completada",
            "title": task["title"],
            "completed": True
        }
    else:
        return {
            "error": f"❌ No encontré la tarea con ID {task_id}"
        }


# ==========================================
# FUNCIÓN 4: Obtener estadísticas
# ==========================================
def get_statistics():
    """
    Calcula estadísticas de las tareas
    
    Returns:
        dict con estadísticas
    """
    
    tasks_db = get_all_tasks()
    
    total = len(tasks_db)
    completed = sum(1 for t in tasks_db if t["completed"])
    pending = total - completed
    
    by_priority = {
        "Alta": sum(1 for t in tasks_db if t["priority"] == "Alta" and not t["completed"]),
        "Media": sum(1 for t in tasks_db if t["priority"] == "Media" and not t["completed"]),
        "Baja": sum(1 for t in tasks_db if t["priority"] == "Baja" and not t["completed"])
    }
    
    return {
        "total_tareas": total,
        "tareas_completadas": completed,
        "tareas_pendientes": pending,
        "pendientes_por_prioridad": by_priority,
        "porcentaje_completado": f"{(completed/total*100):.1f}%" if total > 0 else "0%"
    }

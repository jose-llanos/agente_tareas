"""
PASO 2: DEFINIR LAS HERRAMIENTAS
Las herramientas son las funciones que Claude puede decidir usar
"""

# Aquí van todas las herramientas disponibles para el agente
tools = [
    {
        "name": "create_task",
        "description": "Crea una nueva tarea con título, descripción y prioridad",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Título o nombre de la tarea"
                },
                "description": {
                    "type": "string",
                    "description": "Descripción detallada de qué hacer"
                },
                "priority": {
                    "type": "string",
                    "enum": ["Alta", "Media", "Baja"],
                    "description": "Nivel de urgencia"
                }
            },
            "required": ["title", "priority"]
        }
    },
    {
        "name": "list_tasks",
        "description": "Lista todas las tareas o filtra por estado/prioridad",
        "input_schema": {
            "type": "object",
            "properties": {
                "filter": {
                    "type": "string",
                    "enum": ["todas", "alta", "media", "baja", "completadas", "pendientes"],
                    "description": "Tipo de filtro a aplicar"
                }
            },
            "required": ["filter"]
        }
    },
    {
        "name": "complete_task",
        "description": "Marca una tarea como completada",
        "input_schema": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "integer",
                    "description": "ID de la tarea a marcar como hecha"
                }
            },
            "required": ["task_id"]
        }
    },
    {
        "name": "get_statistics",
        "description": "Obtiene estadísticas: total de tareas, completadas, pendientes, por prioridad",
        "input_schema": {
            "type": "object",
            "properties": {}
        }
    }
]

"""
APP.PY - Servidor Flask para interfaz web
Accede a http://localhost:5000 en tu navegador
"""

from flask import Flask, render_template, request, jsonify
from database import get_all_tasks, add_task, update_task, increment_next_id
from charts import get_all_charts
from functions import get_statistics
from datetime import datetime
import json

app = Flask(__name__)

# ==========================================
# RUTAS
# ==========================================

@app.route('/')
def index():
    """Página principal"""
    tasks = get_all_tasks()
    stats = get_statistics()
    charts = get_all_charts()
    
    return render_template('index.html', 
                         tasks=tasks, 
                         stats=stats, 
                         charts=charts)


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """API: Obtener todas las tareas"""
    tasks = get_all_tasks()
    return jsonify(tasks)


@app.route('/api/tasks', methods=['POST'])
def create_task_api():
    """API: Crear nueva tarea"""
    data = request.json
    
    task_id = increment_next_id()
    new_task = {
        "id": task_id,
        "title": data.get('title', 'Sin título'),
        "description": data.get('description', ''),
        "priority": data.get('priority', 'Media'),
        "completed": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    add_task(new_task)
    return jsonify({"status": "success", "task": new_task}), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task_api(task_id):
    """API: Actualizar tarea"""
    data = request.json
    
    if update_task(task_id, data):
        return jsonify({"status": "success", "message": f"Tarea {task_id} actualizada"})
    else:
        return jsonify({"status": "error", "message": f"Tarea {task_id} no encontrada"}), 404


@app.route('/api/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task_api(task_id):
    """API: Marcar tarea como completada"""
    if update_task(task_id, {"completed": True}):
        return jsonify({"status": "success", "message": f"Tarea {task_id} completada"})
    else:
        return jsonify({"status": "error", "message": f"Tarea {task_id} no encontrada"}), 404


@app.route('/api/statistics', methods=['GET'])
def get_stats():
    """API: Obtener estadísticas"""
    stats = get_statistics()
    return jsonify(stats)


@app.route('/api/charts', methods=['GET'])
def get_charts():
    """API: Obtener gráficos"""
    charts = get_all_charts()
    return jsonify(charts)


# ==========================================
# MANEJO DE ERRORES
# ==========================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "No encontrado"}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 SERVIDOR FLASK INICIADO")
    print("="*70)
    print("\n📱 Abre tu navegador en: http://localhost:5000")
    print("\n⌨️  Para detener el servidor: Presiona Ctrl+C\n")
    print("="*70 + "\n")
    
    # debug=True permite recargar automáticamente
    app.run(debug=True, host='127.0.0.1', port=5000)

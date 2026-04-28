"""
CHARTS.PY - Genera gráficos de tareas
Crea visualizaciones con Matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
from database import get_all_tasks
import io
import base64

# Usar backend sin interfaz gráfica
matplotlib.use('Agg')

# Configurar estilo
plt.style.use('seaborn-v0_8-darkgrid')

def generate_pie_chart():
    """
    Genera un gráfico de pastel: Completadas vs Pendientes
    Retorna una imagen en base64
    """
    tasks = get_all_tasks()
    
    if not tasks:
        return None
    
    completed = sum(1 for t in tasks if t["completed"])
    pending = len(tasks) - completed
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('#f8f9fa')
    
    # Datos
    labels = ['✅ Completadas', '⏳ Pendientes']
    sizes = [completed, pending]
    colors = ['#2ecc71', '#e74c3c']
    explode = (0.05, 0)
    
    # Crear gráfico
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=90, textprops={'fontsize': 12, 'weight': 'bold'})
    ax.set_title('Estado de Tareas', fontsize=16, weight='bold', pad=20)
    
    # Convertir a base64
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
    plt.close()
    
    return f"data:image/png;base64,{img_base64}"


def generate_priority_chart():
    """
    Genera un gráfico de barras: Tareas por prioridad
    """
    tasks = get_all_tasks()
    
    if not tasks:
        return None
    
    # Contar por prioridad
    alta = sum(1 for t in tasks if t["priority"] == "Alta" and not t["completed"])
    media = sum(1 for t in tasks if t["priority"] == "Media" and not t["completed"])
    baja = sum(1 for t in tasks if t["priority"] == "Baja" and not t["completed"])
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#f8f9fa')
    
    # Datos
    prioridades = ['🔴 Alta', '🟡 Media', '🟢 Baja']
    cantidades = [alta, media, baja]
    colors = ['#e74c3c', '#f39c12', '#2ecc71']
    
    # Crear gráfico de barras
    bars = ax.bar(prioridades, cantidades, color=colors, edgecolor='black', linewidth=1.5)
    
    # Agregar valores en las barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=12, weight='bold')
    
    ax.set_ylabel('Cantidad de Tareas', fontsize=12, weight='bold')
    ax.set_title('Tareas Pendientes por Prioridad', fontsize=16, weight='bold', pad=20)
    ax.set_ylim(0, max(cantidades) + 2 if max(cantidades) > 0 else 5)
    
    # Convertir a base64
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
    plt.close()
    
    return f"data:image/png;base64,{img_base64}"


def generate_progress_chart():
    """
    Genera un gráfico de progreso: porcentaje completado
    """
    tasks = get_all_tasks()
    
    if not tasks:
        return None
    
    completed = sum(1 for t in tasks if t["completed"])
    total = len(tasks)
    percentage = (completed / total * 100) if total > 0 else 0
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 2))
    fig.patch.set_facecolor('#f8f9fa')
    
    # Crear barra de progreso
    ax.barh(['Progreso'], [percentage], height=0.5, color='#3498db', edgecolor='black', linewidth=2)
    ax.barh(['Progreso'], [100 - percentage], left=[percentage], height=0.5, color='#ecf0f1', edgecolor='black', linewidth=2)
    
    # Texto
    ax.text(50, 0, f'{percentage:.1f}%\n{completed}/{total} tareas', 
            ha='center', va='center', fontsize=14, weight='bold', color='white')
    
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.5, 0.5)
    ax.axis('off')
    ax.set_title('Progreso General', fontsize=16, weight='bold', pad=20)
    
    # Convertir a base64
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
    plt.close()
    
    return f"data:image/png;base64,{img_base64}"


def get_all_charts():
    """
    Retorna todos los gráficos
    """
    return {
        'pie': generate_pie_chart(),
        'priority': generate_priority_chart(),
        'progress': generate_progress_chart()
    }

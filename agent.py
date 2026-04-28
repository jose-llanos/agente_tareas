"""
PASO 5: LOOP PRINCIPAL DEL AGENTE
Este es el corazón del agente - donde Claude razona y ejecuta herramientas
"""

import json
import os
from dotenv import load_dotenv
from anthropic import Anthropic
from tools import tools
from functions import create_task, list_tasks, complete_task, get_statistics

# Cargar variables de entorno desde .env (opcional)
load_dotenv()

# Inicializar cliente de Anthropic
# IMPORTANTE: Tu API KEY debe estar en la variable de entorno ANTHROPIC_API_KEY
client = Anthropic()


# ==========================================
# Función auxiliar: Ejecutar una herramienta
# ==========================================
def execute_tool(tool_name, tool_input):
    """
    Ejecuta una herramienta basada en el nombre
    
    Args:
        tool_name: Nombre de la herramienta a ejecutar
        tool_input: Parámetros de entrada
    
    Returns:
        Resultado de ejecutar la herramienta
    """
    
    if tool_name == "create_task":
        return create_task(
            tool_input["title"],
            tool_input.get("description", ""),
            tool_input["priority"]
        )
    
    elif tool_name == "list_tasks":
        return list_tasks(tool_input["filter"])
    
    elif tool_name == "complete_task":
        return complete_task(tool_input["task_id"])
    
    elif tool_name == "get_statistics":
        return get_statistics()
    
    else:
        return {"error": f"Herramienta desconocida: {tool_name}"}


# ==========================================
# Función principal: Ejecutar el agente
# ==========================================
def run_task_agent(user_message):
    """
    Ejecuta el agente de tareas con un mensaje del usuario
    
    Args:
        user_message: Lo que el usuario pregunta o pide
    """
    
    print("\n" + "="*60)
    print("🤖 AGENTE DE TAREAS INICIADO")
    print("="*60)
    print(f"📝 Tú: {user_message}\n")
    
    # Historial de mensajes (empieza con el mensaje del usuario)
    messages = [
        {"role": "user", "content": user_message}
    ]
    
    # Loop principal: mientras haya herramientas que ejecutar
    continue_loop = True
    iteration = 0
    
    while continue_loop:
        iteration += 1
        print(f"\n--- Iteración {iteration} ---")
        
        # PASO 1: Llamar a Claude con las herramientas disponibles
        print("🧠 Claude está pensando...")
        
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )
        
        # PASO 2: Agregar la respuesta de Claude al historial
        messages.append({"role": "assistant", "content": response.content})
        
        # PASO 3: Procesar lo que Claude dijo/hizo
        tool_was_called = False
        
        for block in response.content:
            # Si Claude escribió texto, mostrarlo
            if block.type == "text":
                print(f"\n💬 Claude: {block.text}")
            
            # Si Claude quiere usar una herramienta
            elif block.type == "tool_use":
                tool_was_called = True
                
                print(f"\n🔧 Claude quiere usar: {block.name}")
                print(f"   Parámetros: {json.dumps(block.input, ensure_ascii=False)}")
                
                # PASO 4: Ejecutar la herramienta
                tool_result = execute_tool(block.name, block.input)
                
                print(f"   ✅ Resultado: {json.dumps(tool_result, ensure_ascii=False)}\n")
                
                # PASO 5: Decirle a Claude el resultado
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(tool_result, ensure_ascii=False)
                        }
                    ]
                })
        
        # PASO 6: Decidir si continuar el loop
        # Si Claude no usó herramientas O si Claude dice que terminó, salir del loop
        if not tool_was_called or response.stop_reason == "end_turn":
            continue_loop = False
    
    print("\n" + "="*60)
    print("✅ AGENTE COMPLETADO")
    print("="*60 + "\n")


# ==========================================
# Función para múltiples preguntas
# ==========================================
def run_multiple_tasks(queries):
    """
    Ejecuta el agente con múltiples preguntas
    
    Args:
        queries: Lista de preguntas/comandos para el agente
    """
    
    for query in queries:
        run_task_agent(query)
        print("\n")


if __name__ == "__main__":
    # Ejemplos de uso
    run_multiple_tasks([
        "Crea una tarea urgente: preparar presentación para la reunión de mañana",
        "¿Cuántas tareas tengo pendientes? Muestra todas las de alta prioridad",
        "Marca la tarea 2 como completada y dame un resumen de mi progreso"
    ])

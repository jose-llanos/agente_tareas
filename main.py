#!/usr/bin/env python3
"""
AGENTE DE TAREAS INTELIGENTE CON CLAUDE
Interfaz interactiva - Conversación continua
"""

from agent import run_task_agent

def main():
    """
    Interfaz interactiva principal
    """
    
    print("\n")
    print("="*70)
    print("✨ AGENTE INTELIGENTE DE TAREAS CON CLAUDE ✨")
    print("="*70)
    print("\n📝 Tu agenda se guarda automáticamente en 'tareas.json'\n")
    print("Escribe tus comandos naturales:")
    print("  • 'Crear tarea: ...' - Crear una nueva tarea")
    print("  • 'Listar tareas' - Ver todas tus tareas")
    print("  • 'Tareas de alta prioridad' - Filtrar por prioridad")
    print("  • 'Completar tarea 1' - Marcar como hecha")
    print("  • 'Estadísticas' - Ver progreso")
    print("  • 'salir' o 'quit' - Terminar\n")
    print("="*70 + "\n")
    
    # Loop de conversación continua
    while True:
        try:
            # Leer entrada del usuario
            user_input = input("💬 Tú: ").strip()
            
            # Validaciones
            if not user_input:
                print("❌ Por favor escribe algo\n")
                continue
            
            # Salir del programa
            if user_input.lower() in ["salir", "quit", "exit", "bye"]:
                print("\n👋 ¡Hasta luego! Tus tareas se han guardado.\n")
                break
            
            # Ejecutar agente
            print()
            run_task_agent(user_input)
            print()
        
        except KeyboardInterrupt:
            print("\n\n👋 Agente interrumpido. ¡Hasta luego!\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("   Intenta de nuevo\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        print("\n💡 Asegúrate de que:")
        print("   1. Tienes instalada la librería: pip install anthropic python-dotenv")
        print("   2. Tu API KEY está en la variable ANTHROPIC_API_KEY")
        print("   3. Tienes conexión a internet\n")

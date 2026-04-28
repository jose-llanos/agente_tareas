# 🤖 AGENTE DE TAREAS CON CLAUDE

Un agente inteligente que gestiona tus tareas usando la API de Claude.

## ¿Qué hace?

El agente puede:
- ✅ **Crear tareas** con título, descripción y prioridad
- 📋 **Listar tareas** con filtros (por prioridad, estado)
- ✔️ **Marcar tareas** como completadas
- 📊 **Ver estadísticas** de progreso

## Instalación

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

O manualmente:
```bash
pip install anthropic python-dotenv
```

### 2. Configurar tu API KEY

#### Opción A: Variable de entorno (RECOMENDADO)

**Linux/Mac:**
```bash
export ANTHROPIC_API_KEY="tu-clave-aqui"
python main.py
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="tu-clave-aqui"
python main.py
```

#### Opción B: Archivo .env

1. Copia `.env.example` a `.env`
2. Reemplaza `sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx` con tu clave real
3. Ejecuta: `python main.py`

## Uso

### Ejecutar ejemplos predefinidos

```bash
python main.py
# Selecciona opción 1
```

### Ejecutar una pregunta específica

```bash
python main.py
# Selecciona opción 2
# Escribe tu pregunta
```

### Ejecutar directamente desde Python

```python
from agent import run_task_agent

run_task_agent("Crea una tarea: ir al supermercado")
run_task_agent("¿Cuántas tareas tengo pendientes?")
run_task_agent("Marca la tarea 1 como completada")
```

## Ejemplos de preguntas

El agente entiende preguntas naturales como:

```
"Crea una tarea urgente: preparar presentación"
"¿Cuántas tareas tengo?"
"Muestra mis tareas de alta prioridad"
"Marca la tarea 2 como hecha"
"¿Cuál es mi progreso?"
"Necesito una lista de cosas por hacer"
"Completa todas mis tareas de baja prioridad"
```

## Estructura del código

```
tarea_agente/
├── main.py           # Archivo principal (ejecutar esto)
├── agent.py          # Loop del agente
├── functions.py      # Funciones que ejecutan las herramientas
├── tools.py          # Definición de herramientas
├── database.py       # Datos simulados (tareas)
├── requirements.txt  # Dependencias
├── .env.example      # Plantilla para API KEY
└── README.md         # Este archivo
```

## ¿Cómo funciona internamente?

```
1. Usuario pregunta algo
   ↓
2. Se envía a Claude con herramientas disponibles
   ↓
3. Claude decide qué herramienta usar
   ↓
4. El agente ejecuta esa herramienta
   ↓
5. Se envía el resultado a Claude
   ↓
6. ¿Necesita más herramientas? → Volver a paso 3
   ↓
7. Claude da la respuesta final
```

## Troubleshooting

### Error: "No module named 'anthropic'"
```bash
pip install anthropic
```

### Error: "APIError: Unauthorized"
- Verifica que tu API KEY es correcta
- Asegúrate de que está en `ANTHROPIC_API_KEY`
- No incluyas comillas en la variable de entorno

### Error: "No module named 'dotenv'"
```bash
pip install python-dotenv
```

## Personalizar el agente

### Agregar una nueva herramienta

1. Agrega la herramienta a `tools.py`
2. Implementa la función en `functions.py`
3. Agrega el caso en `execute_tool()` en `agent.py`

### Cambiar las tareas iniciales

Edita `database.py` y modifica la lista `tasks_db`

## Próximos pasos

- Conectar a una base de datos real (en lugar de lista en memoria)
- Agregar persistencia (guardar tareas en archivo o DB)
- Agregar más herramientas (eliminar tareas, editar, etc.)
- Crear una interfaz web
- Agregar autenticación de usuarios

## Licencia

Libre para usar y modificar

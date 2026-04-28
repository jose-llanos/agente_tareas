# 🌐 INTERFAZ WEB CON FLASK

Tu agente ahora tiene una interfaz web visual para gestionar tareas en el navegador.

---

## 📦 Instalación

### Paso 1: Instalar dependencias nuevas

```bash
pip install flask matplotlib
```

O reinstala todo:

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecutar el servidor

```bash
python app.py
```

Deberías ver algo como:

```
======================================================================
🚀 SERVIDOR FLASK INICIADO
======================================================================

📱 Abre tu navegador en: http://localhost:5000

⌨️  Para detener el servidor: Presiona Ctrl+C

======================================================================
```

---

## 🌐 Acceder a la web

Abre tu navegador y ve a:

```
http://localhost:5000
```

¡Verás un dashboard bonito con tus tareas! 🎨

---

## 📊 Características de la Interfaz Web

### 1. **Dashboard Principal**
- Vista general con el logo y descripción
- Indicadores de estadísticas en tiempo real

### 2. **Estadísticas**
- Total de tareas
- Tareas completadas
- Tareas pendientes
- Porcentaje de progreso

### 3. **Gráficos Dinámicos**
- **Gráfico de Progreso**: Barra horizontal con % completado
- **Gráfico de Pastel**: Completadas vs Pendientes
- **Gráfico de Barras**: Tareas por prioridad
- Todos generados con **Matplotlib** ✨

### 4. **Gestión de Tareas**
- ➕ **Crear tareas**: Título, descripción, prioridad
- ✓ **Marcar como completada**: Con un clic
- 🎯 **Filtrado visual**: Por prioridad (Alta/Media/Baja)

### 5. **Diseño Responsive**
- Funciona en desktop, tablet y móvil
- Colores y transiciones agradables

---

## 📝 Cómo usar

### Crear una tarea

1. Escribe el **título** en el primer campo
2. (Opcional) Escribe una **descripción**
3. Selecciona la **prioridad** (🔴 Alta, 🟡 Media, 🟢 Baja)
4. Presiona **➕ Crear** o Enter

### Completar una tarea

1. Encuentra la tarea en la lista
2. Presiona el botón **✓ Completar**
3. La tarea desaparecerá o se marcará como hecha

### Ver estadísticas

- Las tarjetas superiores muestran resumen en tiempo real
- Los gráficos se actualizan automáticamente

---

## 🔧 Estructura de archivos

```
tarea_agente/
├── app.py                 # Servidor Flask (ejecuta esto)
├── charts.py              # Generador de gráficos
├── database.py            # Base de datos (tareas.json)
├── functions.py           # Lógica de tareas
├── tools.py               # Definición de herramientas
├── agent.py               # Agente inteligente
├── main.py                # CLI (terminal)
├── tareas.json            # Archivo de tareas
├── requirements.txt       # Dependencias
└── templates/
    └── index.html         # Página web
```

---

## 🔌 Rutas API Disponibles

El servidor expone APIs REST que puedes usar:

### GET /api/tasks
Obtener todas las tareas

```bash
curl http://localhost:5000/api/tasks
```

### POST /api/tasks
Crear una nueva tarea

```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Mi tarea","priority":"Alta"}'
```

### PUT /api/tasks/<id>
Actualizar una tarea

```bash
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"description":"Nueva descripción"}'
```

### PUT /api/tasks/<id>/complete
Marcar como completada

```bash
curl -X PUT http://localhost:5000/api/tasks/1/complete
```

### GET /api/statistics
Obtener estadísticas

```bash
curl http://localhost:5000/api/statistics
```

### GET /api/charts
Obtener gráficos (como imágenes base64)

```bash
curl http://localhost:5000/api/charts
```

---

## 🎨 Gráficos Generados

Los gráficos se generan automáticamente con **Matplotlib**:

### 1. Gráfico de Progreso
```
████████████░░░░░░░░
75.0%
6/8 tareas
```

### 2. Gráfico de Pastel
```
     ✅ Completadas (60%)
    /
   /
  \
   \
    ✗ Pendientes (40%)
```

### 3. Gráfico de Barras
```
Alta   | ███
Media  | █████
Baja   | ██
```

---

## 🌡️ Cómo trabaja internamente

```
1. Usuario abre http://localhost:5000
   ↓
2. Flask carga index.html
   ↓
3. HTML obtiene datos desde /api/tasks
   ↓
4. charts.py genera gráficos con Matplotlib
   ↓
5. Los gráficos se convierten a base64 e inyectan en HTML
   ↓
6. Usuario ve todo en el navegador ✨
```

---

## 🛠️ Personalizaciones

### Cambiar el puerto

En `app.py`, línea final:

```python
# Cambiar 5000 por otro puerto (ej: 8080)
app.run(debug=True, host='127.0.0.1', port=8080)
```

### Cambiar colores de gráficos

En `charts.py`, modifica los colores hex:

```python
colors = ['#e74c3c', '#f39c12', '#2ecc71']  # Rojo, Naranja, Verde
```

### Agregar más campos a las tareas

1. Modifica `index.html` (agregar input)
2. Actualiza `app.py` (endpoint POST)
3. Actualiza `database.py` (guardar campo)

---

## 🐛 Troubleshooting

### Error: "No module named 'flask'"
```bash
pip install flask
```

### Error: "No module named 'matplotlib'"
```bash
pip install matplotlib
```

### No se ve en el navegador
- Verifica que el servidor está corriendo: `python app.py`
- Abre exactamente: `http://localhost:5000` (no 127.0.0.1)
- Intenta Ctrl+F5 para limpiar caché

### Los gráficos no aparecen
- Verifica que hay tareas creadas
- Recarga la página (F5)
- Revisa la consola del navegador (F12 → Console)

### El puerto 5000 está en uso
```bash
# Encontrar qué usa el puerto
lsof -i :5000

# O cambia el puerto en app.py
app.run(debug=True, host='127.0.0.1', port=8080)
```

---

## 💡 Próximos pasos

- ✅ Agregar login de usuarios
- ✅ Sincronizar con base de datos (SQLite, PostgreSQL)
- ✅ Exportar tareas a PDF
- ✅ Aplicación móvil
- ✅ Notificaciones en tiempo real (WebSockets)

---

## Resumen

| Antes | Ahora |
|-------|-------|
| CLI solo (terminal) | Web + CLI |
| Sin gráficos | Gráficos dinámicos con Matplotlib |
| No visual | Dashboard hermoso |
| Texto plano | Interfaz moderna |

¡Tu agente ahora es **web-enabled**! 🚀

Ejecuta: `python app.py` y abre http://localhost:5000

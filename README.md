# Examen Python — Instituto Mexicano del Petróleo

## Archivos

| Archivo | Descripción |
|---|---|
| `app.py` | App principal Streamlit |
| `preguntas.py` | Banco de 10 preguntas (editar aquí) |
| `requirements.txt` | Dependencias para Streamlit Cloud |
| `calificaciones.csv` | Se genera automáticamente al primer envío |

## Cómo agregar o editar preguntas

Abre `preguntas.py` y sigue la estructura:

### Pregunta de escritura libre
```python
{
    "id": 11,
    "tipo": "escritura",
    "enunciado": "Escribe aquí el enunciado con **markdown**",
    "placeholder": "Pista visual para el alumno",
    "respuestas_validas": ["respuesta1", "respuesta2"],  # todas las formas válidas
    "puntaje": 1,
},
```

### Pregunta de opción múltiple
```python
{
    "id": 12,
    "tipo": "opcion_multiple",
    "enunciado": "¿Cuál opción es correcta?",
    "opciones": ["opción A", "opción B", "opción C", "opción D"],
    "respuesta_correcta": "opción B",
    "puntaje": 1,
},
```

## Deploy en Streamlit Cloud (gratis)

1. Sube los 3 archivos a un repositorio de GitHub
2. Entra a https://share.streamlit.io
3. Conecta tu cuenta de GitHub
4. Selecciona el repo y pon `app.py` como archivo principal
5. Click en **Deploy** — en ~2 minutos tendrás tu URL pública

## Calificaciones

El archivo `calificaciones.csv` se guarda en el servidor.
Desde la pantalla de resultados, cualquier alumno (o la profesora) puede descargarlo con el botón **📥 Descargar calificaciones.csv**.

> **Nota:** En Streamlit Cloud el CSV se resetea si el servidor se reinicia.
> Para persistencia permanente considera usar Google Sheets vía `gspread` o una base de datos.

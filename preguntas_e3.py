# ============================================================
#  BANCO DE PREGUNTAS — Examen 3 / IMP
#  Control de Flujo: IF, ELIF, ELSE, WHILE, FOR
# ============================================================

PREGUNTAS = [

    # ── P1 — Completar IF-ELIF-ELSE ────────────────────────
    {
        "id": 1,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que clasifica por edad:\n\n"
            "```python\n"
            "edad = 15\n"
            "if edad >= 18:\n"
            "    print(\"Adulto\")\n"
            "______ edad >= 13:\n"
            "    print(\"Adolescente\")\n"
            "______:\n"
            "    print(\"Niño\")\n"
            "```\n\n"
            "Escribe las dos líneas que faltan (sin 'print'):"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "elif edad >= 13:\nelse:",
            "elif edad>=13:\nelse:",
        ],
        "puntaje": 1,
    },

    # ── P2 — Opción múltiple IF-ELIF-ELSE con calificaciones 
    {
        "id": 2,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál código verifica si una calificación es A (90+), B (80-89), C (70-79) o F (<70)?"
        ),
        "opciones": [
            "if cal >= 90:\n    print(\"A\")\nelse:\n    print(\"B\")",
            "if cal >= 90:\n    print(\"A\")\nelif cal >= 80:\n    print(\"B\")\nelif cal >= 70:\n    print(\"C\")\nelse:\n    print(\"F\")",
            "if cal == 90:\n    print(\"A\")",
            "if cal > 70:\n    print(\"A\")",
        ],
        "respuesta_correcta": "if cal >= 90:\n    print(\"A\")\nelif cal >= 80:\n    print(\"B\")\nelif cal >= 70:\n    print(\"C\")\nelse:\n    print(\"F\")",
        "puntaje": 1,
    },

    # ── P3 — Escribir código IF-ELIF-ELSE ──────────────────
    {
        "id": 3,
        "tipo": "escritura",
        "enunciado": (
            "Escribe código que imprima 'positivo', 'negativo' o 'cero' según el número.\n\n"
            "Considera `numero = 5`"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "if numero > 0:\n    print(\"positivo\")\nelif numero < 0:\n    print(\"negativo\")\nelse:\n    print(\"cero\")",
            "if numero>0:\n    print(\"positivo\")\nelif numero<0:\n    print(\"negativo\")\nelse:\n    print(\"cero\")",
        ],
        "puntaje": 1,
    },

    # ── P4 — Completar WHILE ───────────────────────────────
    {
        "id": 4,
        "tipo": "escritura",
        "enunciado": (
            "Completa el operador para que imprima 1, 2, 3, 4, 5:\n\n"
            "```python\n"
            "i = 1\n"
            "while i ______ 5:\n"
            "    print(i)\n"
            "    i += 1\n"
            "```\n\n"
            "Escribe solo el operador:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "<= 5",
            "< 6",
        ],
        "puntaje": 1,
    },

    # ── P5 — Opción múltiple WHILE ──────────────────────────
    {
        "id": 5,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál código imprime números del 1 al 5 usando `while`?"
        ),
        "opciones": [
            "i = 1\nwhile i < 5:\n    print(i)\n    i += 1",
            "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1",
            "i = 1\nwhile i >= 5:\n    print(i)\n    i += 1",
            "while True:\n    print(i)\n    i += 1",
        ],
        "respuesta_correcta": "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1",
        "puntaje": 1,
    },

    # ── P6 — Escribir IF anidado con acción clara ──────────
    {
        "id": 6,
        "tipo": "escritura",
        "enunciado": (
            "Escribe código que imprima 'válido' solo si el número es positivo Y par.\n"
            "Si no cumple ambas condiciones, no imprime nada.\n\n"
            "Considera `numero = 6`"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "if numero > 0:\n    if numero % 2 == 0:\n        print(\"válido\")",
            "if numero>0:\n    if numero%2==0:\n        print(\"válido\")",
            "if numero > 0 and numero % 2 == 0:\n    print(\"válido\")",
        ],
        "puntaje": 1,
    },

    # ── P7 — Completar AND ───────────────────────────────────
    {
        "id": 7,
        "tipo": "escritura",
        "enunciado": (
            "Completa el operador lógico para que imprima solo si está entre 1 y 9:\n\n"
            "```python\n"
            "numero = 7\n"
            "if numero > 0 ______ numero < 10:\n"
            "    print(\"Está entre 1 y 9\")\n"
            "```\n\n"
            "Escribe solo el operador:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "and",
        ],
        "puntaje": 1,
    },

    # ── P8 — Opción múltiple resultado ELSE ─────────────────
    {
        "id": 8,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál es la salida exacta de este código?\n\n"
            "```python\n"
            "x = 5\n"
            "if x > 10:\n"
            "    print(\"Mayor\")\n"
            "else:\n"
            "    print(\"Menor\")\n"
            "```"
        ),
        "opciones": [
            "Mayor",
            "Menor",
            "Error",
            "Nada",
        ],
        "respuesta_correcta": "Menor",
        "puntaje": 1,
    },

    # ── P9 — Escribir WHILE con condición clara ────────────
    {
        "id": 9,
        "tipo": "escritura",
        "enunciado": (
            "Escribe un `while` que imprima solo los números impares desde 0 hasta 3 (inclusive).\n\n"
            "Resultado esperado: imprime 1 y 3"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "i = 0\nwhile i <= 3:\n    if i % 2 != 0:\n        print(i)\n    i += 1",
            "i=0\nwhile i<=3:\n    if i%2!=0:\n        print(i)\n    i+=1",
            "i = 0\nwhile i <= 3:\n    if i % 2 == 1:\n        print(i)\n    i += 1",
        ],
        "puntaje": 1,
    },

    # ── P10 — Valor final en WHILE ──────────────────────────
    {
        "id": 10,
        "tipo": "escritura",
        "enunciado": (
            "¿Cuál es el valor final de `x` después de ejecutar este código?\n\n"
            "```python\n"
            "x = 0\n"
            "i = 1\n"
            "while i <= 4:\n"
            "    x = x + i\n"
            "    i += 1\n"
            "print(x)\n"
            "```\n\n"
            "Escribe solo el número que se imprime:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "10",
        ],
        "puntaje": 1,
    },
]

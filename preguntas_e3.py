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
            "Completa el código con `elif` y `else`:\n\n"
            "```python\n"
            "edad = 15\n"
            "if edad >= 18:\n"
            "    print(\"Mayor\")\n"
            "______ edad >= 13:\n"
            "    print(\"Adolescente\")\n"
            "______:\n"
            "    print(\"Niño\")\n"
            "```\n\n"
            "Escribe las dos líneas que faltan (con indentación):"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "elif edad >= 13:\nelse:",
            "elif edad>=13:\nelse:",
            "elif edad >= 13 :\nelse :",
        ],
        "puntaje": 1,
    },

    # ── P2 — Opción múltiple IF-ELSE ────────────────────────
    {
        "id": 2,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál código verifica si un número es positivo o negativo?"
        ),
        "opciones": [
            'if numero > 0: print("positivo") else: print("negativo")',
            'if numero >= 0: print("positivo") else: print("negativo")',
            'if numero == 0: print("cero")',
            'if numero < 0: print("negativo")',
        ],
        "respuesta_correcta": 'if numero > 0: print("positivo") else: print("negativo")',
        "puntaje": 1,
    },

    # ── P3 — Escribir código ELIF ───────────────────────────
    {
        "id": 3,
        "tipo": "escritura",
        "enunciado": (
            "Escribe código que diga si una calificación es:\n"
            "- A si es 90 o más\n"
            "- B si es 80 a 89\n"
            "- C si es 70 a 79\n"
            "- F si es menor a 70\n\n"
            "Considera `calificacion = 85`"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "if calificacion >= 90:\n    print(\"A\")\nelif calificacion >= 80:\n    print(\"B\")\nelif calificacion >= 70:\n    print(\"C\")\nelse:\n    print(\"F\")",
            "if calificacion>=90:\n    print(\"A\")\nelif calificacion>=80:\n    print(\"B\")\nelif calificacion>=70:\n    print(\"C\")\nelse:\n    print(\"F\")",
        ],
        "puntaje": 1,
    },

    # ── P4 — Completar WHILE ───────────────────────────────
    {
        "id": 4,
        "tipo": "escritura",
        "enunciado": (
            "Completa el `while`:\n\n"
            "```python\n"
            "i = 1\n"
            "while i ______ 5:\n"
            "    print(i)\n"
            "    i += 1\n"
            "```\n\n"
            "Escribe el operador para imprimir 1, 2, 3, 4, 5:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "<= 5",
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
            "while i < 5: print(i); i += 1",
            "while i <= 5: print(i); i += 1",
            "while i >= 5: print(i); i += 1",
            "while True: print(i); i += 1",
        ],
        "respuesta_correcta": "while i <= 5: print(i); i += 1",
        "puntaje": 1,
    },

    # ── P6 — Escribir IF anidado ────────────────────────────
    {
        "id": 6,
        "tipo": "escritura",
        "enunciado": (
            "Escribe código que verifique si un número es positivo **y** par.\n\n"
            "Considera `numero = 6`"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "if numero > 0:\n    if numero % 2 == 0:\n        print(\"Es positivo y par\")",
            "if numero>0:\n    if numero%2==0:\n        print(\"Es positivo y par\")",
            "if numero > 0 and numero % 2 == 0:\n    print(\"Es positivo y par\")",
        ],
        "puntaje": 1,
    },

    # ── P7 — Completar AND/OR ───────────────────────────────
    {
        "id": 7,
        "tipo": "escritura",
        "enunciado": (
            "Completa:\n\n"
            "```python\n"
            "numero = 7\n"
            "if numero > 0 ______ numero < 10:\n"
            "    print(\"Está entre 1 y 9\")\n"
            "```\n\n"
            "Escribe el operador lógico:"
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
            "¿Cuál es la salida de este código?\n\n"
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

    # ── P9 — Escribir WHILE + IF ────────────────────────────
    {
        "id": 9,
        "tipo": "escritura",
        "enunciado": (
            "Escribe un `while` que incremente `i` desde 1 hasta que sea mayor a 3.\n"
            "Imprime solo si `i` es impar."
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "i = 1\nwhile i <= 3:\n    if i % 2 != 0:\n        print(i)\n    i += 1",
            "i=1\nwhile i<=3:\n    if i%2!=0:\n        print(i)\n    i+=1",
            "i = 1\nwhile i <= 3:\n    if i % 2 == 1:\n        print(i)\n    i += 1",
        ],
        "puntaje": 1,
    },

    # ── P10 — Valor final de variable en WHILE ──────────────
    {
        "id": 10,
        "tipo": "escritura",
        "enunciado": (
            "¿Cuál es el valor final de `x` después de este código?\n\n"
            "```python\n"
            "x = 0\n"
            "i = 1\n"
            "while i <= 4:\n"
            "    x = x + i\n"
            "    i += 1\n"
            "print(x)\n"
            "```\n\n"
            "Escribe solo el número:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "10",
        ],
        "puntaje": 1,
    },
]

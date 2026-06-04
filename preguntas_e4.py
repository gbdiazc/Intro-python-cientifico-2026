# ============================================================
#  BANCO DE PREGUNTAS — Examen 4 / IMP
#  Loops (FOR), BREAK, CONTINUE, Funciones y Argumentos
# ============================================================

PREGUNTAS = [

    # ── P1 — Completar FOR loop ────────────────────────────
    {
        "id": 1,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que imprime números del 1 al 5 usando `for`:\n\n"
            "```python\n"
            "______\n"
            "    print(numero)\n"
            "```\n\n"
            "Escribe la línea del `for` que falta:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "for numero in range(1, 6):",
            "for numero in range(1,6):",
            "for numero in range( 1, 6 ):",
            "for numero in range(1, 6 ):",
            "for numero in range( 1,6 ):",
        ],
        "puntaje": 1,
    },

    # ── P2 — Completar FOR con paso ────────────────────────
    {
        "id": 2,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que imprime solo números pares del 0 al 10:\n\n"
            "```python\n"
            "______\n"
            "    print(numero)\n"
            "```\n\n"
            "Escribe la línea del `for` que falta (con paso de 2):"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "for numero in range(0, 11, 2):",
            "for numero in range(0,11,2):",
            "for numero in range( 0, 11, 2 ):",
            "for numero in range(0, 11 , 2):",
            "for numero in range(0,11 , 2):",
        ],
        "puntaje": 1,
    },

    # ── P3 — Escribir función sin argumentos ───────────────
    {
        "id": 3,
        "tipo": "escritura",
        "enunciado": (
            "Escribe una función llamada `saludar` que imprima 'Hola'.\n\n"
            "No necesita argumentos ni return."
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "def saludar():\n    print(\"Hola\")",
            "def saludar( ):\n    print(\"Hola\")",
            "def saludar():\n  print(\"Hola\")",
            "def saludar():\n    print('Hola')",
            "def saludar():\n  print('Hola')",
            "def saludar( ):\n    print('Hola')",
            "def saludar( ):\n  print(\"Hola\")",
            "def saludar():\n    print( \"Hola\" )",
            "def saludar():\n    print( 'Hola' )",
        ],
        "puntaje": 1,
    },

    # ── P4 — Completar BREAK ───────────────────────────────
    {
        "id": 4,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que detiene el loop cuando encuentra un número par:\n\n"
            "```python\n"
            "for i in range(1, 10):\n"
            "    if i % 2 == 0:\n"
            "        ______\n"
            "    print(i)\n"
            "```\n\n"
            "Escribe solo la palabra clave para detener el loop:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "break",
        ],
        "puntaje": 1,
    },

    # ── P5 — Opción múltiple FOR ──────────────────────────
    {
        "id": 5,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál código imprime números del 1 al 3 usando `for`?"
        ),
        "opciones": [
            "for i in range(1, 3):\n    print(i)",
            "for i in range(1, 4):\n    print(i)",
            "for i in range(0, 3):\n    print(i)",
            "for i in range(1, 3, 1):\n    print(i)",
        ],
        "respuesta_correcta": "for i in range(1, 4):\n    print(i)",
        "puntaje": 1,
    },

    # ── P6 — Escribir función con argumentos ───────────────
    {
        "id": 6,
        "tipo": "escritura",
        "enunciado": (
            "Escribe una función llamada `duplicar` que reciba un número y imprima el doble.\n\n"
            "Por ejemplo: `duplicar(5)` imprime 10"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # Con * 2 - comillas dobles
            "def duplicar(numero):\n    print(numero * 2)",
            "def duplicar(numero):\n    print(numero*2)",
            "def duplicar(numero):\n  print(numero * 2)",
            "def duplicar( numero ):\n    print(numero * 2)",
            "def duplicar( numero ):\n  print(numero * 2)",
            
            # Con * 2 - comillas simples
            "def duplicar(numero):\n    print(numero * 2)",
            
            # Con + numero - comillas dobles
            "def duplicar(numero):\n    print(numero + numero)",
            "def duplicar(numero):\n    print(numero+numero)",
            "def duplicar(numero):\n  print(numero + numero)",
            
            # Con + numero - comillas simples
            "def duplicar(numero):\n    print(numero + numero)",
            
            # Con espacios en print
            "def duplicar(numero):\n    print( numero * 2 )",
            "def duplicar(numero):\n    print( numero + numero )",
            
            # Con espacios después de :
            "def duplicar(numero) :\n    print(numero * 2)",
            "def duplicar( numero ) :\n    print(numero * 2)",
        ],
        "puntaje": 1,
    },

    # ── P7 — Completar CONTINUE ───────────────────────────
    {
        "id": 7,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que salta (no imprime) números impares:\n\n"
            "```python\n"
            "for i in range(1, 6):\n"
            "    if i % 2 != 0:\n"
            "        ______\n"
            "    print(i)\n"
            "```\n\n"
            "Escribe solo la palabra clave para saltar la iteración:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "continue",
        ],
        "puntaje": 1,
    },

    # ── P8 — Opción múltiple función con return ────────────
    {
        "id": 8,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál es la salida de este código?\n\n"
            "```python\n"
            "def sumar(a, b):\n"
            "    return a + b\n"
            "resultado = sumar(3, 4)\n"
            "print(resultado)\n"
            "```"
        ),
        "opciones": [
            "7",
            "34",
            "3 4",
            "Error",
        ],
        "respuesta_correcta": "7",
        "puntaje": 1,
    },

    # ── P9 — Escribir CONTINUE en loop ──────────────────────
    {
        "id": 9,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que imprime solo números menores a 3:\n\n"
            "```python\n"
            "for numero in range(1, 6):\n"
            "    if numero >= 3:\n"
            "        _______\n"
            "    print(numero)\n"
            "```\n\n"
            "Escribe la palabra clave que salta la iteración:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "continue",
        ],
        "puntaje": 1,
    },

    # ── P10 — Contador en FOR ──────────────────────────────
    {
        "id": 10,
        "tipo": "escritura",
        "enunciado": (
            "¿Cuántas veces se imprime 'Hola'?\n\n"
            "```python\n"
            "for i in range(0, 5):\n"
            "    print(\"Hola\")\n"
            "```\n\n"
            "Escribe solo el número:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "5",
        ],
        "puntaje": 1,
    },
]

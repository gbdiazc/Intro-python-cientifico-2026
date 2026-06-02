# ============================================================
#  BANCO DE PREGUNTAS — Examen 2 / IMP
#  Listas, Diccionarios, Operaciones, Booleanos, Módulo, 
#  Operadores Lógicos
# ============================================================

PREGUNTAS = [

    # ── P1 — Crear lista ────────────────────────────────────
    {
        "id": 1,
        "tipo": "escritura",
        "enunciado": (
            "Crea una lista llamada `numeros` con los valores `[1, 2, 3, 4, 5]`.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "numeros = [1, 2, 3, 4, 5]",
            "numeros=[1, 2, 3, 4, 5]",
            "numeros = [1,2,3,4,5]",
            "numeros=[1,2,3,4,5]",
            "numeros = [ 1, 2, 3, 4, 5 ]",
        ],
        "puntaje": 1,
    },

    # ── P2 — Acceder a elemento de lista ────────────────────
    {
        "id": 2,
        "tipo": "escritura",
        "enunciado": (
            "Dada `lista = [10, 20, 30, 40]`, obtén el elemento en índice 2 y asígnalo a `x`.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "x = lista[2]",
            "x=lista[2]",
            "x = lista[ 2 ]",
            "x= lista[2]",
        ],
        "puntaje": 1,
    },

    # ── P3 — Agregar elemento a lista ───────────────────────
    {
        "id": 3,
        "tipo": "escritura",
        "enunciado": (
            "Dada `lista = [1, 2, 3]`, agrega el número 4 al final usando el método apropiado.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "lista.append(4)",
            "lista.append( 4 )",
            "lista . append(4)",
        ],
        "puntaje": 1,
    },

    # ── P4 — Crear diccionario ──────────────────────────────
    {
        "id": 4,
        "tipo": "escritura",
        "enunciado": (
            "Crea un diccionario llamado `persona` con claves `\"nombre\"` y `\"edad\"` "
            "con valores `\"Ana\"` y `25`.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            'persona = {"nombre": "Ana", "edad": 25}',
            'persona={"nombre": "Ana", "edad": 25}',
            'persona = {"nombre":"Ana", "edad":25}',
            'persona = {"nombre": "Ana","edad": 25}',
            "persona = {'nombre': 'Ana', 'edad': 25}",
            "persona={'nombre': 'Ana', 'edad': 25}",
        ],
        "puntaje": 1,
    },

    # ── P5 — Acceder a diccionario (opción múltiple) ────────
    {
        "id": 5,
        "tipo": "opcion_multiple",
        "enunciado": (
            "Dada `dict = {\"color\": \"azul\", \"tamaño\": \"grande\"}`.\n\n"
            "¿Cuál línea obtiene el valor de la clave `\"color\"`?"
        ),
        "opciones": [
            'valor = dict.color',
            'valor = dict["color"]',
            'valor = dict.get("color")',
            'valor = dict["tamaño"]',
        ],
        "respuesta_correcta": 'valor = dict["color"]',
        "puntaje": 1,
    },

    # ── P6 — Operador módulo (opción múltiple) ─────────────
    {
        "id": 6,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál es el resultado de `17 % 5`?"
        ),
        "opciones": [
            "2",
            "3",
            "4",
            "17",
        ],
        "respuesta_correcta": "2",
        "puntaje": 1,
    },

    # ── P7 — Operador AND (opción múltiple) ────────────────
    {
        "id": 7,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál de estas expresiones es `True`?"
        ),
        "opciones": [
            "True and False",
            "False and False",
            "True and True",
            "False and True",
        ],
        "respuesta_correcta": "True and True",
        "puntaje": 1,
    },

    # ── P8 — Operador OR (escritura) ────────────────────────
    {
        "id": 8,
        "tipo": "escritura",
        "enunciado": (
            "Escribe una expresión que devuelva `True` usando el operador `or`. "
            "Considera `a = 5` y `b = 10`.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "a > 10 or b > 5",
            "a>10 or b>5",
            "a > 10 or b > 5",
            "b > 5 or a > 10",
            "b>5 or a>10",
            "5 > 10 or 10 > 5",
            "False or True",
        ],
        "puntaje": 1,
    },

    # ── P9 — Operador NOT (opción múltiple) ────────────────
    {
        "id": 9,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál es el resultado de `not (5 > 3)`?"
        ),
        "opciones": [
            "True",
            "False",
            "5",
            "Error",
        ],
        "respuesta_correcta": "False",
        "puntaje": 1,
    },

    # ── P10 — Booleano en variable (escritura) ──────────────
    {
        "id": 10,
        "tipo": "escritura",
        "enunciado": (
            "Crea una variable `es_mayor` que sea `True` si la edad es mayor a 18. "
            "Considera `edad = 20`.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "es_mayor = edad > 18",
            "es_mayor=edad>18",
            "es_mayor = 20 > 18",
            "es_mayor=20>18",
            "es_mayor = edad>18",
            "es_mayor > 18",
            "es_mayor = True",
        ],
        "puntaje": 1,
    },
]

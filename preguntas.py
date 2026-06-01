# ============================================================
#  BANCO DE PREGUNTAS — Introducción a Python / IMP
#  Tipos:
#    "escritura"       → el alumno escribe la línea completa
#    "opcion_multiple" → elige entre 4 opciones
# ============================================================

PREGUNTAS = [

    # ── P1 ──────────────────────────────────────────────────
    {
        "id": 1,
        "tipo": "escritura",
        "enunciado": (
            "Asigna a la variable `a` el siguiente string:\n\n"
            "`\" Estamos en el Instituto Mexicano \"`\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": 'a = " Estamos en el Instituto Mexicano "',
        "respuestas_validas": [
            'a = " Estamos en el Instituto Mexicano "',
            "a = ' Estamos en el Instituto Mexicano '",
            'a=" Estamos en el Instituto Mexicano "',
            "a=' Estamos en el Instituto Mexicano '",
            'a = " Estamos en el Instituto Mexicano"',
            'a = "Estamos en el Instituto Mexicano "',
            'a = "Estamos en el Instituto Mexicano"',
        ],
        "puntaje": 1,
    },

    # ── P2 ──────────────────────────────────────────────────
    {
        "id": 2,
        "tipo": "escritura",
        "enunciado": (
            "Asigna a la variable `b` el string `\"del Petróleo\"`.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": 'b = "del Petróleo"',
        "respuestas_validas": [
            'b = "del Petróleo"',
            'b = "del petróleo"',
            'b = "del Petróleo "',
            'b = "del petróleo "',
            "b = 'del Petróleo'",
            "b = 'del petróleo'",
            'b="del Petróleo"',
            "b='del Petróleo'",
        ],
        "puntaje": 1,
    },

    # ── P3 ──────────────────────────────────────────────────
    {
        "id": 3,
        "tipo": "opcion_multiple",
        "enunciado": (
            "Tienes `a = \" Estamos en el Instituto Mexicano \"` y `b = \"del Petróleo\"`.\n\n"
            "¿Cuál línea **concatena correctamente** ambas variables en `c`?"
        ),
        "opciones": [
            "c = a - b",
            "c = a + b",
            "c = a * b",
            "c = a.join(b)",
        ],
        "respuesta_correcta": "c = a + b",
        "puntaje": 1,
    },

    # ── P4 ──────────────────────────────────────────────────
    {
        "id": 4,
        "tipo": "opcion_multiple",
        "enunciado": (
            "Tienes `c = \" Estamos en el Instituto Mexicano del Petróleo\"`.\n\n"
            "¿Cuál línea convierte `c` en una **lista de palabras**?"
        ),
        "opciones": [
            "lista = list(c)",
            "lista = c.split(',')",
            "lista = c.split()",
            "lista = c.strip()",
        ],
        "respuesta_correcta": "lista = c.split()",
        "puntaje": 1,
    },

    # ── P5 ──────────────────────────────────────────────────
    {
        "id": 5,
        "tipo": "opcion_multiple",
        "enunciado": (
            "Tienes:\n"
            "```python\n"
            "lista = ['Estamos', 'en', 'el', 'Instituto', 'Mexicano', 'del', 'petróleo']\n"
            "```\n"
            "¿Cuál línea extrae correctamente `\"Instituto Mexicano del petróleo\"` y lo asigna a `e`?"
        ),
        "opciones": [
            'e = lista[3] + " " + lista[4] + " " + lista[5] + " " + lista[6]',
            'e = lista[4] + " " + lista[5] + " " + lista[6] + " " + lista[7]',
            'e = lista[2] + " " + lista[3] + " " + lista[4] + " " + lista[5]',
            'e = lista[3:7]',
        ],
        "respuesta_correcta": 'e = lista[3] + " " + lista[4] + " " + lista[5] + " " + lista[6]',
        "puntaje": 1,
    },

    # ── P6 ──────────────────────────────────────────────────
    {
        "id": 6,
        "tipo": "escritura",
        "enunciado": (
            'Convierte el string `"3.14"` a número **flotante** y asígnalo a la variable `pi`.\n\n'
            "Escribe la línea completa de código:"
        ),
        "placeholder": 'pi = float("3.14")',
        "respuestas_validas": [
            'pi = float("3.14")',
            "pi = float('3.14')",
            'pi=float("3.14")',
            "pi=float('3.14')",
        ],
        "puntaje": 1,
    },

    # ── P7 ──────────────────────────────────────────────────
    {
        "id": 7,
        "tipo": "escritura",
        "enunciado": (
            'Convierte el string `"42"` a número **entero** y asígnalo a la variable `n`.\n\n'
            "Escribe la línea completa de código:"
        ),
        "placeholder": 'n = int("42")',
        "respuestas_validas": [
            'n = int("42")',
            "n = int('42')",
            'n=int("42")',
            "n=int('42')",
        ],
        "puntaje": 1,
    },

    # ── P8 ──────────────────────────────────────────────────
    {
        "id": 8,
        "tipo": "escritura",
        "enunciado": (
            "Dada `palabra = \"Python\"`, conviértela a **mayúsculas** y asígnala a `mayus`.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": "mayus = palabra.upper()",
        "respuestas_validas": [
            "mayus = palabra.upper()",
            "mayus=palabra.upper()",
            "mayus = palabra.upper(  )",
            "mayus= palabra.upper()",
        ],
        "puntaje": 1,
    },

    # ── P9 ──────────────────────────────────────────────────
    {
        "id": 9,
        "tipo": "escritura",
        "enunciado": (
            "Dada `palabra = \"Python\"`, conviértela a **minúsculas** y asígnala a `minus`.\n\n"
            "Escribe la línea completa de código:"
        ),
        "placeholder": "minus = palabra.lower()",
        "respuestas_validas": [
            "minus = palabra.lower()",
            "minus=palabra.lower()",
            "minus = palabra.lower(  )",
            "minus= palabra.lower()",
        ],
        "puntaje": 1,
    },

    # ── P10 ──────────────────────────────────────────────────
    {
        "id": 10,
        "tipo": "escritura",
        "enunciado": (
            'Convierte el string `"27.5"` a número **flotante** y asígnalo a `resultado`.\n\n'
            "Escribe la línea completa de código:"
        ),
        "placeholder": 'resultado = float("27.5")',
        "respuestas_validas": [
            'resultado = float("27.5")',
            "resultado = float('27.5')",
            'resultado=float("27.5")',
            "resultado=float('27.5')",
        ],
        "puntaje": 1,
    },
]

# ============================================================
#  BANCO DE PREGUNTAS — Introducción a Python / IMP
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
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # comillas dobles, con espacios al inicio/fin
            'a = " Estamos en el Instituto Mexicano "',
            'a=" Estamos en el Instituto Mexicano "',
            # comillas simples
            "a = ' Estamos en el Instituto Mexicano '",
            "a=' Estamos en el Instituto Mexicano '",
            # sin espacio inicial o final (tolerancia)
            'a = "Estamos en el Instituto Mexicano"',
            'a = "Estamos en el Instituto Mexicano "',
            'a = " Estamos en el Instituto Mexicano"',
            # con print al final (algunos lo agregan)
            'a = " Estamos en el Instituto Mexicano "; print(a)',
            'a = " Estamos en el Instituto Mexicano "\nprint(a)',
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
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # comillas dobles
            'b = "del Petróleo"',
            'b="del Petróleo"',
            # minúscula (tolerancia)
            'b = "del petróleo"',
            'b = "del petróleo "',
            'b = "del Petróleo "',
            # sin acento (tolerancia)
            'b = "del Petroleo"',
            'b = "del petroleo"',
            # comillas simples
            "b = 'del Petróleo'",
            "b = 'del petróleo'",
            "b='del Petróleo'",
            "b='del petróleo'",
        ],
        "puntaje": 1,
    },

    # ── P3 — opción múltiple ─────────────────────────────────
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

    # ── P4 — opción múltiple ─────────────────────────────────
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

    # ── P5 — opción múltiple ─────────────────────────────────
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
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # comillas dobles
            'pi = float("3.14")',
            'pi=float("3.14")',
            # comillas simples
            "pi = float('3.14')",
            "pi=float('3.14')",
            # sin comillas (el número ya es float, también válido)
            "pi = float(3.14)",
            "pi=float(3.14)",
            # solo la función (sin asignación)
            'float("3.14")',
            "float('3.14')",
            "float(3.14)",
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
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # comillas dobles
            'n = int("42")',
            'n=int("42")',
            # comillas simples
            "n = int('42')",
            "n=int('42')",
            # sin comillas (también válido)
            "n = int(42)",
            "n=int(42)",
            # solo la función
            'int("42")',
            "int('42')",
            "int(42)",
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
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # con asignación a mayus
            "mayus = palabra.upper()",
            "mayus=palabra.upper()",
            # solo el método
            "palabra.upper()",
            # con la cadena directa
            '"Python".upper()',
            "mayus = \"Python\".upper()",
            # con print
            "print(palabra.upper())",
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
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # con asignación a minus
            "minus = palabra.lower()",
            "minus=palabra.lower()",
            # solo el método
            "palabra.lower()",
            # con la cadena directa
            '"Python".lower()',
            "minus = \"Python\".lower()",
            # con print
            "print(palabra.lower())",
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
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # comillas dobles
            'resultado = float("27.5")',
            'resultado=float("27.5")',
            # comillas simples
            "resultado = float('27.5')",
            "resultado=float('27.5')",
            # sin comillas
            "resultado = float(27.5)",
            "resultado=float(27.5)",
            # solo la función
            'float("27.5")',
            "float('27.5')",
            "float(27.5)",
        ],
        "puntaje": 1,
    },
]

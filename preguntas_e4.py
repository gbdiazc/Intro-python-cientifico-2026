# ============================================================
#  BANCO DE PREGUNTAS — Examen 4 / IMP
#  Loops (FOR), BREAK, CONTINUE, Funciones y Argumentos
# ============================================================

PREGUNTAS = [

    # ── P1 — Completar FOR loop ────────────────────────────
    # ✅ Variable fijada en "numero" por el body ya mostrado
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
            "for numero in range( 1,6):",
            "for numero in range( 1,6 ):",
            "for numero in range(1, 6) :",
            "for numero in range(1,6) :",
            "for numero in range( 1, 6 ) :",
            "for numero in range (1,6):",
        ],
        "puntaje": 1,
    },

    # ── P2 — Completar FOR con paso ────────────────────────
    {
        "id": 2,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que imprime solo números pares del 0 al 10 (con paso de 2):\n\n"
            "```python\n"
            "______\n"
            "    print(numero)\n"
            "```\n\n"
            "Escribe la línea del `for` que falta:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "for numero in range(0, 11, 2):",
            "for numero in range(0,11,2):",
            "for numero in range( 0, 11, 2 ):",
            "for numero in range(0, 11 , 2):",
            "for numero in range(0,11 , 2):",
            "for numero in range( 0,11,2 ):",
            "for numero in range( 0, 11, 2):",
            "for numero in range(0, 11, 2) :",
            "for numero in range(0,11,2) :",
        ],
        "puntaje": 1,
    },

    # ── P3 — Escribir función sin argumentos ───────────────
    {
        "id": 3,
        "tipo": "escritura",
        "enunciado": (
            "Escribe una función llamada `saludar` que imprima `'Hola'`.\n\n"
            "No necesita argumentos ni `return`."
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # 4 espacios, comilla doble
            "def saludar():\n    print(\"Hola\")",
            "def saludar( ):\n    print(\"Hola\")",
            "def saludar() :\n    print(\"Hola\")",
            "def saludar():\n    print( \"Hola\" )",
            "def saludar( ):\n    print( \"Hola\" )",
            # 4 espacios, comilla simple
            "def saludar():\n    print('Hola')",
            "def saludar( ):\n    print('Hola')",
            "def saludar() :\n    print('Hola')",
            "def saludar():\n    print( 'Hola' )",
            "def saludar( ):\n    print( 'Hola' )",
            # 2 espacios, comilla doble
            "def saludar():\n  print(\"Hola\")",
            "def saludar( ):\n  print(\"Hola\")",
            "def saludar() :\n  print(\"Hola\")",
            "def saludar():\n  print( \"Hola\" )",
            # 2 espacios, comilla simple
            "def saludar():\n  print('Hola')",
            "def saludar( ):\n  print('Hola')",
            "def saludar() :\n  print('Hola')",
            "def saludar():\n  print( 'Hola' )",
            # tab, comilla doble
            "def saludar():\n\tprint(\"Hola\")",
            "def saludar( ):\n\tprint(\"Hola\")",
            "def saludar() :\n\tprint(\"Hola\")",
            # tab, comilla simple
            "def saludar():\n\tprint('Hola')",
            "def saludar( ):\n\tprint('Hola')",
            "def saludar() :\n\tprint('Hola')",
        ],
        "puntaje": 1,
    },

    # ── P4 — Completar BREAK ───────────────────────────────
    # ✅ Solo "break" es correcto — no hay variantes sintácticas
    {
        "id": 4,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que **detiene completamente el loop** cuando encuentra un número par:\n\n"
            "```python\n"
            "for i in range(1, 10):\n"
            "    if i % 2 == 0:\n"
            "        ______\n"
            "    print(i)\n"
            "```\n\n"
            "Resultado esperado: imprime 1, luego se detiene (porque 2 es par).\n\n"
            "Escribe la palabra clave:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "break",
        ],
        "puntaje": 1,
    },

    # ── P5 — Opción múltiple FOR ──────────────────────────
    # ✅ Verificado: b imprime 1,2,3 — a y d imprimen 1,2 — c imprime 0,1,2
    {
        "id": 5,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál código imprime números del 1 al 3 usando `for`?"
        ),
        "opciones": {
            "a": "for i in range(1, 3):\n    print(i)",
            "b": "for i in range(1, 4):\n    print(i)",
            "c": "for i in range(0, 3):\n    print(i)",
            "d": "for i in range(1, 3, 1):\n    print(i)",
        },
        "respuesta_correcta": "b",
        "puntaje": 1,
    },

    # ── P6 — Escribir función con argumentos ───────────────
    # ✅ La pregunta especifica "variable x" — se acepta solo x como parámetro
    {
        "id": 6,
        "tipo": "escritura",
        "enunciado": (
            "Escribe una función llamada `duplicar` que reciba una variable `x` e imprima el doble.\n\n"
            "Por ejemplo: `duplicar(5)` imprime `10`"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            # ── x * 2 — 4 espacios ──
            "def duplicar(x):\n    print(x * 2)",
            "def duplicar(x):\n    print(x*2)",
            "def duplicar( x ):\n    print(x * 2)",
            "def duplicar( x ):\n    print(x*2)",
            "def duplicar(x) :\n    print(x * 2)",
            "def duplicar( x ) :\n    print(x * 2)",
            "def duplicar(x):\n    print( x * 2 )",
            "def duplicar( x ):\n    print( x * 2 )",
            # ── x * 2 — 2 espacios ──
            "def duplicar(x):\n  print(x * 2)",
            "def duplicar(x):\n  print(x*2)",
            "def duplicar( x ):\n  print(x * 2)",
            "def duplicar(x) :\n  print(x * 2)",
            # ── x * 2 — tab ──
            "def duplicar(x):\n\tprint(x * 2)",
            "def duplicar(x):\n\tprint(x*2)",
            "def duplicar( x ):\n\tprint(x * 2)",
            "def duplicar(x) :\n\tprint(x * 2)",
            # ── 2 * x — 4 espacios ──
            "def duplicar(x):\n    print(2 * x)",
            "def duplicar(x):\n    print(2*x)",
            "def duplicar( x ):\n    print(2 * x)",
            "def duplicar( x ):\n    print(2*x)",
            "def duplicar(x) :\n    print(2 * x)",
            "def duplicar(x):\n    print( 2 * x )",
            "def duplicar( x ):\n    print( 2 * x )",
            # ── 2 * x — 2 espacios ──
            "def duplicar(x):\n  print(2 * x)",
            "def duplicar(x):\n  print(2*x)",
            "def duplicar( x ):\n  print(2 * x)",
            "def duplicar( x ):\n  print(2*x)",
            "def duplicar(x) :\n  print(2 * x)",
            # ── 2 * x — tab ──
            "def duplicar(x):\n\tprint(2 * x)",
            "def duplicar(x):\n\tprint(2*x)",
            "def duplicar( x ):\n\tprint(2 * x)",
            "def duplicar(x) :\n\tprint(2 * x)",
            # ── x + x — 4 espacios ──
            "def duplicar(x):\n    print(x + x)",
            "def duplicar(x):\n    print(x+x)",
            "def duplicar( x ):\n    print(x + x)",
            "def duplicar(x):\n    print( x + x )",
            "def duplicar(x) :\n    print(x + x)",
            # ── x + x — 2 espacios ──
            "def duplicar(x):\n  print(x + x)",
            "def duplicar(x):\n  print(x+x)",
            "def duplicar( x ):\n  print(x + x)",
            # ── x + x — tab ──
            "def duplicar(x):\n\tprint(x + x)",
            "def duplicar(x):\n\tprint(x+x)",
            "def duplicar( x ):\n\tprint(x + x)",
            # ── f-string x * 2 ──
            "def duplicar(x):\n    print(f\"{x * 2}\")",
            "def duplicar(x):\n    print(f\"{x*2}\")",
            "def duplicar(x):\n    print(f'{x * 2}')",
            "def duplicar(x):\n    print(f'{x*2}')",
            "def duplicar(x):\n  print(f\"{x * 2}\")",
            "def duplicar(x):\n  print(f\"{x*2}\")",
            "def duplicar(x):\n\tprint(f\"{x * 2}\")",
            "def duplicar(x):\n\tprint(f\"{x*2}\")",
            # ── f-string 2 * x ──
            "def duplicar(x):\n    print(f\"{2 * x}\")",
            "def duplicar(x):\n    print(f\"{2*x}\")",
            "def duplicar(x):\n    print(f'{2 * x}')",
            "def duplicar(x):\n    print(f'{2*x}')",
            "def duplicar(x):\n  print(f\"{2 * x}\")",
            "def duplicar(x):\n  print(f\"{2*x}\")",
            "def duplicar(x):\n\tprint(f\"{2 * x}\")",
            "def duplicar(x):\n\tprint(f\"{2*x}\")",
            # ── f-string x + x ──
            "def duplicar(x):\n    print(f\"{x + x}\")",
            "def duplicar(x):\n    print(f\"{x+x}\")",
            "def duplicar(x):\n    print(f'{x + x}')",
            "def duplicar(x):\n  print(f\"{x + x}\")",
            "def duplicar(x):\n\tprint(f\"{x + x}\")",
            # ── str(x * 2) ──
            "def duplicar(x):\n    print(str(x * 2))",
            "def duplicar(x):\n    print(str(x*2))",
            "def duplicar(x):\n  print(str(x * 2))",
            "def duplicar(x):\n  print(str(x*2))",
            "def duplicar(x):\n\tprint(str(x * 2))",
            "def duplicar(x):\n\tprint(str(x*2))",
            # ── str(2 * x) ──
            "def duplicar(x):\n    print(str(2 * x))",
            "def duplicar(x):\n    print(str(2*x))",
            "def duplicar(x):\n  print(str(2 * x))",
            "def duplicar(x):\n\tprint(str(2 * x))",
            # ── str(x + x) ──
            "def duplicar(x):\n    print(str(x + x))",
            "def duplicar(x):\n    print(str(x+x))",
            "def duplicar(x):\n  print(str(x + x))",
            "def duplicar(x):\n\tprint(str(x + x))",
            # ── str(x + x) ──
            "def duplicar(x):\r\n duplicar = x * 2\r\n return duplicar",
        ],
        "puntaje": 1,
    },

    # ── P7 — Completar CONTINUE ────────────────────────────
    # ✅ Solo "continue" — no hay variantes
    {
        "id": 7,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que **salta la iteración** cuando el número es par (no lo imprime):\n\n"
            "```python\n"
            "for i in range(1, 6):\n"
            "    if i % 2 == 0:\n"
            "        ______\n"
            "    print(i)\n"
            "```\n\n"
            "Resultado esperado: imprime 1, 3, 5 (salta los pares).\n\n"
            "Escribe la palabra clave (NO es break):"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "continue",
        ],
        "puntaje": 1,
    },

    # ── P8 — Opción múltiple función con return ────────────
    # ✅ Verificado: b es la única que retorna el doble correctamente
    # a) imprime pero no retorna; c) n no está definida; d) no hace nada
    {
        "id": 8,
        "tipo": "opcion_multiple",
        "enunciado": (
            "¿Cuál función recibe un número y **retorna** el doble?"
        ),
        "opciones": {
            "a": "def doble(n):\n    print(n * 2)",
            "b": "def doble(n):\n    return n * 2",
            "c": "def doble():\n    return n * 2",
            "d": "def doble(n):\n    n * 2",
        },
        "respuesta_correcta": "b",
        "puntaje": 1,
    },

    # ── P9 — Completar CONTINUE en loop ──────────────────────
    # ✅ Solo "continue" — no hay variantes
    {
        "id": 9,
        "tipo": "escritura",
        "enunciado": (
            "Completa el código que **salta a la siguiente iteración** cuando número >= 3:\n\n"
            "```python\n"
            "for numero in range(1, 6):\n"
            "    if numero >= 3:\n"
            "        _______\n"
            "    print(numero)\n"
            "```\n\n"
            "Resultado esperado: imprime 1, 2 (luego salta 3, 4, 5).\n\n"
            "Escribe la palabra clave (NO es break):"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "continue",
        ],
        "puntaje": 1,
    },

    # ── P10 — Contador en FOR ──────────────────────────────
    # ✅ range(0,5) → 5 iteraciones confirmado
    {
        "id": 10,
        "tipo": "escritura",
        "enunciado": (
            "¿Cuántas veces se imprime `'Hola'`?\n\n"
            "```python\n"
            "for i in range(0, 5):\n"
            "    print('Hola')\n"
            "```\n\n"
            "Escribe solo el número:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "5",
            " 5",
            "5 ",
            "5.",
        ],
        "puntaje": 1,
    },
]

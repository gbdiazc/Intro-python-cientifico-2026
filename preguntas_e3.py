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
            "Completa el código que clasifica por edad. Clasifica mayores de 18 (inclusivo), mayores de 13 (inclusivo) y menores de 13.\n Escribe las dos líneas que faltan:\n\n"
            "```python\n"
            "edad = 15\n"
            "______\n"
            "    print(\"Adulto\")\n"
            "______ \n"
            "    print(\"Adolescente\")\n"
            "else:\n"
            "    print(\"Niño\")\n"
            "```\n\n"
            "```"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
    "if edad >= 18:\nelif edad >= 13:",
    "if edad>=18:\nelif edad>=13:",
    "if edad >= 18 :\nelif edad >= 13 :",
    "if edad>=18:\nelif edad >= 13:",
    "if edad >= 18:\nelif edad>=13:",
    "if edad>=18:\nelif edad >= 13 :",
    "if edad>=18 :\nelif edad>=13 :",
    "if edad  >=  18:\nelif edad  >=  13:",
],
        "puntaje": 1,
    },

    # ── P2 — Completar IF para verificar divisibilidad ──────
    {
        "id": 2,
        "tipo": "escritura",
        "enunciado": (
            "Completa la línea del `if` para verificar si un número es divisible entre 4:\n\n"
            "```python\n"
            "num = int(input(\"Ingrese un número: \"))\n"
            "______\n"
            "    print(num, \" es divisible entre 4\")\n"
            "else:\n"
            "    print(num, \" no es divisible entre 4\")\n"
            "```\n\n"
            "Escribe la línea del `if` que falta:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "if num % 4 == 0:",
            "if num%4==0:",
            "if num % 4 == 0 :",
        ],
        "puntaje": 1,
    },

    # ── P3 — Escribir WHILE con incremento ──────────────────
    {
        "id": 3,
        "tipo": "escritura",
        "enunciado": (
            "Escribe un `while` que imprima temperaturas desde 15 hasta 19 (inclusive).\n\n"
            "En cada iteración:\n"
            "- Imprime la temperatura actual\n"
            "- Incrementa la temperatura en 1\n\n"
            "Considera `temperatura = 15` como definida previamente, no la tienes que volver a definir"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "temperatura = 15\nwhile temperatura < 20:\n    print(temperatura)\n    temperatura += 1",
            "temperatura = 15\nwhile temperatura < 20:\n    print(temperatura)\n    temperatura = temperatura + 1",
            "temperatura=15\nwhile temperatura<20:\n    print(temperatura)\n    temperatura+=1",
            "while temperatura < 20:\n    print(temperatura)\n    temperatura += 1",
            "while temperatura < 20:\n    print(temperatura)\n    temperatura = temperatura + 1",
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
            "Escribe el operador completo:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            " < = ",
            "<= ",
            "< =",
            "< = ",
	    " <= ",
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
            "i = 1\nwhile True:\n    print(i)\n    i += 1",
        ],
        "respuesta_correcta": "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1",
        "puntaje": 1,
    },

    # ── P6 — Escribir IF anidado con acción clara ──────────
    {
        "id": 6,
        "tipo": "escritura",
        "enunciado": (
            "Escribe un código que imprima 'válido' solo si el número es positivo y par.\n"
            "Si no cumple ambas condiciones que no imprime nada.\n\n"
            "Considera el `numero = 6` dado, no tienes que definirlo"
        ),
        "placeholder": "Tu respuesta aquí...",
"respuestas_validas": [
    # IF anidado - comillas dobles
    "if numero > 0:\n    if numero % 2 == 0:\n        print(\"válido\")",
    "if numero>0:\n    if numero%2==0:\n        print(\"válido\")",
    "if numero > 0 :\n    if numero % 2 == 0 :\n        print(\"válido\")",
    "if numero > 0:\n  if numero % 2 == 0:\n    print(\"válido\")",
    
    # IF anidado - comillas simples
    "if numero > 0:\n    if numero % 2 == 0:\n        print('válido')",
    "if numero>0:\n    if numero%2==0:\n        print('válido')",
    "if numero > 0:\n  if numero % 2 == 0:\n    print('válido')",
    
    # IF anidado - Orden invertido (comillas dobles)
    "if numero % 2 == 0:\n    if numero > 0:\n        print(\"válido\")",
    "if numero%2==0:\n    if numero>0:\n        print(\"válido\")",
    
    # IF anidado - Orden invertido (comillas simples)
    "if numero % 2 == 0:\n    if numero > 0:\n        print('válido')",
    "if numero%2==0:\n    if numero>0:\n        print('válido')",
    
    # IF con AND - comillas dobles
    "if numero > 0 and numero % 2 == 0:\n    print(\"válido\")",
    "if numero>0 and numero%2==0:\n    print(\"válido\")",
    "if numero > 0 and numero % 2 == 0 :\n    print(\"válido\")",
    
    # IF con AND - comillas simples
    "if numero > 0 and numero % 2 == 0:\n    print('válido')",
    "if numero>0 and numero%2==0:\n    print('válido')",
    
    # IF con AND - Orden invertido (comillas dobles)
    "if numero % 2 == 0 and numero > 0:\n    print(\"válido\")",
    "if numero%2==0 and numero>0:\n    print(\"válido\")",
    
    # IF con AND - Orden invertido (comillas simples)
    "if numero % 2 == 0 and numero > 0:\n    print('válido')",
    "if numero%2==0 and numero>0:\n    print('válido')",
    
    # Con != 1 (comillas dobles)
    "if numero > 0 and numero % 2 != 1:\n    print(\"válido\")",
    "if numero % 2 != 1 and numero > 0:\n    print(\"válido\")",
    
    # Con != 1 (comillas simples)
    "if numero > 0 and numero % 2 != 1:\n    print('válido')",
    "if numero % 2 != 1 and numero > 0:\n    print('válido')",
    
    # Con >= 1 (comillas dobles)
    "if numero >= 1 and numero % 2 == 0:\n    print(\"válido\")",
    "if numero % 2 == 0 and numero >= 1:\n    print(\"válido\")",
    
    # Con >= 1 (comillas simples)
    "if numero >= 1 and numero % 2 == 0:\n    print('válido')",
    "if numero % 2 == 0 and numero >= 1:\n    print('válido')",
    
    # Con paréntesis (comillas dobles)
    "if (numero > 0) and (numero % 2 == 0):\n    print(\"válido\")",
    "if numero > 0 and (numero % 2 == 0):\n    print(\"válido\")",
    
    # Con paréntesis (comillas simples)
    "if (numero > 0) and (numero % 2 == 0):\n    print('válido')",
    "if numero > 0 and (numero % 2 == 0):\n    print('válido')",
    
    # Espacios en print (comillas dobles)
    "if numero > 0:\n    if numero % 2 == 0:\n        print( \"válido\" )",
    "if numero > 0 and numero % 2 == 0:\n    print( \"válido\" )",
    
    # Espacios en print (comillas simples)
    "if numero > 0:\n    if numero % 2 == 0:\n        print( 'válido' )",
    "if numero > 0 and numero % 2 == 0:\n    print( 'válido' )",
],
        "puntaje": 1,
    },

    # ── P7 — Completar AND ───────────────────────────────────
{
    "id": 7,
    "tipo": "escritura",
    "enunciado": (
        "Completa el operador lógico para que imprima solo si el número está fuera del rango de 1 a 9, en donde\n\n"
        "```python\n"
        "numero = 15\n"
        "if numero < 1 ______ numero > 9:\n"
        "    print(\"Fuera de rango\")\n"
        "```\n\n"
        "Escribe solo el operador:"
    ),
    "placeholder": "Tu respuesta aquí...",
    "respuestas_validas": [
        "or",
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

    # ── P9 — Escribir bloque IF dentro de WHILE ────────────
    {
        "id": 9,
        "tipo": "escritura",
        "enunciado": (
            "Escribe el bloque `if` y `print` que falta para que imprima solo números impares:\n\n"
            "```python\n"
            "i = 0\n"
            "while i <= 3:\n"
            "    _______\n"
	    "    _______\n"
            "    i += 1\n"
            "```\n\n"
            "Escribe las 2 líneas que van en el espacio en blanco:"
        ),
        "placeholder": "Tu respuesta aquí...",
        "respuestas_validas": [
            "if i % 2 != 0:\n        print(i)",
            "if i%2!=0:\n        print(i)",
            "if i % 2 == 1:\n        print(i)",
            "if i%2==1:\n        print(i)",
            "if i % 2 != 0:\n    print(i)",
            "if i%2!=0:\n    print(i)",
            "if i % 2 == 1:\n    print(i)",
            "if i%2==1:\n    print(i)",
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
            " \n"
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

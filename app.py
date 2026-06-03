import streamlit as st
import random
import time
import csv
import os
import base64
import json
import requests
from datetime import datetime

# ── Cargar examen dinámicamente ──────────────────────────────────────────────
def cargar_examen(numero_examen):
    """Carga las preguntas y configuración del examen."""
    if numero_examen == 1:
        from preguntas_e1 import PREGUNTAS as PREG_E1
        return {
            "numero": 1,
            "titulo": "Introducción a la programación en Python",
            "preguntas": PREG_E1,
            "csv": "calificaciones_e1.csv",
        }
    elif numero_examen == 2:
        from preguntas_e2 import PREGUNTAS as PREG_E2
        return {
            "numero": 2,
            "titulo": "Listas, Diccionarios, Operaciones, Booleanos y Operadores Lógicos",
            "preguntas": PREG_E2,
            "csv": "calificaciones_e2.csv",
        }
    elif numero_examen == 3:
        from preguntas_e3 import PREGUNTAS as PREG_E3
        return {
            "numero": 3,
            "titulo": "Control de Flujo: IF, ELIF, ELSE, WHILE, FOR",
            "preguntas": PREG_E3,
            "csv": "calificaciones_e3.csv",
        }
    else:
        return None

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Examen — Python IMP",
    page_icon="🧪",
    layout="centered",
)

TIEMPO_LIMITE = 10 * 60   # segundos
NUM_PREGUNTAS = 5
PUNTOS_POR_PREGUNTA = 2   # 5 × 2 = 10

# ── CONFIGURACIÓN: Elige qué examen mostrar ─────────────────────────────────
# Opciones:
#   None        → Los alumnos eligen (pantalla de selección)
#   1           → Solo Examen 1 (directo a login)
#   2           → Solo Examen 2 (directo a login)
EXAMEN_FIJO = None  # Cambia aquí: None, 1 o 2

# ── CSS global — tema claro ───────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"], .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #f5f7fa !important;
    color: #1a1a2e !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; max-width: 820px !important; }

.timer-box {
    background: #ffffff;
    border: 2px solid #2e8b57;
    border-radius: 10px;
    padding: 10px 20px;
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.7rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.timer-ok  { color: #2e8b57; border-color: #2e8b57; }
.timer-mid { color: #d4830a; border-color: #d4830a; }
.timer-low { color: #c0392b; border-color: #c0392b; animation: pulse 1s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.55} }

.pregunta-card {
    background: #ffffff;
    border: 1px solid #dde3ea;
    border-radius: 10px;
    padding: 22px 26px;
    margin-bottom: 18px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
.pregunta-num {
    display: inline-block;
    background: #2e8b57;
    color: #fff;
    font-weight: 700;
    font-size: 0.72rem;
    padding: 3px 12px;
    border-radius: 20px;
    margin-bottom: 12px;
    letter-spacing: 0.06em;
}

.stTextInput > div > div > input {
    background: #f8f9fb !important;
    border: 1.5px solid #c8d0da !important;
    color: #1a1a2e !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.88rem !important;
    border-radius: 7px !important;
    padding: 8px 12px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #2e8b57 !important;
    box-shadow: 0 0 0 3px rgba(46,139,87,0.12) !important;
}
.stTextInput > div > div > input::placeholder {
    color: #aab0ba !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.stRadio > div { gap: 7px !important; }
.stRadio > div > label {
    background: #f8f9fb !important;
    border: 1.5px solid #dde3ea !important;
    border-radius: 8px !important;
    padding: 9px 16px !important;
    font-size: 0.83rem !important;
    font-family: 'JetBrains Mono', monospace !important;
    color: #1a1a2e !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
}
.stRadio > div > label:hover {
    border-color: #2e8b57 !important;
    background: #f0f9f4 !important;
}
.stRadio > div > label > div {
    color: #1a1a2e !important;
}
.stRadio > div > label p {
    color: #1a1a2e !important;
    margin: 0 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #27ae60, #2e8b57) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    padding: 11px 28px !important;
    letter-spacing: 0.03em !important;
    box-shadow: 0 2px 8px rgba(46,139,87,0.25) !important;
}
.stButton > button:hover { opacity: 0.88 !important; }

.login-box {
    background: #ffffff;
    border: 1px solid #dde3ea;
    border-radius: 12px;
    padding: 30px 36px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    margin-top: 8px;
}

.resultado-box {
    background: #ffffff;
    border: 1px solid #dde3ea;
    border-radius: 12px;
    padding: 36px;
    text-align: center;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    margin-top: 16px;
}
.cal-numero   { font-size: 4.5rem; font-weight: 700; line-height: 1; font-family: 'JetBrains Mono', monospace; }
.cal-verde    { color: #2e8b57; }
.cal-amarillo { color: #d4830a; }
.cal-rojo     { color: #c0392b; }
.detalle-item { font-size: 0.82rem; color: #555; margin: 5px 0; padding: 6px 12px; background:#f8f9fb; border-radius:6px; }
.detalle-ok   { color: #2e8b57; font-weight: 600; }
.detalle-mal  { color: #c0392b; font-weight: 600; }

code {
    background: #eef2f7 !important;
    color: #c0392b !important;
    border-radius: 4px !important;
    padding: 1px 5px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.87em !important;
}
pre {
    background: #f4f6f9 !important;
    border: 1px solid #dde3ea !important;
    border-radius: 7px !important;
}
hr { border-color: #e8ecf0 !important; margin: 20px 0 !important; }

.alumno-info {
    background: #f0f9f4;
    border-left: 4px solid #2e8b57;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 0.85rem;
    color: #2c5f3f;
    margin-bottom: 18px;
}
</style>
""", unsafe_allow_html=True)


# ── Helpers ──────────────────────────────────────────────────────────────────

def fecha_en_espanol(dt):
    """Convierte datetime a formato: 'X de [mes] de YYYY' en español."""
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    return f"{dt.day} de {meses[dt.month]} de {dt.year}"

def render_header():
    numero_examen = st.session_state.get("numero_examen", 1)
    fecha_hoy = fecha_en_espanol(datetime.now())
    
    st.markdown(f"""
    <div style="background-color:#f2f2f2; border-left: 8px solid #2e8b57; padding: 20px; border-radius: 10px; font-family: Arial, sans-serif; margin-bottom: 24px;">
      <center>
        <h1 style="color:#2e8b57;">Introducción a la programación en Python</h1>
        <h2 style="color:#2e8b57;">Instituto Mexicano del Petróleo</h2>
        <h3 style="color:#2e8b57;">Examen {numero_examen}  ·  {fecha_hoy}</h3>
        <p style="font-size:16px; color:#333;">
          <strong>Dra. Gabriela Berenice Díaz Cortés</strong><br>
          <em>gbdiaz@imp.mx</em>
        </p>
        <p style="font-size:16px; color:#333;">
          <strong>Dr. Luis Antonio López Peña</strong><br>
          <em>llopezp@imp.mx</em>
        </p>
        <p style="font-size:15px; color:#555;">
          Dirección de Investigación<br>
          Gerencia de Investigación en Explotación
        </p>
      </center>
    </div>
    """, unsafe_allow_html=True)


def tiempo_str(seg):
    m, s = divmod(int(seg), 60)
    return f"{m:02d}:{s:02d}"


def color_timer(seg):
    if seg > 120:
        return "timer-ok"
    elif seg > 60:
        return "timer-mid"
    return "timer-low"


def normalizar_codigo(codigo):
    """Normaliza código: quita espacios, estandariza comparación flexible."""
    # Quitar saltos de línea al inicio/fin, dividir en líneas
    lineas = [linea.strip() for linea in codigo.strip().split('\n')]
    # Quitar líneas vacías
    lineas = [l for l in lineas if l]
    # Unir líneas, convertir a minúsculas, quitar todos los espacios
    texto = '\n'.join(lineas).lower().replace(' ', '')
    return texto

def normalizar(texto):
    """Quita espacios extra internos y convierte a minúsculas para comparar."""
    return " ".join(texto.lower().split())

def calificar(preguntas, respuestas):
    detalle = []
    for p in preguntas:
        pid  = p["id"]
        raw  = respuestas.get(pid, None)
        resp = (raw or "").strip()
        if p["tipo"] == "escritura":
            # Detectar si es código multilineal (contiene \n o es muy largo)
            es_multilineal = '\n' in resp or len(resp) > 100
            if es_multilineal:
                # Usar normalización de código
                resp_norm = normalizar_codigo(resp)
                correcto = any(normalizar_codigo(v) == resp_norm for v in p["respuestas_validas"])
            else:
                # Usar normalización simple (sin mayúsculas)
                resp_norm = normalizar(resp)
                correcto = any(resp_norm == normalizar(v) for v in p["respuestas_validas"])
            correcta  = p["respuestas_validas"][0]
        else:
            correcto = (resp == p["respuesta_correcta"]) if resp else False
            correcta = p["respuesta_correcta"]
        detalle.append({
            "id":                pid,
            "enunciado":         p["enunciado"],
            "respuesta_alumno":  resp,
            "respuesta_correcta": correcta,
            "correcto":          correcto,
        })
    return detalle


# ── GitHub: guardar CSV ───────────────────────────────────────────────────────

def guardar_en_github(nombre, calificacion, correctas, detalle, csv_nombre="calificaciones.csv"):
    """
    Guarda/actualiza calificaciones en el repo de GitHub vía API.
    Incluye todas las respuestas de cada alumno y las respuestas correctas.
    """
    try:
        token  = st.secrets["GH_TOKEN"]
        repo   = st.secrets["GH_REPO"]
        branch = st.secrets.get("GH_BRANCH", "main")
    except Exception as e:
        st.warning(f"⚠️ No se encontraron los secrets de GitHub: {e}")
        return False

    csv_path_gh = csv_nombre
    api_url = f"https://api.github.com/repos/{repo}/contents/{csv_path_gh}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Intentar hasta 3 veces
    for intento in range(3):
        sha = None
        contenido_actual = ""
        r = requests.get(api_url, headers=headers, params={"ref": branch})
        if r.status_code == 200:
            data = r.json()
            sha  = data["sha"]
            contenido_actual = base64.b64decode(data["content"]).decode("utf-8")
        elif r.status_code not in (404,):
            st.warning(f"⚠️ Error al leer GitHub ({r.status_code}): {r.text}")
            return False

        # Construir fila con todas las respuestas
        # Formato: Fecha,Nombre,Calificacion,Correctas,Total,Tiempo,P1_alumno,P1_correcta,P1_ok,P2_alumno,P2_correcta,P2_ok,...
        
        if not contenido_actual:
            # Crear encabezado
            encabezado = "Fecha,Nombre,Calificacion,Correctas,Total,Tiempo"
            for i in range(1, NUM_PREGUNTAS + 1):
                encabezado += f",P{i}_alumno,P{i}_correcta,P{i}_ok"
            contenido_actual = encabezado + "\n"

        # Construir fila de datos
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nueva_fila = f'"{timestamp}","{nombre}",{calificacion:.0f},{correctas},{NUM_PREGUNTAS},{tiempo_str(st.session_state.get("tiempo_usado", 0))}'
        
        for d in detalle:
            resp_alumno = d["respuesta_alumno"].replace('"', '""')  # Escapar comillas
            resp_correcta = d["respuesta_correcta"].replace('"', '""')
            ok = "1" if d["correcto"] else "0"
            nueva_fila += f',"{resp_alumno}","{resp_correcta}",{ok}'
        
        nueva_fila += "\n"
        nuevo_contenido = contenido_actual + nueva_fila
        contenido_b64   = base64.b64encode(nuevo_contenido.encode("utf-8")).decode("utf-8")

        # PUT
        payload = {
            "message": f"Calificacion: {nombre} — {calificacion:.0f}/10",
            "content": contenido_b64,
            "branch":  branch,
        }
        if sha:
            payload["sha"] = sha

        r2 = requests.put(api_url, headers=headers, data=json.dumps(payload))

        if r2.status_code in (200, 201):
            return True
        elif r2.status_code == 409 and intento < 2:
            time.sleep(1)
            continue
        else:
            st.warning(f"⚠️ No se pudo guardar en GitHub ({r2.status_code}): {r2.text}")
            return False

    return False


# ── Inicializar estado ────────────────────────────────────────────────────────

def init_state():
    defaults = {
        "pantalla":        "seleccionar_examen" if EXAMEN_FIJO is None else "login",
        "numero_examen":   EXAMEN_FIJO,
        "examen_config":   cargar_examen(EXAMEN_FIJO) if EXAMEN_FIJO else None,
        "nombre":          "",
        "preguntas_selec": [],
        "respuestas":      {},
        "inicio_ts":       None,
        "detalle":         [],
        "calificacion":    0.0,
        "tiempo_usado":    0,
        "enviado":         False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ════════════════════════════════════════════════════════════════════════════
#  PANTALLA 0 — SELECCIONAR EXAMEN (solo si EXAMEN_FIJO es None)
# ════════════════════════════════════════════════════════════════════════════

if EXAMEN_FIJO is None and st.session_state.pantalla == "seleccionar_examen":
    render_header()
    
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("#### 🎓 ¿Cuál examen deseas presentar?")
    st.markdown("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            '<div style="background:#f0f9f4; border:2px solid #2e8b57; border-radius:12px; padding:20px; text-align:center; cursor:pointer;">'
            '<div style="font-size:2rem; margin-bottom:8px;">📖</div>'
            '<div style="font-weight:600; color:#2e8b57; margin-bottom:4px;">Examen 1</div>'
            '<div style="font-size:0.85rem; color:#555;">Introducción a Python</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("Seleccionar", key="btn_e1", use_container_width=True):
            st.session_state.numero_examen = 1
            st.session_state.examen_config = cargar_examen(1)
            st.session_state.pantalla = "login"
            st.rerun()
    
    with col2:
        st.markdown(
            '<div style="background:#eef2f7; border:2px solid #58a6ff; border-radius:12px; padding:20px; text-align:center; cursor:pointer;">'
            '<div style="font-size:2rem; margin-bottom:8px;">📊</div>'
            '<div style="font-weight:600; color:#58a6ff; margin-bottom:4px;">Examen 2</div>'
            '<div style="font-size:0.85rem; color:#555;">Listas, Diccionarios, Operadores</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("Seleccionar", key="btn_e2", use_container_width=True):
            st.session_state.numero_examen = 2
            st.session_state.examen_config = cargar_examen(2)
            st.session_state.pantalla = "login"
            st.rerun()
    
    with col3:
        st.markdown(
            '<div style="background:#f4e8f7; border:2px solid #d946ef; border-radius:12px; padding:20px; text-align:center; cursor:pointer;">'
            '<div style="font-size:2rem; margin-bottom:8px;">⚙️</div>'
            '<div style="font-weight:600; color:#d946ef; margin-bottom:4px;">Examen 3</div>'
            '<div style="font-size:0.85rem; color:#555;">Control de Flujo</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("Seleccionar", key="btn_e3", use_container_width=True):
            st.session_state.numero_examen = 3
            st.session_state.examen_config = cargar_examen(3)
            st.session_state.pantalla = "login"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
#  PANTALLA 1 — LOGIN
# ════════════════════════════════════════════════════════════════════════════

if st.session_state.pantalla == "login":
    render_header()

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("#### Ingresa tu nombre para comenzar")
    nombre = st.text_input("Nombre", placeholder="p. ej.  Ana García López", label_visibility="collapsed")
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        iniciar = st.button("▶  Comenzar examen  (10 min)", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align:center; color:#888; font-size:0.8rem; margin-top:14px;'>"
        "Tendrás <strong>10 minutos</strong> para responder 5 preguntas. "
        "El examen se envía automáticamente al terminar el tiempo.</p>",
        unsafe_allow_html=True,
    )

    if iniciar:
        if not nombre.strip():
            st.error("⚠️  Por favor ingresa tu nombre antes de continuar.")
        else:
            st.session_state.nombre          = nombre.strip()
            st.session_state.preguntas_selec = random.sample(st.session_state.examen_config["preguntas"], NUM_PREGUNTAS)
            st.session_state.respuestas      = {}
            st.session_state.inicio_ts       = time.time()
            st.session_state.enviado         = False
            st.session_state.pantalla        = "examen"
            st.rerun()


# ════════════════════════════════════════════════════════════════════════════
#  PANTALLA 2 — EXAMEN
# ════════════════════════════════════════════════════════════════════════════

elif st.session_state.pantalla == "examen":
    render_header()

    elapsed  = time.time() - st.session_state.inicio_ts
    restante = max(0, TIEMPO_LIMITE - elapsed)

    # ── Tiempo agotado → envío automático ──
    if restante == 0 and not st.session_state.enviado:
        st.session_state.enviado      = True
        st.session_state.tiempo_usado = TIEMPO_LIMITE
        st.session_state.detalle      = calificar(
            st.session_state.preguntas_selec,
            st.session_state.respuestas,
        )
        correctas = sum(1 for r in st.session_state.detalle if r["correcto"])
        st.session_state.calificacion = correctas * PUNTOS_POR_PREGUNTA
        guardar_en_github(
            st.session_state.nombre,
            st.session_state.calificacion,
            correctas,
            st.session_state.detalle,
            st.session_state.examen_config["csv"],
        )
        st.session_state.pantalla = "resultado"
        st.rerun()

    # ── Timer ──
    clase_timer = color_timer(restante)
    st.markdown(
        f'<div class="timer-box {clase_timer}">⏱&nbsp; {tiempo_str(restante)}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="alumno-info">👤 &nbsp;<strong>{st.session_state.nombre}</strong></div>',
        unsafe_allow_html=True,
    )

    # ── Preguntas ──
    for i, p in enumerate(st.session_state.preguntas_selec):
        with st.container():
            st.markdown(
                f'<div style="background:#ffffff; border:1px solid #dde3ea; border-radius:10px; '
                f'padding:22px 26px; margin-bottom:18px; box-shadow:0 1px 4px rgba(0,0,0,0.05);">'
                f'<span style="display:inline-block; background:#2e8b57; color:#fff; font-weight:700; '
                f'font-size:0.72rem; padding:3px 12px; border-radius:20px; margin-bottom:12px; '
                f'letter-spacing:0.06em;">Pregunta {i+1}</span></div>',
                unsafe_allow_html=True,
            )
            st.markdown(p["enunciado"])

            pid = p["id"]
            if p["tipo"] == "escritura":
                nueva = st.text_area(
                    f"resp_{pid}",
                    placeholder=p.get("placeholder", "Tu respuesta aquí..."),
                    height=100,
                    key=f"input_{pid}",
                    label_visibility="collapsed",
                )
                st.session_state.respuestas[pid] = nueva
            else:
                opciones = p["opciones"]
                val      = st.session_state.respuestas.get(pid, None)
                
                # Mostrar opciones formateadas si contienen código
                st.markdown("**Opciones:**")
                for i, opc in enumerate(opciones):
                    # Si contiene saltos de línea, mostrar como bloque de código
                    if '\n' in opc:
                        st.markdown(f"**{chr(97+i)})**")
                        st.code(opc, language="python")
                    else:
                        st.markdown(f"**{chr(97+i)})** `{opc}`")
                
                # Selector de respuesta - mostrar a), b), c), d)
                idx = opciones.index(val) if val in opciones else None
                sel = st.radio(
                    f"opc_{pid}",
                    range(len(opciones)),
                    format_func=lambda x: f"{chr(97+x)})",
                    index=None,
                    key=f"radio_{pid}",
                    label_visibility="collapsed",
                )
                if sel is not None:
                    st.session_state.respuestas[pid] = opciones[sel]
            st.markdown("---")

    # ── Botón enviar ──
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        enviar = st.button("✅  Enviar examen", use_container_width=True)

    if enviar and not st.session_state.enviado:
        st.session_state.enviado      = True
        st.session_state.tiempo_usado = int(elapsed)
        st.session_state.detalle      = calificar(
            st.session_state.preguntas_selec,
            st.session_state.respuestas,
        )
        correctas = sum(1 for r in st.session_state.detalle if r["correcto"])
        st.session_state.calificacion = correctas * PUNTOS_POR_PREGUNTA
        guardar_en_github(
            st.session_state.nombre,
            st.session_state.calificacion,
            correctas,
            st.session_state.detalle,
            st.session_state.examen_config["csv"],
        )
        st.session_state.pantalla = "resultado"
        st.rerun()

    time.sleep(1)
    st.rerun()


# ════════════════════════════════════════════════════════════════════════════
#  PANTALLA 3 — RESULTADO
# ════════════════════════════════════════════════════════════════════════════

elif st.session_state.pantalla == "resultado":
    render_header()

    cal       = st.session_state.calificacion
    correctas = sum(1 for r in st.session_state.detalle if r["correcto"])
    color     = "cal-verde" if cal >= 7 else ("cal-amarillo" if cal >= 5 else "cal-rojo")
    emoji     = "🟢" if cal >= 7 else ("🟡" if cal >= 5 else "🔴")

    st.markdown(f"""
    <div class="resultado-box">
      <div style="color:#888; font-size:0.78rem; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.08em;">Calificación final</div>
      <div class="cal-numero {color}">{cal:.0f}<span style="font-size:1.8rem; color:#aaa;"> / 10</span></div>
      <div style="margin:14px 0; font-size:0.95rem; color:#444;">
        {emoji} &nbsp; {correctas} de {NUM_PREGUNTAS} preguntas correctas
      </div>
      <div style="color:#888; font-size:0.78rem;">
        Alumno: <strong>{st.session_state.nombre}</strong> &nbsp;·&nbsp;
        Tiempo: {tiempo_str(st.session_state.tiempo_usado)}
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Detalle de respuestas")

    for i, r in enumerate(st.session_state.detalle):
        icono  = "✅" if r["correcto"] else "❌"
        clase  = "detalle-ok" if r["correcto"] else "detalle-mal"
        estado = "Correcta"   if r["correcto"] else "Incorrecta"
        resp_alumno = r["respuesta_alumno"] or "(sin respuesta)"
        resp_correcta = r.get("respuesta_correcta", "")
        enunciado = r.get("enunciado", "")
        
        st.markdown(
            f'<div style="margin-bottom:18px; padding:12px 16px; background:#f8f9fb; border-left:4px solid #2e8b57; border-radius:6px;">'
            f'<div style="font-weight:600; margin-bottom:10px; color:#1a1a2e;">'
            f'{icono} <span class="{clase}">Pregunta {i+1} — {estado}</span></div>',
            unsafe_allow_html=True,
        )
        
        # Mostrar el enunciado de la pregunta
        st.markdown(enunciado)
        
        st.markdown(
            f'<div style="margin-top:10px; padding-top:10px; border-top:1px solid #dde3ea;">'
            f'<div style="font-size:0.82rem; margin-bottom:6px;">'
            f'<strong>Tu respuesta:</strong> <code style="background:#fff; padding:2px 6px; border-radius:3px;">{resp_alumno}</code>'
            f'</div>',
            unsafe_allow_html=True,
        )
        
        if not r["correcto"] and resp_correcta:
            st.markdown(
                f'<div style="font-size:0.82rem;">'
                f'<strong style="color:#2e8b57;">Respuesta correcta:</strong> '
                f'<code style="background:#f0f9f4; padding:2px 6px; border-radius:3px; color:#2e8b57;">{resp_correcta}</code>'
                f'</div>',
                unsafe_allow_html=True,
            )
        
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄  Nuevo intento", use_container_width=True):
            pantalla_destino = "login" if EXAMEN_FIJO else "seleccionar_examen"
            st.session_state.pantalla = pantalla_destino
            st.session_state.nombre = ""
            st.session_state.respuestas = {}
            st.session_state.enviado = False
            st.rerun()

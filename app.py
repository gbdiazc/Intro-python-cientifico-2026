import streamlit as st
import random
import time
import base64
import json
import requests
from datetime import datetime

# ── Cargar examen dinámicamente ──────────────────────────────────────────────
def cargar_examen(numero_examen):
    if numero_examen == 1:
        from preguntas_e1 import PREGUNTAS as P
        return {"numero": 1, "titulo": "Introducción a la programación en Python",             "preguntas": P, "csv": "calificaciones_e1.csv"}
    elif numero_examen == 2:
        from preguntas_e2 import PREGUNTAS as P
        return {"numero": 2, "titulo": "Listas, Diccionarios, Operaciones, Booleanos y Operadores Lógicos", "preguntas": P, "csv": "calificaciones_e2.csv"}
    elif numero_examen == 3:
        from preguntas_e3 import PREGUNTAS as P
        return {"numero": 3, "titulo": "Control de Flujo: IF, ELIF, ELSE, WHILE, FOR",         "preguntas": P, "csv": "calificaciones_e3.csv"}
    elif numero_examen == 4:
        from preguntas_e4 import PREGUNTAS as P
        return {"numero": 4, "titulo": "Loops (FOR), BREAK, CONTINUE, Funciones y Argumentos", "preguntas": P, "csv": "calificaciones_e4.csv"}
    else:
        return None

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(page_title="Examen — Python IMP", page_icon="🧪", layout="centered")

TIEMPO_LIMITE    = 10 * 60   # segundos
NUM_PREGUNTAS    = 5
PUNTOS_POR_PREG  = 2         # 5 × 2 = 10

# ── CONFIGURACIÓN: Elige qué examen mostrar ──────────────────────────────────
# None  → Los alumnos eligen (pantalla de selección)
# 1,2,3 o 4 → Va directo a login con ese examen
EXAMEN_FIJO = None   # <── Cambia aquí: None, 1, 2, 3 o 4

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
body, .stApp { background:#f8f9fa !important; }
.header-box {
    background:#ffffff; border:1px solid #dee2e6;
    border-radius:12px; padding:24px 32px 18px;
    margin-bottom:24px; text-align:center;
    box-shadow:0 2px 8px rgba(0,0,0,.06);
}
.header-box h1 { color:#2e8b57; font-size:1.6rem; margin:0 0 4px; }
.header-box h2 { color:#2e8b57; font-size:1.1rem; margin:0 0 4px; }
.header-box h3 { color:#555;    font-size:0.95rem; margin:0 0 10px; }
.header-box .prof { color:#333; font-size:0.9rem; }
.header-box .dept { color:#666; font-size:0.8rem; margin-top:6px; }
.login-box  {
    background:#fff; border:1px solid #dee2e6;
    border-radius:12px; padding:28px 32px;
    box-shadow:0 2px 8px rgba(0,0,0,.06);
}
.timer-box  {
    text-align:center; font-size:1.6rem; font-weight:700;
    padding:10px; border-radius:8px; margin-bottom:16px;
}
.timer-ok  { background:#d4edda; color:#155724; }
.timer-mid { background:#fff3cd; color:#856404; }
.timer-low { background:#f8d7da; color:#721c24; }
.alumno-info { background:#e9ecef; border-radius:8px; padding:8px 14px; margin-bottom:16px; font-size:0.9rem; }
.pregunta-box {
    background:#fff; border:1px solid #dee2e6;
    border-radius:10px; padding:20px 24px; margin-bottom:20px;
    box-shadow:0 1px 4px rgba(0,0,0,.04);
}
.detalle-item { margin-bottom:8px; font-size:0.9rem; }
.detalle-ok  { color:#155724; font-weight:600; }
.detalle-mal { color:#721c24; font-weight:600; }
.card-examen {
    background:#fff; border:2px solid #dee2e6; border-radius:12px;
    padding:20px; text-align:center; margin-bottom:8px;
}
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────────────────
def render_header(subtitulo=""):
    num = st.session_state.get("numero_examen", None)
    num_str = f"Examen {num} · " if num else ""
    st.markdown(f"""
    <div class="header-box">
        <h1>Introducción a la programación en Python</h1>
        <h2>Instituto Mexicano del Petróleo</h2>
        <h3>{num_str}4 de Junio de 2026{(" — " + subtitulo) if subtitulo else ""}</h3>
        <div class="prof"><strong>Dra. Gabriela Berenice Díaz Cortés</strong><br><em>gbdiaz@imp.mx</em></div>
        <div class="prof"><strong>Dr. Luis Antonio López Peña</strong><br><em>llopezp@imp.mx</em></div>
        <div class="dept">Dirección de Investigación · Gerencia de Investigación en Explotación</div>
    </div>
    """, unsafe_allow_html=True)

# ── Guardar en GitHub ─────────────────────────────────────────────────────────
def guardar_en_github(nombre, calificacion, correctas, detalle, csv_nombre="calificaciones.csv"):
    try:
        token  = st.secrets["GH_TOKEN"]
        repo   = st.secrets["GH_REPO"]
        branch = st.secrets.get("GH_BRANCH", "main")
    except Exception as e:
        st.warning(f"⚠️ Secrets de GitHub no encontrados: {e}")
        return False

    api_url = f"https://api.github.com/repos/{repo}/contents/{csv_nombre}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

    for intento in range(3):
        sha = None
        contenido_actual = ""
        r = requests.get(api_url, headers=headers, params={"ref": branch})
        if r.status_code == 200:
            d   = r.json()
            sha = d["sha"]
            contenido_actual = base64.b64decode(d["content"]).decode("utf-8")
        elif r.status_code not in (404,):
            st.warning(f"⚠️ Error al leer GitHub ({r.status_code})")
            return False

        if not contenido_actual:
            contenido_actual = "Fecha,Nombre,Calificacion,Correctas,Total,Tiempo\n"

        nueva_fila = (
            f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")},'
            f'"{nombre}",'
            f'{calificacion:.0f},{correctas},{NUM_PREGUNTAS},'
            f'{tiempo_str(st.session_state.get("tiempo_usado", 0))}\n'
        )
        nuevo = contenido_actual + nueva_fila
        b64   = base64.b64encode(nuevo.encode("utf-8")).decode("utf-8")
        payload = {"message": f"Calificacion: {nombre} — {calificacion:.0f}/10", "content": b64, "branch": branch}
        if sha:
            payload["sha"] = sha
        r2 = requests.put(api_url, headers=headers, data=json.dumps(payload))
        if r2.status_code in (200, 201):
            return True
        elif r2.status_code == 409 and intento < 2:
            time.sleep(1)
        else:
            st.warning(f"⚠️ No se pudo guardar ({r2.status_code})")
            return False
    return False

# ── Calificar ─────────────────────────────────────────────────────────────────
def calificar(preguntas, respuestas):
    detalle = []
    for p in preguntas:
        pid  = p["id"]
        resp = respuestas.get(pid, "").strip()
        if p["tipo"] == "escritura":
            correcto = resp in [v.strip() for v in p["respuestas_validas"]]
        else:
            correcto = resp == p["respuesta_correcta"]
        detalle.append({"id": pid, "tipo": p["tipo"], "respuesta_alumno": resp, "correcto": correcto})
    return detalle

def tiempo_str(seg):
    m, s = divmod(int(seg), 60)
    return f"{m:02d}:{s:02d}"

def color_timer(seg):
    if seg > 120: return "timer-ok"
    if seg > 60:  return "timer-mid"
    return "timer-low"

# ── Estado inicial ────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "pantalla":        "seleccionar_examen" if EXAMEN_FIJO is None else "login",
        "numero_examen":   EXAMEN_FIJO,
        "examen_config":   cargar_examen(EXAMEN_FIJO) if EXAMEN_FIJO else None,
        "nombre":          "",
        "matricula":       "",
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

    examenes = [
        (1, "📖", "Examen 1", "Introducción a Python"),
        (2, "📊", "Examen 2", "Listas, Diccionarios, Operadores"),
        (3, "⚙️",  "Examen 3", "Control de Flujo: IF, WHILE"),
        (4, "🔄", "Examen 4", "FOR, BREAK, CONTINUE, Funciones"),
    ]
    col1, col2 = st.columns(2)
    cols = [col1, col2, col1, col2]
    for (num, ico, titulo, desc), col in zip(examenes, cols):
        with col:
            st.markdown(
                f'<div class="card-examen">'
                f'<div style="font-size:2rem">{ico}</div>'
                f'<div style="font-weight:600;color:#2e8b57">{titulo}</div>'
                f'<div style="font-size:0.82rem;color:#666">{desc}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
            if st.button("Seleccionar", key=f"btn_e{num}", use_container_width=True):
                st.session_state.numero_examen = num
                st.session_state.examen_config = cargar_examen(num)
                st.session_state.pantalla      = "login"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  PANTALLA 1 — LOGIN
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pantalla == "login":
    cfg = st.session_state.examen_config
    subtitulo = cfg["titulo"] if cfg else ""
    render_header(subtitulo)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("#### Antes de comenzar, escribe tu nombre")
    nombre = st.text_input("👤 Nombre completo", placeholder="p. ej. Ana García López", label_visibility="collapsed")
    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        iniciar = st.button("▶  Comenzar examen  (10 min)", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align:center;color:#888;font-size:0.8rem;margin-top:14px'>"
        "Tendrás <strong>10 minutos</strong> para responder 5 preguntas. "
        "El examen se envía automáticamente al terminar el tiempo.</p>",
        unsafe_allow_html=True,
    )

    if iniciar:
        if not nombre.strip():
            st.error("⚠️ Por favor ingresa tu nombre antes de continuar.")
        elif cfg is None:
            st.error("⚠️ No hay examen configurado. Regresa y selecciona uno.")
        else:
            st.session_state.nombre          = nombre.strip()
            st.session_state.preguntas_selec = random.sample(cfg["preguntas"], NUM_PREGUNTAS)
            st.session_state.respuestas      = {}
            st.session_state.inicio_ts       = time.time()
            st.session_state.enviado         = False
            st.session_state.pantalla        = "examen"
            st.rerun()

# ════════════════════════════════════════════════════════════════════════════
#  PANTALLA 2 — EXAMEN
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pantalla == "examen":
    cfg      = st.session_state.examen_config
    render_header(cfg["titulo"] if cfg else "")

    elapsed  = time.time() - st.session_state.inicio_ts
    restante = max(0, TIEMPO_LIMITE - elapsed)

    # Tiempo agotado → envío automático
    if restante == 0 and not st.session_state.enviado:
        st.session_state.enviado      = True
        st.session_state.tiempo_usado = TIEMPO_LIMITE
        st.session_state.detalle      = calificar(
            st.session_state.preguntas_selec, st.session_state.respuestas)
        correctas = sum(1 for r in st.session_state.detalle if r["correcto"])
        st.session_state.calificacion = correctas * PUNTOS_POR_PREG
        guardar_en_github(
            st.session_state.nombre, st.session_state.calificacion,
            correctas, st.session_state.detalle, cfg["csv"] if cfg else "calificaciones.csv")
        st.session_state.pantalla = "resultado"
        st.rerun()

    # Timer
    st.markdown(
        f'<div class="timer-box {color_timer(restante)}">⏱ {tiempo_str(restante)}</div>',
        unsafe_allow_html=True)
    st.markdown(
        f'<div class="alumno-info">👤 <strong>{st.session_state.nombre}</strong>'
        f'</div>',
        unsafe_allow_html=True)

    preguntas = st.session_state.preguntas_selec

    for i, p in enumerate(preguntas):
        st.markdown(f'<div class="pregunta-box">', unsafe_allow_html=True)
        st.markdown(f"**Pregunta {i+1} / {NUM_PREGUNTAS}**")
        st.markdown(p["enunciado"])

        pid = p["id"]
        if p["tipo"] == "escritura":
            val = st.session_state.respuestas.get(pid, "")
            nueva = st.text_area(
                "Tu respuesta:",
                value=val,
                height=120,
                key=f"resp_{pid}",
                placeholder=p.get("placeholder", ""),
                label_visibility="collapsed",
            )
            st.session_state.respuestas[pid] = nueva

        else:  # opcion_multiple
            opciones = p["opciones"]
            val_actual = st.session_state.respuestas.get(pid, None)
            # Mostrar cada opción con su código antes del radio
            for letra, codigo in opciones.items():
                seleccionado = "✅ " if val_actual == letra else ""
                st.markdown(f"**{seleccionado}{letra})**")
                st.code(codigo, language="python")
            # Radio para seleccionar (solo muestra las letras)
            letras = list(opciones.keys())
            idx = letras.index(val_actual) if val_actual in letras else None
            sel = st.radio(
                "Selecciona tu respuesta:",
                letras,
                index=idx,
                key=f"radio_{pid}",
                horizontal=True,
            )
            if sel:
                st.session_state.respuestas[pid] = sel

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        enviar = st.button("✅  Enviar examen", use_container_width=True)

    if enviar and not st.session_state.enviado:
        st.session_state.enviado      = True
        st.session_state.tiempo_usado = int(elapsed)
        st.session_state.detalle      = calificar(
            st.session_state.preguntas_selec, st.session_state.respuestas)
        correctas = sum(1 for r in st.session_state.detalle if r["correcto"])
        st.session_state.calificacion = correctas * PUNTOS_POR_PREG
        guardar_en_github(
            st.session_state.nombre, st.session_state.calificacion,
            correctas, st.session_state.detalle, cfg["csv"] if cfg else "calificaciones.csv")
        st.session_state.pantalla = "resultado"
        st.rerun()

    # Auto-refresh cada 5 segundos para actualizar el timer
    st.markdown(
        "<script>setTimeout(()=>window.location.reload(), 5000)</script>",
        unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  PANTALLA 3 — RESULTADO
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pantalla == "resultado":
    render_header()

    cal  = st.session_state.calificacion
    det  = st.session_state.detalle
    correctas = sum(1 for r in det if r["correcto"])

    if cal >= 8:
        emoji, color, msg = "🎉", "#155724", "¡Excelente trabajo!"
    elif cal >= 6:
        emoji, color, msg = "👍", "#856404", "¡Buen esfuerzo!"
    else:
        emoji, color, msg = "📚", "#721c24", "Sigue practicando."

    st.markdown(f"""
    <div style="text-align:center; background:#fff; border-radius:12px; padding:32px;
                border:1px solid #dee2e6; box-shadow:0 2px 8px rgba(0,0,0,.06)">
        <div style="font-size:3rem">{emoji}</div>
        <h2 style="color:{color}; margin:12px 0 4px">{cal:.0f} / 10</h2>
        <p style="color:#555">{msg}</p>
        <p style="color:#888; font-size:0.85rem">
            {correctas} de {NUM_PREGUNTAS} correctas &nbsp;·&nbsp;
            Tiempo usado: {tiempo_str(st.session_state.tiempo_usado)}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Detalle de respuestas")
    for i, r in enumerate(det):
        icono = "✅" if r["correcto"] else "❌"
        clase = "detalle-ok" if r["correcto"] else "detalle-mal"
        estado = "Correcta" if r["correcto"] else "Incorrecta"
        resp  = r["respuesta_alumno"] or "(sin respuesta)"
        st.markdown(
            f'<div class="detalle-item">{icono} '
            f'<span class="{clase}">Pregunta {i+1} — {estado}</span>'
            f'&nbsp;&nbsp;·&nbsp;&nbsp;Tu respuesta: <code>{resp}</code></div>',
            unsafe_allow_html=True)

    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄  Nuevo intento", use_container_width=True):
            pantalla_dest = "login" if EXAMEN_FIJO else "seleccionar_examen"
            for k in ["nombre", "preguntas_selec", "respuestas",
                      "inicio_ts", "detalle", "calificacion", "tiempo_usado", "enviado"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.session_state.pantalla = pantalla_dest
            if EXAMEN_FIJO:
                st.session_state.numero_examen = EXAMEN_FIJO
                st.session_state.examen_config = cargar_examen(EXAMEN_FIJO)
            st.rerun()

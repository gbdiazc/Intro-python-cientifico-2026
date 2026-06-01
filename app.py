import streamlit as st
import random
import time
import csv
import os
from datetime import datetime
from preguntas import PREGUNTAS

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Examen 1 — Python IMP",
    page_icon="🧪",
    layout="centered",
)

TIEMPO_LIMITE = 5 * 60   # segundos
CSV_PATH = "calificaciones.csv"

# ── CSS global — tema claro, estilo limpio ────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #f5f7fa !important;
    color: #1a1a2e !important;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; max-width: 820px !important; }

/* ── Encabezado institucional ── */
.header-box {
    background-color: #f2f2f2;
    border-left: 8px solid #2e8b57;
    padding: 20px;
    border-radius: 10px;
    font-family: Arial, sans-serif;
    margin-bottom: 24px;
    text-align: center;
}
.header-box h1 { color: #2e8b57; font-size: 1.35rem; margin: 0 0 4px 0; }
.header-box h2 { color: #2e8b57; font-size: 1.05rem; margin: 0 0 4px 0; }
.header-box h3 { color: #2e8b57; font-size: 0.9rem;  margin: 0 0 14px 0; font-weight: 500; }
.header-box .prof { font-size: 15px; color: #333; line-height: 1.8; margin-bottom: 10px; }
.header-box .dept { font-size: 14px; color: #555; }

/* ── Timer ── */
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

/* ── Tarjeta de pregunta ── */
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

/* ── Inputs ── */
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

/* ── Radio buttons ── */
.stRadio > div { gap: 7px !important; }
.stRadio label {
    background: #f8f9fb !important;
    border: 1.5px solid #dde3ea !important;
    border-radius: 8px !important;
    padding: 9px 16px !important;
    font-size: 0.83rem !important;
    font-family: 'JetBrains Mono', monospace !important;
    color: #2c3e50 !important;
    cursor: pointer !important;
    transition: border-color 0.15s, background 0.15s;
}
.stRadio label:hover {
    border-color: #2e8b57 !important;
    background: #f0f9f4 !important;
}

/* ── Botones ── */
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
    transition: opacity 0.2s, transform 0.1s !important;
    box-shadow: 0 2px 8px rgba(46,139,87,0.25) !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

/* ── Login box ── */
.login-box {
    background: #ffffff;
    border: 1px solid #dde3ea;
    border-radius: 12px;
    padding: 30px 36px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    margin-top: 8px;
}

/* ── Resultado ── */
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

/* ── Code blocks ── */
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

/* ── Info alumno ── */
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


# ── Helpers ─────────────────────────────────────────────────────────────────

def render_header():
    st.markdown("""
    <div style="background-color:#f2f2f2; border-left: 8px solid #2e8b57; padding: 20px; border-radius: 10px; font-family: Arial, sans-serif; margin-bottom: 24px;">
      <center>
        <h1 style="color:#2e8b57;">Introducción a la programación en Python</h1>
        <h2 style="color:#2e8b57;">Instituto Mexicano del Petróleo</h2>
        <h3 style="color:#2e8b57;">Examen 1 &nbsp;·&nbsp; 2 de Junio de 2026</h3>
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


def guardar_calificacion(nombre, calificacion, total, respuestas_detalle):
    existe = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow([
                "Fecha", "Nombre",
                "Calificacion", "Correctas", "Total",
                "Preguntas_IDs", "Tiempo_usado_seg"
            ])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            nombre,
            round(calificacion, 2),
            sum(1 for r in respuestas_detalle if r["correcto"]),
            total,
            "-".join(str(r["id"]) for r in respuestas_detalle),
            st.session_state.get("tiempo_usado", "N/A"),
        ])


def calificar(preguntas, respuestas):
    detalle = []
    for p in preguntas:
        pid  = p["id"]
        resp = respuestas.get(pid, "").strip()
        if p["tipo"] == "escritura":
            correcto = resp in [v.strip() for v in p["respuestas_validas"]]
        else:
            correcto = resp == p["respuesta_correcta"]
        detalle.append({
            "id": pid,
            "tipo": p["tipo"],
            "respuesta_alumno": resp,
            "correcto": correcto,
        })
    return detalle


def tiempo_str(seg):
    m, s = divmod(int(seg), 60)
    return f"{m:02d}:{s:02d}"


def color_timer(seg):
    if seg > 120:
        return "timer-ok"
    elif seg > 60:
        return "timer-mid"
    return "timer-low"


# ── Inicializar estado ────────────────────────────────────────────────────────

def init_state():
    defaults = {
        "pantalla":         "login",
        "nombre":           "",
        "preguntas_selec":  [],
        "respuestas":       {},
        "inicio_ts":        None,
        "detalle":          [],
        "calificacion":     0.0,
        "tiempo_usado":     0,
        "enviado":          False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()


# ════════════════════════════════════════════════════════════════════════════
#  PANTALLA 1 — LOGIN
# ════════════════════════════════════════════════════════════════════════════

if st.session_state.pantalla == "login":
    render_header()

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("#### Ingresa tu nombre para comenzar")
    nombre = st.text_input("Nombre completo", placeholder="p. ej.  Ana García López", label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        iniciar = st.button("▶  Comenzar examen  (5 min)", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align:center; color:#888; font-size:0.8rem; margin-top:14px;'>"
        "Tendrás <strong>5 minutos</strong> para responder 5 preguntas. "
        "El examen se envía automáticamente al terminar el tiempo.</p>",
        unsafe_allow_html=True,
    )

    if iniciar:
        if not nombre.strip():
            st.error("⚠️  Por favor ingresa tu nombre antes de continuar.")
        else:
            st.session_state.nombre          = nombre.strip()
            st.session_state.preguntas_selec = random.sample(PREGUNTAS, 5)
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
        st.session_state.calificacion = (correctas / 5) * 10
        guardar_calificacion(
            st.session_state.nombre,
            st.session_state.calificacion,
            5,
            st.session_state.detalle,
        )
        st.session_state.pantalla = "resultado"
        st.rerun()

    # ── Timer ──
    clase_timer = color_timer(restante)
    st.markdown(
        f'<div class="timer-box {clase_timer}">⏱&nbsp; {tiempo_str(restante)}</div>',
        unsafe_allow_html=True,
    )

    # ── Info alumno ──
    st.markdown(
        f'<div class="alumno-info">👤 &nbsp;<strong>{st.session_state.nombre}</strong></div>',
        unsafe_allow_html=True,
    )

    # ── Preguntas ──
    preguntas = st.session_state.preguntas_selec

    for i, p in enumerate(preguntas):
        st.markdown(f'<div class="pregunta-card">', unsafe_allow_html=True)
        st.markdown(f'<span class="pregunta-num">Pregunta {i+1}</span>', unsafe_allow_html=True)
        st.markdown(p["enunciado"])

        pid = p["id"]
        if p["tipo"] == "escritura":
            val   = st.session_state.respuestas.get(pid, "")
            nueva = st.text_input(
                f"resp_{pid}",
                value=val,
                placeholder=p.get("placeholder", ""),
                key=f"input_{pid}",
                label_visibility="collapsed",
            )
            st.session_state.respuestas[pid] = nueva

        else:
            opciones = p["opciones"]
            val      = st.session_state.respuestas.get(pid, None)
            idx      = opciones.index(val) if val in opciones else None
            sel      = st.radio(
                f"opc_{pid}",
                opciones,
                index=idx,
                key=f"radio_{pid}",
                label_visibility="collapsed",
            )
            st.session_state.respuestas[pid] = sel

        st.markdown("</div>", unsafe_allow_html=True)

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
        st.session_state.calificacion = (correctas / 5) * 10
        guardar_calificacion(
            st.session_state.nombre,
            st.session_state.calificacion,
            5,
            st.session_state.detalle,
        )
        st.session_state.pantalla = "resultado"
        st.rerun()

    # ── Refresh cada segundo ──
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
      <div class="cal-numero {color}">{cal:.1f}<span style="font-size:1.8rem; color:#aaa;"> / 10</span></div>
      <div style="margin:14px 0; font-size:0.95rem; color:#444;">
        {emoji} &nbsp; {correctas} de 5 preguntas correctas
      </div>
      <div style="color:#888; font-size:0.78rem;">
        Alumno: <strong>{st.session_state.nombre}</strong> &nbsp;·&nbsp;
        Tiempo: {tiempo_str(st.session_state.tiempo_usado)} &nbsp;·&nbsp;
        Guardado ✓
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Detalle de respuestas")

    for i, r in enumerate(st.session_state.detalle):
        icono  = "✅" if r["correcto"] else "❌"
        clase  = "detalle-ok"  if r["correcto"] else "detalle-mal"
        estado = "Correcta"    if r["correcto"] else "Incorrecta"
        resp   = r["respuesta_alumno"] or "(sin respuesta)"
        st.markdown(
            f'<div class="detalle-item">'
            f'{icono} <span class="{clase}">Pregunta {i+1} — {estado}</span>'
            f'&nbsp;&nbsp;·&nbsp;&nbsp;Tu respuesta: <code>{resp}</code>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── Descarga CSV ──
    if os.path.isfile(CSV_PATH):
        with open(CSV_PATH, "rb") as f:
            st.download_button(
                label="📥  Descargar calificaciones.csv",
                data=f,
                file_name="calificaciones.csv",
                mime="text/csv",
            )

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄  Nuevo intento", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

import streamlit as st
import time

# Configuración de la página
st.set_page_config(
    page_title="Agradecimientos de Rotación | Epidemiología",
    page_icon="🩺",
    layout="centered"
)

# Estilos CSS personalizados para simular transiciones fluidas tipo Prezi y diseño elegante
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .prezi-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 2.5rem;
        border-radius: 20px;
        color: #f8fafc;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.2);
        border: 1px solid #334155;
        margin-top: 1rem;
        margin-bottom: 2rem;
        animation: fadeIn 0.8s ease-in-out;
    }
    
    .prezi-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 1rem;
        border-bottom: 2px solid #334155;
        padding-bottom: 0.5rem;
    }
    
    .prezi-subtitle {
        font-size: 1.1rem;
        color: #cbd5e1;
        font-weight: 300;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }
    
    .prezi-quote {
        font-style: italic;
        color: #94a3b8;
        border-left: 4px solid #38bdf8;
        padding-left: 1rem;
        margin-top: 1rem;
        font-size: 1rem;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px) scale(0.98); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Control de estados para la navegación tipo diapositiva/zoom de Prezi
if 'step' not in st.session_state:
    st.session_state.step = 0

total_steps = 5

def next_step():
    if st.session_state.step < total_steps - 1:
        st.session_state.step += 1

def prev_step():
    if st.session_state.step > 0:
        st.session_state.step -= 1

# Barra de progreso cenital
progress_val = (st.session_state.step + 1) / total_steps
st.progress(progress_val)

# --- PASO 0: INTRODUCCIÓN GENERAL ---
if st.session_state.step == 0:
    st.markdown("""
        <div class="prezi-card" style="text-align: center;">
            <div class="prezi-title" style="border: none; justify-content: center;">✨ Reflexiones y Agradecimientos de Rotación ✨</div>
            <p class="prezi-subtitle" style="font-size: 1.25rem;">
                Un recorrido por los aprendizajes, las mentorías y las experiencias que marcaron un antes y un después en mi formación como epidemiólogo.
            </p>
            <p class="prezi-quote">
                "La salud pública no se construye solo con teoría, sino con las manos y el ejemplo de quienes nos enseñan el camino."
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- PASO 1: DRA. ELISA ---
elif st.session_state.step == 1:
    st.markdown("""
        <div class="prezi-card">
            <div class="prezi-title">🩺 Dra. Elisa</div>
            <p class="prezi-subtitle">
                Gracias por esta rotación. Usted me enseñó que la epidemiología va mucho más allá de números fríos y métricas en un reporte: es saber tomar decisiones con empatía, gestionar la incertidumbre y liderar un equipo con una visión profundamente humana para conseguir metas que realmente transformen la salud de la comunidad.<br><br>
                Gracias por impulsarme a pensar de forma estratégica, por cada consejo oportuno y por contagiarme esa pasión inquebrantable por la prevención. Gracias por enseñarme la Medicina Preventiva desde su verdadero sentido y por recordarme que, detrás de cada indicador y cada estadística, siempre hay personas esperando una respuesta.
            </p>
            <div class="prezi-quote">
                "Liderar con visión humana y transformar los datos en bienestar comunitario."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- PASO 2: DR. MANUEL ---
elif st.session_state.step == 2:
    st.markdown("""
        <div class="prezi-card">
            <div class="prezi-title">🔬 Dr. Manuel</div>
            <p class="prezi-subtitle">
                Gracias por esta rotación. Usted me enseñó que la epidemiología va más allá de ver indicadores detrás de un escritorio y exige salir al campo a hacer una verdadera vigilancia activa. Me demostró que lo fundamental es poseer bases sólidas, comprender a fondo el porqué clínico y social de los eventos de salud, y entender que nuestra disciplina abarca mucho más que supervisiones burocráticas.<br><br>
                Gracias por desafiar mi pensamiento analítico, por regalarme un enfoque clínico-epidemiológico completamente distinto y por mostrarme que el rigor científico, unido a la curiosidad constante, son las herramientas más poderosas de un médico especialista.
            </p>
            <div class="prezi-quote">
                "Entender el porqué de las cosas para hacer una vigilancia activa y con rigor científico."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- PASO 3: ENF. WENDY ---
elif st.session_state.step == 3:
    st.markdown("""
        <div class="prezi-card">
            <div class="prezi-title">💉 Enf. Wendy</div>
            <p class="prezi-subtitle">
                Gracias por esta rotación. Usted me enseñó que la epidemiología va más allá de ver las vacunas como simples esquemas fijos que cumplir en un papel. Me enseñó a leer los diferentes escenarios operativos, a individualizar a cada paciente para brindarle una atención de calidad y a dimensionar la compleja red logística que hay detrás de la inmunización.<br><br>
                Gracias por guiarme desde la gestión detallada de un puesto de vacunación hasta la importancia crítica de cuidar cada parámetro de la red de frío para garantizar la efectividad del biológico. Comprendí que aplicar una vacuna trasciende la técnica mecánica: es un acto sublime de protección comunitaria. ¡Arriba la Salud Pública!
            </p>
            <div class="prezi-quote">
                "Una vacuna va mucho más allá de una técnica; es el arte de proteger a toda una comunidad."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- PASO 4: LIC. BERE ---
elif st.session_state.step == 4:
    st.markdown("""
        <div class="prezi-card">
            <div class="prezi-title">📋 Lic. Bere</div>
            <p class="prezi-subtitle">
                Gracias por esta rotación. Usted me enseñó que la epidemiología va mucho más allá de administrar insumos o cumplir con trámites administrativos; es conocer a profundidad a la población clave para aterrizar estrategias efectivas y alinear los lineamientos vigentes a la realidad operativa.<br><br>
                Admiro enormemente su apertura al conocimiento, su disposición para enseñar sin reservas y su capacidad para no limitarse ante los obstáculos, encontrando siempre soluciones prácticas. Me demostró que la curiosidad es una virtud y que ante la duda, preguntar siempre abre la puerta al crecimiento. Gracias por enseñarme que la gestión en salud es el motor invisible que sostiene todo lo demás.
            </p>
            <div class="prezi-quote">
                "La administración va más allá de la gestión: es conocer a la población y transformar los recursos en soluciones."
            </div>
        </div>
    """, unsafe_allow_html=True)

# Controles de navegación interactivos estilo botonera de diapositivas
st.write("")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.step > 0:
        st.button("⬅️ Anterior", on_click=prev_step, use_container_width=True)

with col3:
    if st.session_state.step < total_steps - 1:
        st.button("Siguiente ➡️", on_click=next_step, use_container_width=True)
    else:
        if st.button("🔄 Reiniciar", on_click=lambda: update_step(0) if 'update_step' in globals() else st.session_state.update({'step': 0}), use_container_width=True):
            pass
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Agradecimientos de Rotación | Epidemiología",
    page_icon="🩺",
    layout="centered"
)

# Estilos CSS personalizados para el diseño moderno, tarjetas y botones limpios
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
        animation: fadeIn 0.6s ease-in-out;
    }
    
    .prezi-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 1.2rem;
        border-bottom: 2px solid #334155;
        padding-bottom: 0.5rem;
    }
    
    .mensaje-segmento {
        background: rgba(51, 65, 85, 0.4);
        padding: 1.1rem 1.3rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border-left: 4px solid #38bdf8;
        font-size: 1.05rem;
        line-height: 1.6;
        color: #cbd5e1;
    }
    
    .mensaje-segmento strong {
        color: #f8fafc;
    }
    
    .frase-cierre {
        font-style: italic;
        color: #94a3b8;
        text-align: center;
        margin-top: 1.5rem;
        font-size: 0.95rem;
        border-top: 1px dashed #334155;
        padding-top: 1rem;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px) scale(0.98); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Control de estados para saber qué sección/persona se está visualizando
if 'seccion' not in st.session_state:
    st.session_state.seccion = 'inicio'

# --- MENÚ DE BOTONES PRINCIPAL EN LA INTERFAZ ---
st.markdown("### 👋 Elige a quién agradecer:")

col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4)

with col_btn1:
    if st.button("👩‍⚕️ Dra. Elisa", use_container_width=True):
        st.session_state.seccion = 'elisa'
with col_btn2:
    if st.button("🔬 Dr. Manuel", use_container_width=True):
        st.session_state.seccion = 'manuel'
with col_btn3:
    if st.button("💉 Enf. Wendy", use_container_width=True):
        st.session_state.seccion = 'wendy'
with col_btn4:
    if st.button("📋 Lic. Bere", use_container_width=True):
        st.session_state.seccion = 'bere'

st.write("---")

# --- VISTA DE INICIO ---
if st.session_state.seccion == 'inicio':
    st.markdown("""
        <div class="prezi-card" style="text-align: center;">
            <div class="prezi-title" style="border: none;">✨ Reflexiones y Agradecimientos de Rotación ✨</div>
            <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.6;">
                Selecciona cualquiera de los botones superiores para descubrir los mensajes y reconocimientos especiales preparados para cada integrante del equipo.
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- VISTA: DRA. ELISA ---
elif st.session_state.seccion == 'elisa':
    st.markdown("""
        <div class="prezi-card">
            <div class="prezi-title">👩‍⚕️ ¡Gracias, Dra. Elisa!</div>
            <p style="color: #38bdf8; font-weight: 600; margin-bottom: 1.2rem;">Por su guía excepcional durante esta rotación</p>
            
            <div class="mensaje-segmento">
                <strong>Visión y Liderazgo Humano:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la Epidemiología va mucho más allá de números fríos y métricas en un reporte: es saber tomar decisiones con empatía, gestionar la incertidumbre y liderar un equipo con una visión profundamente humana para conseguir metas que realmente transformen la salud de la comunidad.
            </div>

            <div class="mensaje-segmento">
                <strong>Estrategia y Prevención:</strong><br>
                Gracias por impulsarme a pensar de forma estratégica, por cada consejo oportuno y por contagiarme esa pasión inquebrantable por la prevención. Gracias por enseñarme la Medicina Preventiva desde su verdadero sentido y por recordarme que, detrás de cada indicador y cada estadística, siempre hay personas esperando una respuesta.
            </div>

            <div class="mensaje-segmento">
                <strong>Modelo a Seguir:</strong><br>
                Me llevo la lección de que anticiparse, educar y guiar con el ejemplo es la herramienta más poderosa que tenemos en nuestra disciplina. ¡Gracias por ser una mentora excepcional!
            </div>

            <div class="frase-cierre">
                "Liderar con visión humana y transformar los datos en bienestar comunitario."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- VISTA: DR. MANUEL ---
elif st.session_state.seccion == 'manuel':
    st.markdown("""
        <div class="prezi-card">
            <div class="prezi-title">🔬 ¡Gracias, Dr. Manuel!</div>
            <p style="color: #38bdf8; font-weight: 600; margin-bottom: 1.2rem;">Por su guía excepcional durante esta rotación</p>
            
            <div class="mensaje-segmento">
                <strong>Vigilancia Activa en el Terreno:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la epidemiología va más allá de ver indicadores detrás de un escritorio y exige salir al campo a hacer una verdadera vigilancia activa. Me demostró que lo fundamental es poseer bases sólidas y comprender a fondo el porqué clínico y social de los eventos de salud.
            </div>

            <div class="mensaje-segmento">
                <strong>Rigor Científico y Criterio:</strong><br>
                Gracias por desafiar mi pensamiento analítico, por regalarme un enfoque clínico-epidemiológico completamente distinto y por mostrarme que el rigor científico, unido a la curiosidad constante, son las herramientas más poderosas de un médico especialista más allá de supervisiones burocráticas.
            </div>

            <div class="mensaje-segmento">
                <strong>Pensamiento Crítico:</strong><br>
                Su exigencia y mentoría me enseñaron a no dar nada por sentado, a cuestionar la evidencia con bases firmes y a buscar siempre la excelencia técnica en cada análisis.
            </div>

            <div class="frase-cierre">
                "Entender el porqué de las cosas para hacer una vigilancia activa y con rigor científico."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- VISTA: ENF. WENDY ---
elif st.session_state.seccion == 'wendy':
    st.markdown("""
        <div class="prezi-card">
            <div class="prezi-title">💉 ¡Gracias, Enf. Wendy!</div>
            <p style="color: #38bdf8; font-weight: 600; margin-bottom: 1.2rem;">Por su guía excepcional durante esta rotación</p>
            
            <div class="mensaje-segmento">
                <strong>Escenarios y Cuidado Individualizado:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la epidemiología va más allá de ver las vacunas como simples esquemas fijos que cumplir en un papel. Me enseñó a leer los diferentes escenarios operativos, a individualizar a cada paciente para brindarle una atención de calidad y a dimensionar la compleja red logística que hay detrás de la inmunización.
            </div>

            <div class="mensaje-segmento">
                <strong>Gestión de la Cadena de Frío:</strong><br>
                Gracias por guiarme desde la gestión detallada de un puesto de vacunación hasta la importancia crítica de cuidar cada parámetro de la red de frío para garantizar la efectividad del biológico. Comprendí que aplicar una vacuna trasciende la técnica mecánica: es un acto sublime de protección comunitaria.
            </div>

            <div class="mensaje-segmento">
                <strong>Pasión por la Inmunización:</strong><br>
                Gracias por ayudarme a entender las vacunas, despertar en mí un genuino interés por ellas y reafirmar mi vocación en este campo. ¡Arriba la Salud Pública!
            </div>

            <div class="frase-cierre">
                "Una vacuna va mucho más allá de una técnica; es el arte de proteger a toda una comunidad."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- VISTA: LIC. BERE ---
elif st.session_state.seccion == 'bere':
    st.markdown("""
        <div class="prezi-card">
            <div class="prezi-title">📋 ¡Gracias, Lic. Bere!</div>
            <p style="color: #38bdf8; font-weight: 600; margin-bottom: 1.2rem;">Por su guía excepcional durante esta rotación</p>
            
            <div class="mensaje-segmento">
                <strong>Población Clave y Gestión Operativa:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la epidemiología va mucho más allá de administrar insumos o cumplir con trámites administrativos; es conocer a profundidad a la población clave para aterrizar estrategias efectivas y alinear los lineamientos vigentes a la realidad operativa.
            </div>

            <div class="mensaje-segmento">
                <strong>Apertura, Soluciones y Curiosidad:</strong><br>
                Admiro enormemente su apertura al conocimiento, su disposición para enseñar sin reservas y su capacidad para no limitarse ante los obstáculos, encontrando siempre soluciones prácticas. Me demostró que la curiosidad es una virtud y que ante la duda, preguntar siempre abre la puerta al crecimiento.
            </div>

            <div class="mensaje-segmento">
                <strong>El Motor de la Operación:</strong><br>
                Gracias por enseñarme que la administración en salud va mucho más allá de la simple organización: es el pilar estratégico que sostiene toda la labor asistencial y preventiva.
            </div>

            <div class="frase-cierre">
                "La administración va más allá de la gestión: es conocer a la población y transformar los recursos en soluciones."
            </div>
        </div>
    """, unsafe_allow_html=True)

# Botón para regresar al inicio si estás dentro de una tarjeta
if st.session_state.seccion != 'inicio':
    col_back1, col_back2, col_back3 = st.columns([1, 2, 1])
    with col_back2:
        if st.button("🏠 Regresar al inicio", use_container_width=True):
            st.session_state.seccion = 'inicio'
            st.rerun()

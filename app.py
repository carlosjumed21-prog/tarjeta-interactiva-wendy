import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Agradecimientos de Rotación | Epidemiología",
    page_icon="🩺",
    layout="centered"
)

# Estilos CSS avanzados con efectos visuales dinámicos tipo Prezi, transiciones suaves y partículas
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Contenedor principal con efecto de zoom y fundido dinámico */
    .prezi-stage {
        background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
        padding: 3rem;
        border-radius: 24px;
        color: #f8fafc;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        border: 1px solid #334155;
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        animation: preziZoomIn 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        position: relative;
        overflow: hidden;
    }
    
    /* Efecto decorativo de brillo ambiental */
    .prezi-stage::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(56, 189, 248, 0.05) 0%, transparent 70%);
        pointer-events: none;
    }
    
    .prezi-title {
        font-size: 2rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #334155;
        padding-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 12px;
        animation: slideDown 0.6s ease-out;
    }
    
    /* Bloques segmentados secuenciales con retraso escalonado (Efecto Prezi de aparición en cadena) */
    .segment-box {
        background: rgba(30, 41, 59, 0.7);
        border-left: 5px solid #38bdf8;
        padding: 1.25rem 1.5rem;
        border-radius: 0 16px 16px 0;
        margin-bottom: 1.25rem;
        font-size: 1.15rem;
        color: #e2e8f0;
        line-height: 1.7;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
        animation: preziSlideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    
    .segment-1 { animation-delay: 0.1s; border-color: #38bdf8; }
    .segment-2 { animation-delay: 0.3s; border-color: #818cf8; }
    
    .prezi-quote {
        font-style: italic;
        color: #94a3b8;
        background: rgba(15, 23, 42, 0.6);
        border-left: 4px solid #34d399;
        padding: 1rem 1.25rem;
        border-radius: 0 12px 12px 0;
        margin-top: 1.5rem;
        font-size: 1.05rem;
        animation: fadeInScale 0.8s ease-out 0.7s both;
    }
    
    /* Animaciones fluidas avanzadas */
    @keyframes preziZoomIn {
        0% { opacity: 0; transform: scale(0.92) translateY(25px); }
        100% { opacity: 1; transform: scale(1) translateY(0); }
    }
    
    @keyframes preziSlideUp {
        0% { opacity: 0; transform: translateY(30px) scale(0.97); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    @keyframes slideDown {
        0% { opacity: 0; transform: translateY(-15px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInScale {
        0% { opacity: 0; transform: scale(0.95); }
        100% { opacity: 1; transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Menú lateral de navegación interactivo para elegir el mensaje directamente
st.sidebar.markdown("### 🧭 Menú de Navegación")
st.sidebar.markdown("Selecciona el espacio de agradecimiento:")

seccion = st.sidebar.radio(
    "Destinatario:",
    [
        "✨ Introducción General",
        "🩺 Dra. Elisa",
        "🔬 Dr. Manuel",
        "💉 Enf. Wendy",
        "📋 Lic. Bere"
    ],
    label_visibility="collapsed"
)

# --- 1. INTRODUCCIÓN GENERAL ---
if seccion == "✨ Introducción General":
    st.markdown("""
        <div class="prezi-stage" style="text-align: center;">
            <div class="prezi-title" style="justify-content: center; border: none;">
                ✨ Reflexiones y Agradecimientos de Rotación ✨
            </div>
            <div class="segment-box segment-1" style="border-left: none; text-align: center;">
                Un recorrido interactivo por las mentorías, los aprendizajes y las experiencias clave que marcaron un hito en mi formación como epidemiólogo.
            </div>
            <div class="segment-box segment-2" style="border-left: none; text-align: center;">
                Utiliza el menú lateral para explorar detalladamente el reconocimiento dedicado a cada pilar fundamental de esta etapa.
            </div>
            <div class="prezi-quote">
                "La salud pública no se construye solo con teoría, sino con las manos y el ejemplo de quienes nos enseñan el camino."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 2. DRA. ELISA ---
elif seccion == "🩺 Dra. Elisa":
    st.markdown("""
        <div class="prezi-stage">
            <div class="prezi-title">🩺 Dra. Elisa</div>
            <div class="segment-box segment-1">
                <strong>Visión y Liderazgo Humano:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la epidemiología va mucho más allá de números fríos y métricas en un reporte: es saber tomar decisiones con empatía, gestionar la incertidumbre y liderar un equipo con una visión profundamente humana para conseguir metas que realmente transformen la salud de la comunidad.
            </div>
            <div class="segment-box segment-2">
                <strong>Pasión por la Prevención:</strong><br>
                Gracias por impulsarme a pensar de forma estratégica, por cada consejo oportuno y por contagiarme esa pasión inquebrantable por la prevención. Gracias por enseñarme la Medicina Preventiva desde su verdadero sentido y por recordarme que, detrás de cada indicador y cada estadística, siempre hay personas esperando una respuesta.
            </div>
            <div class="prezi-quote">
                "Liderar con visión humana y transformar los datos en bienestar comunitario."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 3. DR. MANUEL ---
elif seccion == "🔬 Dr. Manuel":
    st.markdown("""
        <div class="prezi-stage">
            <div class="prezi-title">🔬 Dr. Manuel</div>
            <div class="segment-box segment-1">
                <strong>Vigilancia Activa en el Terreno:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la epidemiología va más allá de ver indicadores detrás de un escritorio y exige salir al campo a hacer una verdadera vigilancia activa. Me demostró que lo fundamental es poseer bases sólidas, comprender a fondo el porqué clínico y social de los eventos de salud.
            </div>
            <div class="segment-box segment-2">
                <strong>Rigor Científico y Criterio:</strong><br>
                Gracias por desafiar mi pensamiento analítico, por regalarme un enfoque clínico-epidemiológico completamente distinto y por mostrarme que el rigor científico, unido a la curiosidad constante, son las herramientas más poderosas de un médico especialista más allá de supervisiones burocráticas.
            </div>
            <div class="prezi-quote">
                "Entender el porqué de las cosas para hacer una vigilancia activa y con rigor científico."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. ENF. WENDY ---
elif seccion == "💉 Enf. Wendy":
    st.markdown("""
        <div class="prezi-stage">
            <div class="prezi-title">💉 Enf. Wendy</div>
            <div class="segment-box segment-1">
                <strong>Escenarios y Cuidado Individualizado:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la epidemiología va más allá de ver las vacunas como simples esquemas fijos que cumplir en un papel. Me enseñó a leer los diferentes escenarios operativos, a individualizar a cada paciente para brindarle una atención de calidad y a dimensionar la compleja red logística que hay detrás de la inmunización.
            </div>
            <div class="segment-box segment-2">
                <strong>Más Allá de la Técnica:</strong><br>
                Gracias por guiarme desde la gestión detallada de un puesto de vacunación hasta la importancia crítica de cuidar cada parámetro de la red de frío para garantizar la efectividad del biológico. Comprendí que aplicar una vacuna trasciende la técnica mecánica: es un acto sublime de protección comunitaria. ¡Arriba la Salud Pública!
            </div>
            <div class="prezi-quote">
                "Una vacuna va mucho más allá de una técnica; es el arte de proteger a toda una comunidad."
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 5. LIC. BERE ---
elif seccion == "📋 Lic. Bere":
    st.markdown("""
        <div class="prezi-stage">
            <div class="prezi-title">📋 Lic. Bere</div>
            <div class="segment-box segment-1">
                <strong>Población Clave y Gestión Operativa:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la epidemiología va mucho más allá de administrar insumos o cumplir con trámites administrativos; es conocer a profundidad a la población clave para aterrizar estrategias efectivas y alinear los lineamientos vigentes a la realidad operativa.
            </div>
            <div class="segment-box segment-2">
                <strong>Apertura, Soluciones y Curiosidad:</strong><br>
                Admiro enormemente su apertura al conocimiento, su disposición para enseñar sin reservas y su capacidad para no limitarse ante los obstáculos, encontrando siempre soluciones prácticas. Me demostró que la curiosidad es una virtud y que ante la duda, preguntar siempre abre la puerta al crecimiento. Gracias por enseñarme que la gestión en salud es el motor invisible que sostiene todo lo demás.
            </div>
            <div class="prezi-quote">
                "La administración va más allá de la gestión: es conocer a la población y transformar los recursos en soluciones."
            </div>
        </div>
    """, unsafe_allow_html=True)

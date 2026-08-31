import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="¡Gracias por la Rotación!",
    page_icon="✨",
    layout="centered"
)

# --- ESTILOS CSS (LA MAGIA VISUAL) ---
st.markdown("""
    <style>
    /* Importar fuentes de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600;700&display=swap');

    /* Estilo general de la página */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        background-image: radial-gradient(#e0e0e0 1px, transparent 1px);
        background-size: 20px 20px;
        font-family: 'Poppins', sans-serif;
    }

    /* Contenedor principal de la tarjeta con efecto 3D y sombra */
    .tarjeta-contenedor {
        background: white;
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1), 0 5px 15px rgba(0,0,0,0.07);
        border: 1px solid rgba(255,255,255,0.8);
        position: relative;
        overflow: hidden;
        animation: entradaTarjeta 0.8s ease-out;
        margin-top: 20px;
    }

    /* Efecto decorativo de confeti flotante en el fondo (usando gradientes) */
    .tarjeta-contenedor::before {
        content: '';
        position: absolute;
        top: -10px;
        left: -10px;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, rgba(255, 215, 0, 0.4) 20%, transparent 20%),
                    radial-gradient(circle, rgba(255, 105, 180, 0.4) 20%, transparent 20%),
                    radial-gradient(circle, rgba(100, 149, 237, 0.4) 20%, transparent 20%);
        background-size: 20px 20px;
        opacity: 0.5;
        z-index: 0;
    }

    /* Título Principal (Ej. "¡Gracias, Dra. Elisa!") */
    .titulo-principal {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b;
        font-size: 3.5rem;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        position: relative;
        z-index: 1;
        animation: aparecerTexto 1s ease-out;
    }

    /* Subtítulo descriptivo */
    .subtitulo {
        color: #555;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 30px;
        z-index: 1;
        position: relative;
        animation: aparecerTexto 1.2s ease-out;
    }

    /* Segmento de mensaje individual (con animación de deslizamiento) */
    .mensaje-segmento {
        background-color: #f8f9fa;
        border-left: 5px solid #4facfe;
        color: #333;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        font-size: 1.1rem;
        line-height: 1.6;
        position: relative;
        z-index: 1;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        animation: deslizarDerecha 0.5s ease-out both;
    }
    
    /* Animaciones escalonadas para los segmentos */
    .seg1 { animation-delay: 0.2s; border-color: #4facfe; }
    .seg2 { animation-delay: 0.4s; border-color: #00f2fe; }
    .seg3 { animation-delay: 0.6s; border-color: #43e97b; }

    /* Destacados en el texto (negrita con color) */
    strong { color: #333; font-weight: 600; }

    /* Frase de cierre inspiradora */
    .frase-cierre {
        text-align: center;
        font-style: italic;
        color: #888;
        margin-top: 30px;
        font-size: 1rem;
        animation: aparecerTexto 1.5s ease-out;
    }

    /* Iconos decorativos animados */
    .icono-decorativo {
        font-size: 3rem;
        text-align: center;
        display: block;
        margin: 0 auto 15px auto;
        animation: flotar 3s ease-in-out infinite;
    }

    /* --- DEFINICIÓN DE ANIMACIONES KEYFRAMES --- */
    @keyframes entradaTarjeta {
        from { opacity: 0; transform: translateY(50px) scale(0.95); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    @keyframes aparecerTexto {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes deslizarDerecha {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes flotar {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    /* Ajuste para dispositivos móviles para que el menú sea legible */
    [data-testid="stSidebarNav"] {
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL DE NAVEGACIÓN ---
st.sidebar.markdown("### 👋 Elige a quién agradecer:")
menu_seleccion = st.sidebar.radio(
    "Selecciona el destinatario:",
    [
        "✨ Introducción",
        "🩺 Dra. Elisa",
        "🔬 Dr. Manuel",
        "💉 Enf. Wendy",
        "📋 Lic. Bere"
    ],
    label_visibility="collapsed"
)

# --- LÓGICA DE VISUALIZACIÓN SEGÚN SELECCIÓN ---

# 1. INTRODUCCIÓN GENERAL
if menu_seleccion == "✨ Introducción":
    st.markdown("""
        <div class="tarjeta-contenedor">
            <span class="icono-decorativo">🎉</span>
            <h1 class="titulo-principal" style="font-size: 2.5rem;">¡Gracias por tanto!</h1>
            <p class="subtitulo">Un pequeño espacio digital para expresar mi gratitud a personas increíbles que hicieron de esta rotación una experiencia inolvidable.</p>
            <div class="mensaje-segmento seg1" style="text-align: center; border-left: none; background: #f0f2f6;">
                Durante mi paso por el área de <strong>Epidemiología</strong>, no solo aprendí teoría; me llevé lecciones de vida y mentoría invaluable. Aquí recojo un poco de lo que cada uno me enseñó. Utiliza el menú de la izquierda para leer el mensaje personalizado.
            </div>
            <p class="frase-cierre">"La educación es el arma más poderosa para cambiar el mundo." - Nelson Mandela</p>
        </div>
    """, unsafe_allow_html=True)

# 2. DRA. ELISA
elif menu_seleccion == "🩺 Dra. Elisa":
    st.markdown(f"""
        <div class="tarjeta-contenedor">
            <span class="icono-decorativo">👩‍⚕️</span>
            <h1 class="titulo-principal">¡Gracias, Dra. Elisa!</h1>
            <p class="subtitulo">Por su guía excepcional durante esta rotación</p>
            
            <div class="mensaje-segmento seg1">
                <strong>Más allá de los números:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la Epidemiología va mucho más allá de números fríos y métricas en una base de datos. Me demostró que los datos son solo el inicio para entender la realidad humana y que la disciplina requiere <strong>saber tomar decisiones cruciales</strong> bajo presión.
            </div>
            
            <div class="mensaje-segmento seg2">
                <strong>Liderazgo y Visión Integral:</strong><br>
                Aprendí de usted la importancia de <strong>liderar un equipo</strong> con empatía y dirección clara para conseguir metas ambiciosas pero alcanzables en salud pública. Usted no solo gestiona; inspira al equipo a trabajar con un propósito común.
            </div>
            
            <div class="mensaje-segmento seg3">
                <strong>La esencia de la prevención:</strong><br>
                Gracias, de corazón, por enseñarme un poquito de la <strong>Medicina Preventiva</strong> desde su enfoque más humano y efectivo. Me llevo la lección de que anticiparse y educar es la herramienta más poderosa que tenemos. ¡Gracias por ser un modelo a seguir!
            </div>
            
            <p class="frase-cierre">"La medicina cura al hombre, la medicina veterinaria cura a la humanidad." - Louis Pasteur</p>
        </div>
    """, unsafe_allow_html=True)

# 3. DR. MANUEL
elif menu_seleccion == "🔬 Dr. Manuel":
    st.markdown(f"""
        <div class="tarjeta-contenedor">
            <span class="icono-decorativo">👨‍🏫</span>
            <h1 class="titulo-principal">¡Gracias, Dr. Manuel!</h1>
            <p class="subtitulo">Por darme un enfoque distinto y riguroso de la Epidemiología</p>
            
            <div class="mensaje-segmento seg1">
                <strong>Más allá de la supervisión:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la Epidemiología va más allá de ver indicadores de forma superficial y limitarse a hacer supervisiones administrativas. Me enseñó a <strong>hacer una verdadera vigilancia activa</strong>, a estar donde ocurren los eventos y a no dar nada por sentado sin un análisis crítico.
            </div>
            
            <div class="mensaje-segmento seg2">
                <strong>Entendiendo el porqué:</strong><br>
                Usted me inculcó la necesidad de tener bases sólidas, de <strong>entender el "porqué"</strong> de las cosas y el mecanismo detrás de cada brote o fenómeno. Me enseñó a analizar la situación con profundidad, a cuestionar los hallazgos y a utilizar la evidencia científica para sustentar cada acción de salud pública.
            </div>
            
            <div class="mensaje-segmento seg3">
                <strong>Un enfoque clínico-epidemiológico:</strong><br>
                Gracias por regalarme un enfoque distinto, donde la clínica se fusiona con la visión poblacional para tomar mejores decisiones. Su mentoría ha sido clave para entender la complejidad de los problemas sanitarios.
            </div>
            
            <p class="frase-cierre">"El buen médico trata la enfermedad; el gran médico trata al paciente que tiene la enfermedad." - William Osler</p>
        </div>
    """, unsafe_allow_html=True)

# 4. ENF. WENDY
elif menu_seleccion == "💉 Enf. Wendy":
    st.markdown(f"""
        <div class="tarjeta-contenedor">
            <span class="icono-decorativo">👩‍💉</span>
            <h1 class="titulo-principal">¡Gracias, Enf. Wendy!</h1>
            <p class="subtitulo">Por mostrarme el arte detrás de la Vacunología y la Salud Pública</p>
            
            <div class="mensaje-segmento seg1">
                <strong>Vacunas más allá del esquema:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la Epidemiología va más allá de solo ver las vacunas como esquemas fijos a cumplir mecánicamente. Me enseñó a <strong>conocer los diferentes escenarios epidemiológicos</strong> y operativos, y a <strong>individualizar a cada paciente</strong> para brindarle una atención de mayor calidad, asegurando que la protección llegue a quien realmente lo necesita.
            </div>
            
            <div class="mensaje-segmento seg2">
                <strong>Gestión y Calidad Total:</strong><br>
                Gracias por enseñarme desde <strong>cómo se gestiona un puesto de vacunación</strong> de manera eficiente hasta la importancia crítica de tener en cuenta todos los parámetros logísticos. Aprendí que la red de frío, el manejo del biológico y el proceso de registro son fundamentales para que las vacunas lleguen en óptimas condiciones para su correcta aplicación.
            </div>
            
            <div class="mensaje-segmento seg3">
                <strong>Técnica y Vocación:</strong><br>
                Comprendí que una vacuna va mucho más allá de saber una técnica de inyección; es un acto de responsabilidad, empatía y protección comunitaria. Gracias por ayudarme a entender las vacunas, despertar mi interés genuino en ellas y reafirmar mi pasión por la Salud Pública.
            </div>
            
            <p class="frase-cierre">¡Arriba la Salud Pública! 💖</p>
        </div>
    """, unsafe_allow_html=True)

# 5. LIC. BERE
elif menu_seleccion == "📋 Lic. Bere":
    st.markdown(f"""
        <div class="tarjeta-contenedor">
            <span class="icono-decorativo">👩‍💼</span>
            <h1 class="titulo-principal">¡Gracias, Lic. Bere!</h1>
            <p class="subtitulo">Por enseñarme la importancia vital de la Gestión y la Administración en Salud</p>
            
            <div class="mensaje-segmento seg1">
                <strong>Administración con sentido social:</strong><br>
                Gracias por esta rotación. Usted me enseñó que la Epidemiología va mucho más allá que solo administrar insumos y llevar un control de inventarios. Me demostró que la administración eficaz es la base para conocer a la <strong>población clave</strong> y así aplicar estrategias o lineamientos vigentes de manera efectiva y oportuna.
            </div>
            
            <div class="mensaje-segmento seg2">
                <strong>Apertura y Soluciones:</strong><br>
                Admiro profundamente su <strong>apertura al conocimiento</strong> y su disposición para compartirlo. Me siento orgulloso de encontrar personas como usted, que no se limitan a un manual, que conocen su campo a profundidad y que siempre <strong>implementan soluciones</strong> prácticas para superar los desafíos diarios.
            </div>
            
            <div class="mensaje-segmento seg3">
                <strong>El valor de preguntar:</strong><br>
                Gracias por recordarme que, ante la duda, <strong>es mejor preguntar</strong> y buscar la respuesta correcta que asumir. Usted me enseñó que la administración en salud va mucho más allá de la simple organización y gestión de recursos: es el motor que permite que las estrategias de salud pública funcionen.
            </div>
            
            <p class="frase-cierre">"La gestión es hacer las cosas bien; el liderazgo es hacer las cosas correctas." - Peter Drucker</p>
        </div>
    """, unsafe_allow_html=True)


import streamlit as st
import random
import math

# ==========================================
# CONFIGURACIÓN GENERAL
# ==========================================

st.set_page_config(
    page_title="Gestalt Kids",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS
# ==========================================

st.markdown("""
<style>
.stApp {
    background: #F7FAFF;
    color: #233451;
}
section[data-testid="stSidebar"] {
    background: #E5EEFF;
}
section[data-testid="stSidebar"] * {
    color: #233451 !important;
}
h1, h2, h3, p, label {
    color: #233451;
}
div.stButton > button {
    background: #4361EE;
    color: white !important;
    border: none;
    border-radius: 14px;
    font-weight: 700;
    min-height: 44px;
}
div.stButton > button:hover {
    background: #3048C5;
    color: white !important;
}
.hero {
    background: linear-gradient(120deg, #DFE8FF, #FFE8BA);
    border-radius: 22px;
    padding: 25px;
    margin-bottom: 18px;
}
.card {
    background: white;
    border: 2px solid #DCE6FF;
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 12px;
}
.visual {
    background: white;
    border: 2px solid #DCE6FF;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    margin: 15px 0;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# INFORMACIÓN DE LAS ACTIVIDADES
# ==========================================

ACTIVIDADES = [
    "🔵 Proximidad",
    "🎨 Similitud",
    "🧩 Cierre",
    "➡️ Continuidad",
    "👀 Figura y fondo",
    "🐟 Destino común",
    "⭐ Simetría"
]

EXPLICACIONES = {
    "🔵 Proximidad":
        "Nuestro cerebro agrupa los objetos que están cerca.",

    "🎨 Similitud":
        "Agrupamos objetos que se parecen en color o forma.",

    "🧩 Cierre":
        "Nuestro cerebro completa figuras aunque falten partes.",

    "➡️ Continuidad":
        "Nuestra mirada sigue líneas y caminos continuos.",

    "👀 Figura y fondo":
        "Distinguimos los objetos principales del fondo.",

    "🐟 Destino común":
        "Agrupamos objetos que se mueven en la misma dirección.",

    "⭐ Simetría":
        "Reconocemos figuras cuyos lados se parecen como un espejo."
}

PREGUNTAS = {
    "🔵 Proximidad": (
        "¿Por qué vemos grupos de círculos?",
        [
            "Porque están cerca",
            "Porque hacen ruido",
            "Porque son invisibles"
        ],
        0
    ),
    "🎨 Similitud": (
        "¿Por qué agrupamos figuras parecidas?",
        [
            "Porque tienen características similares",
            "Porque están en movimiento",
            "Porque desaparecen"
        ],
        0
    ),
    "🧩 Cierre": (
        "¿Por qué reconocemos figuras incompletas?",
        [
            "Porque nuestro cerebro completa lo que falta",
            "Porque no tienen forma",
            "Porque cambian de tamaño"
        ],
        0
    ),
    "➡️ Continuidad": (
        "¿Qué camino sigue más fácilmente nuestra mirada?",
        [
            "El que continúa suavemente",
            "El que desaparece",
            "El que cambia sin seguir un patrón"
        ],
        0
    ),
    "👀 Figura y fondo": (
        "¿Qué hace nuestro cerebro?",
        [
            "Separa la figura principal del fondo",
            "Ignora toda la imagen",
            "Solo observa colores"
        ],
        0
    ),
    "🐟 Destino común": (
        "¿Por qué agrupamos objetos que se mueven juntos?",
        [
            "Porque siguen una dirección parecida",
            "Porque tienen diferentes tamaños",
            "Porque están quietos"
        ],
        0
    ),
    "⭐ Simetría": (
        "¿Qué significa que una figura sea simétrica?",
        [
            "Que sus lados se corresponden como un espejo",
            "Que tiene muchos colores",
            "Que está incompleta"
        ],
        0
    )
}

# ==========================================
# ESTADO
# ==========================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "🏠 Inicio"

if "completadas" not in st.session_state:
    st.session_state.completadas = set()

if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}


def navegar(pagina):
    st.session_state.pagina = pagina
    st.rerun()


def completar(actividad):
    if actividad not in st.session_state.completadas:
        st.session_state.completadas.add(actividad)
        st.balloons()


# ==========================================
# FUNCIONES PARA DIBUJAR
# ==========================================

def circulo(x, y, color="#4361EE", radio=12):
    return (
        f'<circle cx="{x}" cy="{y}" r="{radio}" '
        f'fill="{color}"/>'
    )


def mostrar_svg(svg):
    st.markdown(
        f'<div class="visual">{svg}</div>',
        unsafe_allow_html=True
    )


def ilustracion(actividad, variante=0):

    svg = (
        '<svg viewBox="0 0 600 260" '
        'xmlns="http://www.w3.org/2000/svg" '
        'style="width:100%;max-width:650px;height:auto">'
    )

    # 1. PROXIMIDAD
    if actividad == "🔵 Proximidad":
        separacion = 32 + variante * 8

        for centro in [155, 445]:
            for fila in range(3):
                for columna in range(3):
                    x = centro + (columna - 1) * separacion
                    y = 130 + (fila - 1) * separacion
                    svg += circulo(x, y)

    # 2. SIMILITUD
    elif actividad == "🎨 Similitud":
        for fila in range(3):
            for columna in range(7):
                x = 100 + columna * 65
                y = 65 + fila * 65

                if variante == 0:
                    color = (
                        "#FFB703"
                        if columna in [1, 3, 5]
                        else "#4361EE"
                    )
                else:
                    color = (
                        "#FFB703"
                        if fila == 1
                        else "#4361EE"
                    )

                svg += circulo(x, y, color, 20)

    # 3. CIERRE
    elif actividad == "🧩 Cierre":
        svg += """
        <circle cx="300" cy="130" r="80"
        fill="none" stroke="#4361EE"
        stroke-width="13"
        stroke-dasharray="100 35 100 35 100 35"/>
        """
        if variante == 1:
            svg += """
            <circle cx="300" cy="130" r="80"
            fill="none" stroke="#FFB703"
            stroke-width="5"/>
            """

    # 4. CONTINUIDAD
    elif actividad == "➡️ Continuidad":
        svg += """
        <path d="M40 210 Q300 -80 560 210"
        fill="none" stroke="#4361EE"
        stroke-width="9" stroke-linecap="round"/>
        <path d="M40 50 Q300 340 560 50"
        fill="none" stroke="#FFB703"
        stroke-width="9" stroke-linecap="round"/>
        """

    # 5. FIGURA Y FONDO
    elif actividad == "👀 Figura y fondo":
        svg += """
        <rect x="80" y="20" width="440" height="220"
        rx="18" fill="#233451"/>
        <path d="M80 20 H520 V240 H80 Z
        M215 30 C175 80 175 180 215 230
        L385 230 C425 180 425 80 385 30 Z"
        fill="#FFFFFF" fill-rule="evenodd"/>
        <path d="M265 30 C250 80 250 180 265 230
        L335 230 C350 180 350 80 335 30 Z"
        fill="#FFB703"/>
        """

    # 6. DESTINO COMÚN
    elif actividad == "🐟 Destino común":
        direcciones = (
            [1, 1, 1, -1, -1]
            if variante == 0
            else [-1, -1, 1, 1, 1]
        )

        for i, direccion in enumerate(direcciones):
            x = 80 + i * 105
            y = 120 + (i % 2) * 30
            simbolo = "➜" if direccion == 1 else "⬅"
            color = (
                "#4361EE" if direccion == 1 else "#FFB703"
            )

            svg += (
                f'<text x="{x}" y="{y}" '
                f'font-size="60" fill="{color}">'
                f'{simbolo}</text>'
            )

    # 7. SIMETRÍA
    elif actividad == "⭐ Simetría":
        svg += """
        <line x1="300" y1="20" x2="300" y2="240"
        stroke="#233451" stroke-width="3"
        stroke-dasharray="8 8"/>
        <path d="M300 35 L220 90 L250 150
        L200 210 L300 230 Z"
        fill="#4361EE"/>
        """
        if variante == 1:
            svg += """
            <path d="M300 35 L380 90 L350 150
            L400 210 L300 230 Z"
            fill="#FFB703"/>
            """

    svg += "</svg>"
    mostrar_svg(svg)


# ==========================================
# MENÚ LATERAL
# ==========================================

with st.sidebar:
    st.title("🧠 Gestalt Kids")
    st.write("¡Aprende jugando!")

    st.markdown("### 🎮 Elige una actividad")

    opciones = ["🏠 Inicio"] + ACTIVIDADES

    seleccion = st.radio(
        "Navegación",
        opciones,
        index=opciones.index(st.session_state.pagina),
        label_visibility="collapsed"
    )

    if seleccion != st.session_state.pagina:
        navegar(seleccion)

    st.divider()

    progreso = len(st.session_state.completadas)
    st.progress(progreso / 7)
    st.markdown(f"### ⭐ {progreso} de 7 estrellas")
    st.caption("¡Completa los siete retos!")

    if st.button("🔄 Reiniciar progreso"):
        st.session_state.completadas = set()
        st.session_state.respuestas = {}
        navegar("🏠 Inicio")


# ==========================================
# PANTALLA DE INICIO
# ==========================================

if st.session_state.pagina == "🏠 Inicio":

    st.markdown("""
    <div class="hero">
        <h1>🌈 ¡Bienvenido a Gestalt Kids!</h1>
        <p>
        Tu cerebro es un detective.
        Descubre formas, grupos y patrones
        en todo lo que ves.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.header("🧠 ¿Qué es la Gestalt?")

    st.write(
        "La Gestalt nos ayuda a entender cómo "
        "nuestro cerebro organiza lo que vemos."
    )

    st.info(
        "👈 Elige una actividad en el menú, "
        "juega y gana estrellas."
    )

    st.subheader("🎮 Tus siete aventuras")

    for inicio in range(0, len(ACTIVIDADES), 2):
        columnas = st.columns(2)

        for j, columna in enumerate(columnas):
            indice = inicio + j

            if indice >= len(ACTIVIDADES):
                continue

            actividad = ACTIVIDADES[indice]

            with columna:
                estado = (
                    "⭐ ¡Completado!"
                    if actividad in st.session_state.completadas
                    else "🎮 Listo para jugar"
                )

                st.markdown(
                    f"""
                    <div class="card">
                        <h3>{actividad}</h3>
                        <p>{EXPLICACIONES[actividad]}</p>
                        <strong>{estado}</strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"Explorar {actividad}",
                    key=f"inicio_{indice}"
                ):
                    navegar(actividad)


# ==========================================
# PANTALLAS DE ACTIVIDADES
# ==========================================

else:
    actividad = st.session_state.pagina
    indice = ACTIVIDADES.index(actividad)

    st.title(actividad)

    st.markdown(
        f"""
        <div class="hero">
            <h3>🧠 Descubre el principio</h3>
            <p>{EXPLICACIONES[actividad]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("👀 Observa y experimenta")

    if actividad == "🔵 Proximidad":
        variante = st.slider(
            "Cambia la distancia entre los círculos",
            min_value=0,
            max_value=5,
            value=0,
            key=f"slider_{indice}"
        )
    else:
        variante = st.slider(
            "Cambia el ejemplo",
            min_value=0,
            max_value=1,
            value=0,
            key=f"slider_{indice}"
        )

    ilustracion(actividad, variante)

    st.caption(
        "Mueve el control para descubrir "
        "cómo cambia lo que percibes."
    )

    st.divider()
    st.subheader("🎯 ¡Tu reto!")

    pregunta, opciones, correcta = PREGUNTAS[actividad]

    st.write(pregunta)

    respuesta = st.radio(
        "Selecciona tu respuesta:",
        opciones,
        index=None,
        key=f"pregunta_{indice}"
    )

    if st.button(
        "✨ Comprobar respuesta",
        key=f"comprobar_{indice}"
    ):
        if respuesta is None:
            st.warning("Selecciona una respuesta primero.")
        elif respuesta == opciones[correcta]:
            completar(actividad)
            st.session_state.respuestas[actividad] = True
        else:
            st.session_state.respuestas[actividad] = False

    if actividad in st.session_state.respuestas:
        if st.session_state.respuestas[actividad]:
            st.success(
                "🎉 ¡Excelente! Ganaste una estrella."
            )
        else:
            st.error(
                "¡Buen intento! Observa y vuelve a probar."
            )

    st.divider()
    columna1, columna2 = st.columns(2)

    with columna1:
        if st.button("🏠 Volver al inicio"):
            navegar("🏠 Inicio")

    with columna2:
        if indice < len(ACTIVIDADES) - 1:
            siguiente = ACTIVIDADES[indice + 1]

            if st.button("➡️ Siguiente actividad"):
                navegar(siguiente)
        else:
            if st.button("🏆 Ver mis estrellas"):
                navegar("🏠 Inicio")


# ==========================================
# FELICITACIÓN FINAL
# ==========================================

if len(st.session_state.completadas) == 7:
    st.success(
        "🏆 ¡FELICIDADES! Completaste las siete "
        "actividades Gestalt."
    )
    st.markdown(
        "### 🌟 ¡Ahora eres un detective visual!"
    )

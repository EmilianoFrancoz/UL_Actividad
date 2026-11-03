
import streamlit as st
import random
import math

st.set_page_config(
    page_title="Gestalt Kids",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

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
    padding: 0.6rem 1.2rem;
    font-weight: 700;
}

div.stButton > button:hover {
    background: #3048C5;
    color: white !important;
}

.hero {
    background: linear-gradient(120deg, #DFE8FF, #FFE8BA);
    border-radius: 22px;
    padding: 28px;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 22px;
    border: 2px solid #DCE6FF;
    border-radius: 18px;
    margin-bottom: 15px;
}

.visual {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 2px solid #DCE6FF;
    text-align: center;
    margin: 15px 0;
}

.small-note {
    color: #526581;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ACTIVIDADES
# --------------------------------------------------

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
        "Nuestro cerebro agrupa las cosas que están cerca unas de otras.",

    "🎨 Similitud":
        "Nuestro cerebro reúne objetos que se parecen en color, forma o tamaño.",

    "🧩 Cierre":
        "Aunque falten partes de una figura, nuestro cerebro intenta completarla.",

    "➡️ Continuidad":
        "Preferimos seguir caminos y líneas que parecen continuar suavemente.",

    "👀 Figura y fondo":
        "Nuestro cerebro separa lo que estamos mirando del fondo que lo rodea.",

    "🐟 Destino común":
        "Los objetos que se mueven en la misma dirección parecen formar un grupo.",

    "⭐ Simetría":
        "Reconocemos fácilmente las figuras cuyos lados se parecen como un espejo."
}

PREGUNTAS = {
    "🔵 Proximidad": (
        "¿Por qué vemos grupos de círculos?",
        [
            "Porque están cerca unos de otros",
            "Porque todos se mueven",
            "Porque son invisibles"
        ],
        0
    ),

    "🎨 Similitud": (
        "¿Qué hace que agrupemos las figuras?",
        [
            "Su posición en la pantalla",
            "Su parecido en color o forma",
            "El sonido que producen"
        ],
        1
    ),

    "🧩 Cierre": (
        "¿Por qué reconocemos una figura incompleta?",
        [
            "Porque nuestro cerebro completa lo que falta",
            "Porque la figura se mueve",
            "Porque no tiene ningún significado"
        ],
        0
    ),

    "➡️ Continuidad": (
        "¿Qué camino suele seguir nuestra mirada?",
        [
            "El que cambia bruscamente",
            "El que parece continuar suavemente",
            "Ninguno"
        ],
        1
    ),

    "👀 Figura y fondo": (
        "¿Qué hace nuestro cerebro al observar una imagen?",
        [
            "Ignora todos los objetos",
            "Separa la figura principal del fondo",
            "Ve únicamente colores"
        ],
        1
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
            "Que tiene muchos colores",
            "Que está incompleta",
            "Que sus lados se corresponden como en un espejo"
        ],
        2
    )
}


# --------------------------------------------------
# ESTADO DE LA APLICACIÓN
# --------------------------------------------------

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


# --------------------------------------------------
# ILUSTRACIONES SVG
# --------------------------------------------------

def mostrar_svg(contenido):
    st.markdown(
        f'<div class="visual">{contenido}</div>',
        unsafe_allow_html=True
    )


def circulo(x, y, color="#4361EE", radio=15):
    return (
        f'<circle cx="{x}" cy="{y}" r="{radio}" '
        f'fill="{color}"/>'
    )


def ilustracion(actividad, variante=0):

    svg = (
        '<svg viewBox="0 0 600 260" '
        'xmlns="http://www.w3.org/2000/svg" '
        'style="width:100%;max-width:650px;height:auto">'
    )

    if actividad == "🔵 Proximidad":
        separacion = 18 if variante == 0 else 27

        for grupo in [130, 430]:
            for fila in range(3):
                for columna in range(3):
                    x = grupo + columna * separacion
                    y = 80 + fila * separacion
                    svg += circulo(x, y)

    elif actividad == "🎨 Similitud":
        for fila in range(3):
            for columna in range(7):
                x = 100 + columna * 65
                y = 65 + fila * 65
                color = (
                    "#FFB703"
                    if columna in [1, 3, 5]
                    else "#4361EE"
                )

                if variante == 1:
                    color = (
                        "#FFB703"
                        if fila == 1
                        else "#4361EE"
                    )

                svg += circulo(x, y, color, 20)

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

    elif actividad == "➡️ Continuidad":
        svg += """
        <path d="M40 210 Q300 -80 560 210"
        fill="none" stroke="#4361EE"
        stroke-width="9" stroke-linecap="round"/>

        <path d="M40 50 Q300 340 560 50"
        fill="none" stroke="#FFB703"
        stroke-width="9" stroke-linecap="round"/>
        """

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
            color = "#4361EE" if direccion == 1 else "#FFB703"

            svg += (
                f'<text x="{x}" y="{y}" '
                f'font-size="60" fill="{color}">'
                f'{simbolo}</text>'
            )

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


# --------------------------------------------------
# MENÚ LATERAL
# --------------------------------------------------

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


# --------------------------------------------------
# PANTALLA DE INICIO
# --------------------------------------------------

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
        "La Gestalt nos ayuda a entender cómo nuestro "
        "cerebro organiza lo que vemos. "
        "¡A veces encontramos figuras y grupos "
        "sin darnos cuenta!"
    )

    st.info(
        "👈 Elige una actividad en el menú de la izquierda. "
        "Observa, juega y gana estrellas."
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


# --------------------------------------------------
# PANTALLAS DE ACTIVIDADES
# --------------------------------------------------

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
                "🎉 ¡Excelente! Ganaste una estrella. "
                "¡Tu cerebro es increíble!"
            )
        else:
            st.error(
                "¡Buen intento! Observa otra vez "
                "y vuelve a probar."
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


# --------------------------------------------------
# MENSAJE FINAL
# --------------------------------------------------

if len(st.session_state.completadas) == 7:

    st.success(
        "🏆 ¡FELICIDADES! "
        "Completaste las siete actividades Gestalt."
    )

    st.markdown(
        "### 🌟 ¡Ahora eres un detective visual!"
    )


import streamlit as st
import random
import html

# ==========================================
# CONFIGURACIÓN
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

st.html("""
<style>
.stApp {
    background: #F7FAFF;
    color: #233451;
}

section[data-testid="stSidebar"] {
    background: #E5EEFF;
}

h1, h2, h3 {
    color: #233451;
}

div.stButton > button {
    background-color: #4361EE;
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    min-height: 45px;
}

div.stButton > button:hover {
    background-color: #3048C5;
    color: white;
}

.hero {
    background: linear-gradient(
        120deg,
        #DFE8FF,
        #FFE8BA
    );
    border-radius: 22px;
    padding: 28px;
    margin-bottom: 20px;
    color: #233451;
}

.hero h1,
.hero h3,
.hero p {
    color: #233451;
}

.card {
    background: white;
    border: 2px solid #DCE6FF;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 12px;
    color: #233451;
}

.card h3,
.card p {
    color: #233451;
}

.visual {
    background: white;
    border: 2px solid #DCE6FF;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    margin: 16px 0;
}

.visual svg {
    width: 100%;
    max-width: 650px;
    height: auto;
    display: block;
    margin: auto;
}
</style>
""")

# ==========================================
# ACTIVIDADES
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
            "Porque desaparecen",
            "Porque producen sonidos"
        ],
        0
    ),

    "🧩 Cierre": (
        "¿Por qué reconocemos figuras incompletas?",
        [
            "Porque nuestro cerebro completa lo que falta",
            "Porque cambian de tamaño",
            "Porque no tienen forma"
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
# ESTADO DE LA APLICACIÓN
# ==========================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "🏠 Inicio"

if "completadas" not in st.session_state:
    st.session_state.completadas = set()

if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

if "nivel_similitud" not in st.session_state:
    st.session_state.nivel_similitud = 0

if "patron_similitud" not in st.session_state:
    st.session_state.patron_similitud = []

if "resultado_similitud" not in st.session_state:
    st.session_state.resultado_similitud = None


def navegar(pagina):
    st.session_state.pagina = pagina
    st.rerun()


def completar(actividad):
    if actividad not in st.session_state.completadas:
        st.session_state.completadas.add(actividad)
        st.balloons()


# ==========================================
# DIBUJOS SVG
# ==========================================

def circulo(x, y, color="#4361EE", radio=12):
    return (
        f'<circle cx="{x}" cy="{y}" '
        f'r="{radio}" fill="{color}"/>'
    )


def mostrar_svg(svg):
    st.html(
        f'<div class="visual">{svg}</div>'
    )


def ilustracion(actividad, variante=0):

    svg = """
    <svg viewBox="0 0 600 260"
    xmlns="http://www.w3.org/2000/svg"
    style="width:100%;max-width:650px;height:auto">
    """

    # ======================================
    # 1. PROXIMIDAD
    # ======================================

    if actividad == "🔵 Proximidad":

        separacion = 32 + variante * 8

        for centro in [155, 445]:
            for fila in range(3):
                for columna in range(3):

                    x = centro + (columna - 1) * separacion
                    y = 130 + (fila - 1) * separacion

                    svg += circulo(x, y)

    # ======================================
    # 2. SIMILITUD
    # ======================================

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

    # ======================================
    # 3. CIERRE
    # ======================================

    elif actividad == "🧩 Cierre":

        svg += """
        <circle
            cx="300"
            cy="130"
            r="80"
            fill="none"
            stroke="#4361EE"
            stroke-width="13"
            stroke-dasharray="100 35 100 35 100 35"
        />
        """

        if variante == 1:
            svg += """
            <circle
                cx="300"
                cy="130"
                r="80"
                fill="none"
                stroke="#FFB703"
                stroke-width="5"
            />
            """

    # ======================================
    # 4. CONTINUIDAD
    # ======================================

    elif actividad == "➡️ Continuidad":

        svg += """
        <path
            d="M40 210 Q300 -80 560 210"
            fill="none"
            stroke="#4361EE"
            stroke-width="9"
            stroke-linecap="round"
        />

        <path
            d="M40 50 Q300 340 560 50"
            fill="none"
            stroke="#FFB703"
            stroke-width="9"
            stroke-linecap="round"
        />
        """

        if variante == 1:
            svg += """
            <circle cx="300" cy="130" r="13"
            fill="#EF476F"/>
            """

    # ======================================
    # 5. FIGURA Y FONDO
    # ======================================

    elif actividad == "👀 Figura y fondo":

        fondo = "#233451" if variante == 0 else "#4361EE"
        figura = "#FFFFFF" if variante == 0 else "#FFB703"

        svg += f"""
        <rect
            x="80"
            y="20"
            width="440"
            height="220"
            rx="18"
            fill="{fondo}"
        />

        <path
            d="M300 35
               C245 35 220 75 220 110
               C220 155 250 180 250 225
               L350 225
               C350 180 380 155 380 110
               C380 75 355 35 300 35 Z"
            fill="{figura}"
        />
        """

    # ======================================
    # 6. DESTINO COMÚN
    # ======================================

    elif actividad == "🐟 Destino común":

        direcciones = (
            [1, 1, 1, -1, -1]
            if variante == 0
            else [-1, -1, 1, 1, 1]
        )

        for i, direccion in enumerate(direcciones):

            x = 80 + i * 105
            y = 120 + (i % 2) * 30

            if direccion == 1:
                color = "#4361EE"
                simbolo = "➜"
            else:
                color = "#FFB703"
                simbolo = "⬅"

            svg += (
                f'<text x="{x}" y="{y}" '
                f'font-size="60" fill="{color}">'
                f'{simbolo}</text>'
            )

    # ======================================
    # 7. SIMETRÍA CORREGIDA
    # ======================================

    elif actividad == "⭐ Simetría":

        svg += """
        <line
            x1="300"
            y1="20"
            x2="300"
            y2="240"
            stroke="#233451"
            stroke-width="3"
            stroke-dasharray="8 8"
        />

        <path
            d="M300 35
               L220 90
               L250 150
               L200 210
               L300 230 Z"
            fill="#4361EE"
        />
        """

        if variante == 1:
            svg += """
            <path
                d="M300 35
                   L380 90
                   L350 150
                   L400 210
                   L300 230 Z"
                fill="#FFB703"
            />
            """

    svg += "</svg>"

    mostrar_svg(svg)


# ==========================================
# JUEGO EXTRA DE SIMILITUD
# ==========================================

COLORES = {
    "Azul": "#4361EE",
    "Rojo": "#EF476F",
    "Amarillo": "#FFB703",
    "Verde": "#06D6A0"
}

RETOS_SIMILITUD = [
    ("Azul", 5),
    ("Rojo", 6),
    ("Verde", 4)
]


def generar_patron(nivel):

    objetivo, cantidad = RETOS_SIMILITUD[nivel]

    patron = [objetivo] * cantidad
    otros = [c for c in COLORES if c != objetivo]

    for _ in range(15 - cantidad):
        patron.append(random.choice(otros))

    random.shuffle(patron)

    return patron


def mostrar_patron(patron):

    svg = """
    <svg viewBox="0 0 500 320"
    xmlns="http://www.w3.org/2000/svg"
    style="width:100%;max-width:500px;height:auto">
    """

    for i, color in enumerate(patron):

        fila = i // 5
        columna = i % 5

        x = 70 + columna * 90
        y = 65 + fila * 90

        svg += circulo(
            x,
            y,
            COLORES[color],
            25
        )

    svg += "</svg>"

    mostrar_svg(svg)


def actividad_similitud():

    st.title("🎨 Similitud")

    st.markdown("""
    <div class="hero">
        <h3>🧠 ¡Encuentra los objetos parecidos!</h3>
        <p>
        Nuestro cerebro agrupa objetos que tienen
        características parecidas, como el color.
        </p>
    </div>
    """, unsafe_allow_html=True)

    nivel = st.session_state.nivel_similitud

    if nivel >= len(RETOS_SIMILITUD):

        st.success(
            "🏆 ¡Completaste los tres retos de Similitud!"
        )

        st.write(
            "Aprendiste que los objetos pueden formar "
            "grupos porque se parecen."
        )

        if st.button("🔄 Volver a jugar"):
            st.session_state.nivel_similitud = 0
            st.session_state.patron_similitud = []
            st.session_state.resultado_similitud = None
            st.rerun()

        if st.button("➡️ Ir a Cierre"):
            navegar("🧩 Cierre")

        return

    objetivo, cantidad = RETOS_SIMILITUD[nivel]

    if not st.session_state.patron_similitud:
        st.session_state.patron_similitud = generar_patron(nivel)

    st.progress(nivel / 3)

    st.subheader(f"🎯 Reto {nivel + 1} de 3")

    st.write(
        f"¿Cuántos círculos de color "
        f"**{objetivo.lower()}** encuentras?"
    )

    mostrar_patron(
        st.session_state.patron_similitud
    )

    respuesta = st.radio(
        "Selecciona tu respuesta:",
        ["4", "5", "6", "7"],
        index=None,
        key=f"respuesta_similitud_{nivel}"
    )

    if st.button(
        "✨ Comprobar respuesta",
        key=f"comprobar_similitud_{nivel}"
    ):

        if respuesta is None:
            st.warning("Primero selecciona una respuesta.")

        elif int(respuesta) == cantidad:
            st.session_state.resultado_similitud = True

        else:
            st.session_state.resultado_similitud = False

    resultado = st.session_state.resultado_similitud

    if resultado is True:

        st.success(
            f"🎉 ¡Correcto! Encontraste {cantidad} "
            f"círculos {objetivo.lower()}."
        )

        st.info(
            "🧠 Tu cerebro reconoce objetos parecidos "
            "aunque estén mezclados."
        )

        if st.button("➡️ Siguiente reto"):

            if nivel == 2:
                completar("🎨 Similitud")

            st.session_state.nivel_similitud += 1
            st.session_state.patron_similitud = []
            st.session_state.resultado_similitud = None

            st.rerun()

    elif resultado is False:

        st.error(
            "¡Buen intento! Cuenta solamente "
            f"los círculos {objetivo.lower()}."
        )

    st.divider()

    if st.button("🏠 Volver al inicio"):
        navegar("🏠 Inicio")


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

    st.markdown(
        f"### ⭐ {progreso} de 7 estrellas"
    )

    st.caption("¡Completa los siete retos!")

    if st.button("🔄 Reiniciar progreso"):

        st.session_state.completadas = set()
        st.session_state.respuestas = {}

        st.session_state.nivel_similitud = 0
        st.session_state.patron_similitud = []
        st.session_state.resultado_similitud = None

        navegar("🏠 Inicio")


# ==========================================
# PANTALLA DE INICIO
# ==========================================

if st.session_state.pagina == "🏠 Inicio":

    st.html("""
    <div class="hero">
        <h1>🌈 ¡Bienvenido a Gestalt Kids!</h1>
        <p>
        Tu cerebro es un detective.
        Descubre formas, grupos y patrones
        en todo lo que ves.
        </p>
    </div>
    """)

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

                st.html(
                    f"""
                    <div class="card">
                        <h3>{html.escape(actividad)}</h3>
                        <p>{html.escape(EXPLICACIONES[actividad])}</p>
                        <strong>{estado}</strong>
                    </div>
                    """
                )

                if st.button(
                    f"Explorar {actividad}",
                    key=f"inicio_{indice}"
                ):
                    navegar(actividad)


# ==========================================
# ACTIVIDAD DE SIMILITUD
# ==========================================

elif st.session_state.pagina == "🎨 Similitud":

    actividad_similitud()


# ==========================================
# RESTO DE ACTIVIDADES
# ==========================================

else:

    actividad = st.session_state.pagina

    indice = ACTIVIDADES.index(actividad)

    st.title(actividad)

    st.html(
        f"""
        <div class="hero">
            <h3>🧠 Descubre el principio</h3>
            <p>{html.escape(EXPLICACIONES[actividad])}</p>
        </div>
        """
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

            st.warning(
                "Selecciona una respuesta primero."
            )

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

import streamlit as st
import random

st.set_page_config(page_title='Gestalt Kids', page_icon='🧠', layout='wide')

CSS = '''<style>
.stApp {background:linear-gradient(135deg,#f7f9ff,#fff8ed);color:#24304b}
.block-container {padding-top:1.5rem;max-width:1100px}
h1,h2,h3 {color:#28336a}
[data-testid="stSidebar"] {background:#eaf0ff}
.kid-card {background:white;border:2px solid #dfe7ff;border-radius:20px;padding:22px;margin:12px 0;box-shadow:0 6px 18px #23336912}
.hero {background:linear-gradient(120deg,#dce6ff,#ffe7bc);padding:25px;border-radius:24px}
.big-emoji {font-size:64px;text-align:center}
.small-note {color:#4b5874;font-size:1.05rem}
</style>'''
st.markdown(CSS, unsafe_allow_html=True)

LESSONS = [
 ('🔵','Proximidad','Las cosas que están cerquita parecen formar un equipo.','Mira los grupos de puntos. ¿Cuántos grupos ves?', 'Dos grupos', ['Un grupo','Dos grupos','Cinco grupos'], 'Dos grupos', 'Los puntos están separados en dos conjuntos, ¡y tu cerebro los agrupa!'),
 ('🎨','Similitud','Agrupamos las cosas que se parecen en color, forma o tamaño.','¿Qué figuras forman un equipo por su forma?', 'Los círculos', ['Los círculos','Todas por igual','Ninguna'], 'Los círculos', 'Aunque estén mezclados, los círculos se parecen entre sí.'),
 ('🧩','Cierre','Tu cerebro completa las partes que faltan de una figura.','Aunque le falte un pedacito, ¿qué figura reconoces?', 'Un círculo', ['Un triángulo','Un círculo','Un cuadrado'], 'Un círculo', '¡Tu cerebro completa el círculo aunque no esté cerrado!'),
 ('➡️','Continuidad','Preferimos seguir caminos suaves y continuos.','¿Cuál camino parece continuar sin doblarse?', 'El camino recto', ['El camino recto','El camino en zigzag','Ninguno'], 'El camino recto', 'Tu mirada sigue con facilidad las líneas continuas.'),
 ('👀','Figura y fondo','Podemos distinguir lo que miramos del fondo que lo rodea.','¿Qué figura destaca sobre el fondo?', 'La estrella', ['El fondo','La estrella','Las dos igual'], 'La estrella', 'La estrella es la figura y el rectángulo claro es el fondo.'),
 ('🤝','Destino común','Los objetos que se mueven en la misma dirección parecen pertenecer al mismo grupo.','¿Qué flechas parecen ir juntas?', 'Las que apuntan a la derecha', ['Las que apuntan a la derecha','Todas','Ninguna'], 'Las que apuntan a la derecha', 'Cuando varias cosas van hacia el mismo lado, las vemos como equipo.'),
 ('⭐','Simetría','Las formas equilibradas a ambos lados de un eje nos parecen relacionadas.','¿Qué dibujo es simétrico?', 'La mariposa', ['La mariposa','La forma irregular','Ambos'], 'La mariposa', 'Los dos lados de la mariposa se parecen como en un espejo.'),
]

def visual(idx):
    if idx == 0:
        return '''<svg viewBox="0 0 600 210" width="100%" role="img" aria-label="Dos grupos de cinco puntos"><g fill="#5378e8">''' + ''.join(f'<circle cx="{95+(j%3)*36+(i*260)}" cy="{65+(j//3)*48}" r="13"/>' for i in range(2) for j in range(6)) + '</g></svg>'
    if idx == 1:
        shapes = ''.join(f'<circle cx="{95+i*90}" cy="75" r="22" fill="#5378e8"/>' if i%2==0 else f'<rect x="{72+i*90}" y="52" width="46" height="46" rx="5" fill="#f5aa38"/>' for i in range(5))
        return f'<svg viewBox="0 0 600 160" width="100%" role="img" aria-label="Círculos azules y cuadrados amarillos alternados">{shapes}</svg>'
    if idx == 2:
        return '<svg viewBox="0 0 600 210" width="100%" role="img" aria-label="Círculo incompleto"><circle cx="300" cy="103" r="68" fill="none" stroke="#5378e8" stroke-width="14" stroke-dasharray="350 80" stroke-linecap="round"/></svg>'
    if idx == 3:
        return '<svg viewBox="0 0 600 210" width="100%" role="img" aria-label="Camino recto y camino zigzag"><path d="M40 60 H550" stroke="#5378e8" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M40 150 L140 105 L240 185 L340 105 L440 185 L550 145" stroke="#f5aa38" stroke-width="10" fill="none" stroke-linejoin="round"/></svg>'
    if idx == 4:
        return '<svg viewBox="0 0 600 210" width="100%" role="img" aria-label="Estrella morada sobre fondo claro"><rect x="50" y="15" width="500" height="180" rx="18" fill="#dfe9ff"/><polygon points="300,25 321,80 380,80 333,117 351,176 300,140 249,176 267,117 220,80 279,80" fill="#8058d8"/></svg>'
    if idx == 5:
        return '<svg viewBox="0 0 600 210" width="100%" role="img" aria-label="Cuatro flechas hacia la derecha y una hacia arriba"><g font-size="65" font-weight="bold"><text x="80" y="85" fill="#5378e8">→ → →</text><text x="230" y="175" fill="#f5aa38">↑</text></g></svg>'
    return '<svg viewBox="0 0 600 210" width="100%" role="img" aria-label="Mariposa simétrica"><line x1="300" y1="15" x2="300" y2="200" stroke="#888" stroke-dasharray="6 6"/><ellipse cx="240" cy="77" rx="65" ry="48" transform="rotate(25 240 77)" fill="#8058d8"/><ellipse cx="360" cy="77" rx="65" ry="48" transform="rotate(-25 360 77)" fill="#8058d8"/><ellipse cx="257" cy="146" rx="40" ry="32" fill="#f5aa38"/><ellipse cx="343" cy="146" rx="40" ry="32" fill="#f5aa38"/><rect x="293" y="47" width="14" height="116" rx="7" fill="#26356c"/></svg>'

if 'done' not in st.session_state: st.session_state.done = set()
if 'selected' not in st.session_state: st.session_state.selected = '🏠 Inicio'

st.sidebar.title('🧠 Gestalt Kids')
st.sidebar.caption('¡Aprende jugando!')
items = ['🏠 Inicio'] + [f'{x[0]} {x[1]}' for x in LESSONS]
choice = st.sidebar.radio('Elige una actividad:', items, index=items.index(st.session_state.selected) if st.session_state.selected in items else 0)
st.session_state.selected = choice
st.sidebar.divider()
st.sidebar.progress(len(st.session_state.done)/7)
st.sidebar.write(f'⭐ {len(st.session_state.done)} de 7 retos completados')
st.sidebar.caption('Tu progreso se conserva mientras dura esta sesión.')

if choice == '🏠 Inicio':
    st.markdown('<div class="hero"><h1>🌈 ¡Bienvenido a Gestalt Kids!</h1><p style="font-size:21px">Tu cerebro es un detective: descubre formas, grupos y patrones en todo lo que ves.</p></div>', unsafe_allow_html=True)
    st.subheader('¿Qué es la Gestalt?')
    st.write('La Gestalt es una forma de explicar cómo nuestro cerebro organiza lo que vemos. ¡A veces encontramos figuras y grupos sin darnos cuenta!')
    st.info('👈 Abre el menú de la izquierda y elige uno de los siete retos. Observa, responde y gana una estrella.')
    cols = st.columns(2)
    for i, (emoji,name,*_) in enumerate(LESSONS):
        with cols[i%2]:
            st.markdown(f'<div class="kid-card"><h3>{emoji} {name}</h3><p>{"⭐ ¡Completado!" if i in st.session_state.done else "🎮 Listo para jugar"}</p></div>', unsafe_allow_html=True)
            if st.button(f'Explorar {name}', key=f'go_{i}'):
                st.session_state.selected = items[i+1]
                st.rerun()
else:
    idx = items.index(choice)-1
    emoji,name,explanation,question,_,options,correct,feedback = LESSONS[idx]
    st.title(f'{emoji} Actividad {idx+1}: {name}')
    st.markdown(f'<div class="kid-card"><h3>💡 Descubre el principio</h3><p style="font-size:21px">{explanation}</p></div>', unsafe_allow_html=True)
    st.markdown(visual(idx), unsafe_allow_html=True)
    st.subheader('🎯 Tu reto')
    st.write(question)
    answer = st.radio('Elige una respuesta:', options, index=None, key=f'answer_{idx}')
    if st.button('✨ Comprobar respuesta', key=f'check_{idx}', type='primary'):
        if answer is None: st.warning('Primero elige una respuesta 😊')
        elif answer == correct:
            st.session_state.done.add(idx)
            st.success(f'🎉 ¡Correcto! {feedback} Ganaste una estrella ⭐')
            st.balloons()
        else: st.error('¡Buen intento! Mira la imagen otra vez y prueba de nuevo. 💪')
    if idx in st.session_state.done: st.caption('⭐ Actividad completada en esta sesión.')
    st.divider()
    st.caption('Consejo: habla con un amigo o familiar sobre dónde ves este principio en tu vida diaria.')

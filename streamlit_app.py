import streamlit as st
import random
import matplotlib.pyplot as plt

# Título de la aplicación
def slide_intro():
    st.title("📰 La Construcción de las Esferas Públicas y el Estado Moderno")
    st.header("🗣️ Introducción")
    st.write("""
    Bienvenidos a esta presentación sobre el impacto de la **comunicación** en la construcción de los **Estados modernos** y sus **esferas públicas**.
    
    Exploraremos cómo los **periódicos**, **discursos políticos** y otras formas de comunicación jugaron un papel crucial en la creación de la **identidad nacional** y la **participación pública** durante los siglos XVIII y XIX.
    
    Temas que cubriremos:
    - La **comunicación en la construcción del Estado Nación**
    - El **rol de los periódicos** en la esfera pública
    - La **participación ciudadana** y los **discursos políticos**
    """)

# Diapositiva 2: La Comunicación en la Construcción del Estado Nación
def slide_comunicacion_estado():
    st.header("📜 La Comunicación en la Construcción del Estado Nación")
    st.write("""
    En el siglo XVIII, los **periódicos** y **discursos políticos** fueron esenciales para la construcción del **Estado Nación**.
    
    Los periódicos ayudaron a difundir ideas de **identidad nacional** y **unificación**. Al leer los primeros **diarios**, la gente podía informarse sobre las decisiones políticas, el estado de la guerra, las políticas económicas y los discursos que construían una narrativa común.
    
    ¿Qué tema te gustaría explorar en el periódico de hoy?
    """)

    tema = st.selectbox(
        "Selecciona un tema:",
        ["Unidad Nacional", "Reformas Políticas", "Guerra y Conflicto", "Economía y Comercio"]
    )

    if tema == "Unidad Nacional":
        st.write("El periódico de hoy promueve la **unidad nacional**, destacando la importancia de formar una **nación unida** bajo un solo gobierno central.")
    elif tema == "Reformas Políticas":
        st.write("Hoy, el periódico discute las **reformas políticas** para modernizar el gobierno y dar a los ciudadanos un **rol más activo**.")
    elif tema == "Guerra y Conflicto":
        st.write("El periódico de hoy se enfoca en las **guerras** que consolidan la autoridad del Estado, mostrando cómo el conflicto ayuda a unir al pueblo bajo una causa común.")
    else:
        st.write("En este número del periódico, se habla de las **reformas económicas** necesarias para la **prosperidad** del Estado Nación.")

# Diapositiva 3: La Prensa y los Primeros Periódicos
def slide_prensa_periodicos():
    st.header("📰 La Prensa y los Primeros Periódicos")
    st.write("""
    La prensa jugó un papel clave en la **construcción de la esfera pública**. Los periódicos permitieron a los ciudadanos acceder a información sobre el gobierno, las guerras y los debates políticos.
    
    Vamos a simular cómo el contenido de un periódico podría estar distribuido entre varias secciones que fomentan la **unidad nacional**.
    """)

    # Crear un gráfico de barras representando las secciones del periódico
    secciones = ['Unidad Nacional', 'Reformas Políticas', 'Guerra y Conflicto', 'Economía']
    cantidad = [30, 20, 25, 25]  # Representación del contenido de un periódico de la época

    plt.figure(figsize=(10, 6))
    plt.bar(secciones, cantidad, color=['blue', 'green', 'red', 'orange'])
    plt.title('Distribución del Contenido en el Periódico de la Época')
    plt.xlabel('Secciones del Periódico')
    plt.ylabel('Porcentaje de contenido')
    st.pyplot(plt)

# Diapositiva 4: El Rol de los Discursos Políticos
def slide_discursos_politicos():
    st.header("🎙️ Los Discursos Políticos en el Estado Nación")
    st.write("""
    Los **discursos políticos** eran una herramienta crucial para consolidar el poder del Estado. Los discursos pronunciados por líderes políticos ayudaban a **mover a las masas**, consolidar ideas nacionales y legitimar el poder.
    
    Ahora, vamos a simular un discurso donde elegirás los temas que un líder podría tratar para fortalecer el Estado Nación.
    """)

    tema_discurso = st.selectbox(
        "¿Qué tema debería destacar el líder en su discurso?",
        ["Unidad Nacional", "Desarrollo de la Educación", "Modernización del Gobierno", "Reformas Sociales"]
    )

    if tema_discurso == "Unidad Nacional":
        st.write("El discurso enfatiza la **unidad nacional** y la necesidad de superar las divisiones internas para consolidar el poder del Estado.")
    elif tema_discurso == "Desarrollo de la Educación":
        st.write("Hoy, el líder enfatiza la importancia de una **educación centralizada** para formar ciudadanos leales y conscientes.")
    elif tema_discurso == "Modernización del Gobierno":
        st.write("El discurso promete **modernizar las instituciones** del gobierno para garantizar el progreso y la estabilidad.")
    else:
        st.write("El líder aborda las **reformas sociales** necesarias para mejorar las condiciones de vida de la población y fortalecer el Estado.")

# Diapositiva 5: Participación Ciudadana y Esfera Pública
def slide_participacion():
    st.header("🗣️ Participación Ciudadana en la Esfera Pública")
    st.write("""
    La **prensa** permitió que la **opinión pública** fuera un factor crucial en la política, permitiendo a los ciudadanos influir en las decisiones gubernamentales.
    
    Vamos a simular cómo los ciudadanos pueden influir en la política a través de un **sondeo de opinión**.
    """)

    opinion = st.radio("¿Cuál es tu opinión sobre la centralización del poder?", ('A favor', 'En contra', 'Indiferente'))
    
    if opinion == 'A favor':
        st.write("Tu opinión será reflejada en los periódicos que apoyan la **centralización del poder** y la consolidación del Estado.")
    elif opinion == 'En contra':
        st.write("Los periódicos opositores destacan tu preocupación por la **descentralización del poder** y los **derechos civiles**.")
    else:
        st.write("Los periódicos neutralizan tu opinión, presentando un enfoque **equilibrado** en la discusión política.")

# Diapositiva 6: Conclusión y Reflexión Final
def slide_conclusion():
    st.header("📝 Conclusión")
    st.write("""
    A lo largo de esta presentación, hemos analizado cómo la **comunicación** fue fundamental en la construcción de los **estados modernos**. La **prensa**, los **discursos políticos** y la **participación ciudadana** ayudaron a dar forma a la **esfera pública** y consolidaron el poder estatal en el siglo XIX.
    
    ### Reflexión Final:
    Hoy en día, la **comunicación** sigue siendo clave en la construcción del **Estado Nación**, pero ahora se enfrenta a los desafíos que traen las **nuevas tecnologías**. ¿Cómo podrían los algoritmos y la inteligencia artificial seguir influyendo en la esfera pública y el Estado en el futuro?
    """)

# Mostrar todo el contenido
def run():
    slide_intro()
    st.sidebar.title("Navegar entre Secciones")
    option = st.sidebar.selectbox("Elige la sección que deseas ver:", ("Introducción", "Comunicación en el Estado Nación", "La Prensa y los Periódicos", "Los Discursos Políticos", "Participación Ciudadana", "Conclusión"))
    
    if option == "Introducción":
        slide_intro()
    elif option == "Comunicación en el Estado Nación":
        slide_comunicacion_estado()
    elif option == "La Prensa y los Periódicos":
        slide_prensa_periodicos()
    elif option == "Los Discursos Políticos":
        slide_discursos_politicos()
    elif option == "Participación Ciudadana":
        slide_participacion()
    else:
        slide_conclusion()

if __name__ == "__main__":
    run()

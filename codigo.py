import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64
        
#base de datos pandas en informacion
dfinf = pd.read_csv("backloggd_games.csv")
def convertir_k(valor):
    if isinstance(valor, str) and "K" in valor:
        return float(valor.replace("K", "")) * 1000
    else:
        return float(valor)
dfinf["Playing"] = dfinf["Playing"].apply(convertir_k)
dfinf = dfinf.sort_values("Playing", ascending=False)
dfinf['highlight'] = dfinf['Title'].apply(lambda x: 'highlight' if x == 'League of Legends' else 'normal')
dfinf = dfinf.head(30)

#fondo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image_path = "imagenes/fondo.jpg"
bg_image_base64 = get_base64_of_bin_file(bg_image_path)

page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_base64}");
        background-size: cover;
        background-position: center;  /* Centra la imagen */
    }}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.image('imagenes/logo.png', use_column_width=True)
st.image('imagenes/letras.png', use_column_width=True)

opcion = st.sidebar.selectbox('Selecciona una sección', ['Información', 'Campeones', 'Competitivo', 'Acerca de'])

if opcion == 'Información':
    #TITULO
    st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: white;">Información</h1>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    #QUE ES LEAGUE OF LEGENDS?
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">¿Qué es League of Legends?</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>League of Legends (también conocido por sus siglas LoL) es un videojuego multijugador de arena de batalla en línea desarrollado y publicado por Riot Games. Inspirándose en Defense of the Ancients, un mapa personalizado para Warcraft III, los fundadores de Riot buscaron desarrollar un juego independiente del mismo género. Desde su lanzamiento en octubre de 2009, LoL ha sido un juego gratuito y se monetiza a través de la compra de elementos para la personalización de personajes y otros accesorios. El juego está disponible para Microsoft Windows y macOS.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image('imagenes/informacionuno.jpg', use_column_width=True)
    
    #DESTRUYE EL NEXO DEL ENEMIGO
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Destruye el nexo del enemigo</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>El nexo es el corazón de las bases de ambos equipos los cuales no permitiran tan facil que los destruyas. Abrete paso entre los enemigos y destruye su nexo ganar la partida.</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("imagenes/nexoazul.jpg", caption="Los súbditos se generan en tu nexo. Detrás del nexo se encuentra la fuente, donde podrás recuperar vida y maná con rapidez y acceder a la tienda.")
    with col2:
        st.image("imagenes/nexorojo.jpg", caption="El nexo enemigo, que se encuentra en la base del equipo contrario, es igual que el de tu equipo. Si acabas con él, ganarás la partida.")
        
    #Abrete paso
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Abrete paso</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Para llegar hasta el nexo enemigo, tu equipo tendrá que avanzar por al menos una calle. Hay estructuras defensivas que bloquean tu avance: las torretas y los inhibidores. Cada calle cuenta con tres torretas y un inhibidor. Además, cada nexo tiene dos torretas adicionales.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image('imagenes/torretainhibidores.jpg', use_column_width=True)
    
    #USA TUS HABILIDADES
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Usa tus habilidades</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Los campeones cuentan con cinco habilidades básicas y dos hechizos especiales, y pueden equiparse con un máximo de siete objetos. Para que tu equipo se alce con la victoria, tendrás que ir descubriendo cuál es el orden de habilidades, hechizos de invocador y la configuración de objetos óptimos para tu campeón.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image('imagenes/habilidadescast.gif',caption="Personaje disparando la primera habilidad", use_column_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("imagenes/eclipseinf.jpg", caption="Objeto ideal para comprar cuando eres luchador, te otorga escudo, daño a enemigos con mucha vida y reestablecimiento de habilidades.")
    with col2:
        st.image("imagenes/ludencompanioninf.jpg", caption="Objeto ideal para comprar cuando eres mago, te otorga daño magico dispersivo, maná y reestablecimiento de habilidades.")
        
    # VIDEO JUEGO CON MAS JUGADORES
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">De lo mas jugado...</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>League of legends es un videojuego muy popular entre la cultura del videojuego, representado en la siguiente grafica sobre como ha sido uno de los mas jugados atraves del tiempo.</p>
    </div>
    """, unsafe_allow_html=True
    )

    chart = alt.Chart(dfinf).mark_bar().encode(
    x=alt.X("Playing", title="Jugadores activos"),
    y=alt.Y("Title", title="Juegos", sort=None),
    color=alt.Color('highlight:N', legend=None, scale=alt.Scale(domain=['normal', 'highlight'], range=['#cccccc', 'lightgreen']))
    ).properties(
    title="Número de Jugadores por Título",
    width=200,
    height=400
    )
    
    # Mostrar el gráfico en Streamlit
    st.altair_chart(chart, use_container_width=True)

elif opcion == 'Campeones':
    st.sidebar.title("Lista de campeones")
    
    # Variable para guardar el mensaje seleccionado
    mensaje = ""
    
    # Configuración de los botones en el sidebar
    with st.sidebar:    
        for img, title in [("imagenes/aatrox.jpg", "Aatrox"),
                           ("imagenes/ahri.jpg", "Ahri"),
                           ("imagenes/akali.jpg", "Akali"),
                           ("imagenes/akshan.jpg", "Akshan"),
                           ("imagenes/alistar.jpg", "Alistar"),
                           ("imagenes/ambessa.jpg", "Ambessa"),
                           ("imagenes/amumu.jpg", "Amumu"),
                           ("imagenes/anivia.jpg", "Anivia"),
                           ("imagenes/annie.jpg", "Annie"),
                           ("imagenes/aphelios.jpg", "Aphelios"),
                           ("imagenes/ashe.jpg", "Ashe"),
                           ("imagenes/aurelion.jpg", "Aurelion"),
                           ("imagenes/azir.jpg", "Azir"),
                           ("imagenes/bardo.jpg", "Bardo"),
                           ("imagenes/belvet.jpg", "Belvet"),
                           ("imagenes/blitzcrank.jpg", "Blitzcrank"),
                           ("imagenes/brand.jpg", "Brand"),
                           ("imagenes/braum.jpg", "Braum"),
                           ("imagenes/caitlyn.jpg", "Caitlyn"),
                           ("imagenes/camille.jpg", "Camille"),
                           ("imagenes/cassiopeia.jpg", "Cassiopeia"),
                           ("imagenes/chogath.jpg", "Chogath"),
                           ("imagenes/corki.jpg", "Corki"),
                           ("imagenes/darius.jpg", "Darius"),
                           ("imagenes/diana.jpg", "Diana"),
                           ("imagenes/draven.jpg", "Draven"),
                           ("imagenes/drmundo.jpg", "Dr. Mundo"),
                           ("imagenes/ekko.jpg", "Ekko"),
                           ("imagenes/elisse.jpg", "Elisse"),
                           ("imagenes/evelynn.jpg", "Evelynn"),
                           ("imagenes/ezreal.jpg", "Ezreal"),
                           ("imagenes/fiddlesticks.jpg", "Fiddlesticks"),
                           ("imagenes/fiora.jpg", "Fiora"),
                           ("imagenes/fizz.jpg", "Fizz"),
                           ("imagenes/galio.jpg", "Galio"),
                           ("imagenes/gangplank.jpg", "Gangplank"),
                           ("imagenes/garen.jpg", "Garen"),
                           ("imagenes/gnar.jpg", "Gnar"),
                           ("imagenes/gragas.jpg", "Gragas"),
                           ("imagenes/graves.jpg", "Graves"),
                           ("imagenes/gwen.jpg", "Gwen"),
                           ("imagenes/hecarim.jpg", "Hecarim"),
                           ("imagenes/heimerdinger.jpg", "Heimerdinger"),
                           ("imagenes/illaoi.jpg", "Illaoi"),
                           ("imagenes/irelia.jpg", "Irelia"),
                           ("imagenes/ivern.jpg", "Ivern"),
                           ("imagenes/janna.jpg", "Janna"),
                           ("imagenes/jarvan.jpg", "Jarvan"),
                           ("imagenes/jax.jpg", "Jax"),
                           ("imagenes/jayce.jpg", "Jayce"),
                           ("imagenes/jhin.jpg", "Jhin"),
                           ("imagenes/jinx.jpg", "Jinx"),
                           ("imagenes/kaisa.jpg", "Kaisa"),
                           ("imagenes/kalista.jpg", "Kalista"),
                           ("imagenes/karma.jpg", "Karma"),
                           ("imagenes/karthus.jpg", "Karthus"),
                           ("imagenes/kassadin.jpg", "Kassadin"),
                           ("imagenes/katarina.jpg", "Katarina"),
                           ("imagenes/kayle.jpg", "Kayle"),
                           ("imagenes/kayn.jpg", "Kayn"),
                           ("imagenes/kennen.jpg", "Kennen"),
                           ("imagenes/khazix.jpg", "Khazix"),
                           ("imagenes/kindred.jpg", "Kindred"),
                           ("imagenes/kled.jpg", "Kled"),
                           ("imagenes/kogmaw.jpg", "Kogmaw"),
                           ("imagenes/ksante.jpg", "Ksante"),
                           ("imagenes/leblanc.jpg", "Leblanc"),
                           ("imagenes/leesin.jpg", "Leesin"),
                           ("imagenes/leona.jpg", "Leona"),
                           ("imagenes/lillia.jpg", "Lillia"),
                           ("imagenes/lissandra.jpg", "Lissandra"),
                           ("imagenes/lucian.jpg", "Lucian"),
                           ("imagenes/lulu.jpg", "Lulu"),
                           ("imagenes/lux.jpg", "Lux"),
                           ("imagenes/malphite.jpg", "Malphite"),
                           ("imagenes/malzahar.jpg", "Malzahar"),
                           ("imagenes/maokai.jpg", "Maokai"),
                           ("imagenes/mf.jpg", "Miss Fortune"),
                           ("imagenes/mordekaiser.jpg", "Mordekaiser"),
                           ("imagenes/morgana.jpg", "Morgana"),
                           ("imagenes/nami.jpg", "Nami"),
                           ("imagenes/nasus.jpg", "Nasus"),
                           ("imagenes/nautilus.jpg", "Nautilus"),
                           ("imagenes/neeko.jpg", "Neeko"),
                           ("imagenes/nidalee.jpg", "Nidalee"),
                           ("imagenes/nilah.jpg", "Nilah"),
                           ("imagenes/nocturne.jpg", "Nocturne"),
                           ("imagenes/nunu.jpg", "Nunu & Willump"),
                           ("imagenes/olaf.jpg", "Olaf"),
                           ("imagenes/orianna.jpg", "Orianna"),
                           ("imagenes/ornn.jpg", "Ornn"),
                           ("imagenes/pantheon.jpg", "Pantheon"),
                           ("imagenes/poppy.jpg", "Poppy"),
                           ("imagenes/pyke.jpg", "Pyke"),
                           ("imagenes/qiyana.jpg", "Qiyana"),
                           ("imagenes/quinn.jpg", "Quinn"),
                           ("imagenes/rammus.jpg", "Rammus"),
                           ("imagenes/renataglasc.jpg", "Renataglasc"),
                           ("imagenes/renekton.jpg", "Renekton"),
                           ("imagenes/rengar.jpg", "Rengar"),
                           ("imagenes/riven.jpg", "Riven"),
                           ("imagenes/rumble.jpg", "Rumble"),
                           ("imagenes/ryze.jpg", "Ryze"),
                           ("imagenes/sejuani.jpg", "Sejuani"),
                           ("imagenes/senna.jpg", "Senna"),
                           ("imagenes/sett.jpg", "Sett"),
                           ("imagenes/shaco.jpg", "Shaco"),
                           ("imagenes/shen.jpg", "Shen"),
                           ("imagenes/shyvana.jpg", "Shyvana"),
                           ("imagenes/singed.jpg", "Singed"),
                           ("imagenes/sion.jpg", "Sion"),
                           ("imagenes/sivir.jpg", "Sivir"),
                           ("imagenes/skarner.jpg", "Skarner"),
                           ("imagenes/sona.jpg", "Sona"),
                           ("imagenes/soraka.jpg", "Soraka"),
                           ("imagenes/swain.jpg", "Swain"),
                           ("imagenes/sylas.jpg", "Sylas"),
                           ("imagenes/syndra.jpg", "Syndra"),
                           ("imagenes/taliyah.jpg", "Taliyah"),
                           ("imagenes/talon.jpg", "Talon"),
                           ("imagenes/taric.jpg", "Taric"),
                           ("imagenes/teemo.jpg", "Teemo"),
                           ("imagenes/thresh.jpg", "Thresh"),
                           ("imagenes/tristana.jpg", "Tristana"),
                           ("imagenes/trundle.jpg", "Trundle"),
                           ("imagenes/tryndamere.jpg", "Tryndamere"),
                           ("imagenes/twistedfate.jpg", "Twistedfate"),
                           ("imagenes/twitch.jpg", "Twitch"),
                           ("imagenes/udyr.jpg", "Udyr"),
                           ("imagenes/urgot.jpg", "Urgot"),
                           ("imagenes/varus.jpg", "Varus"),
                           ("imagenes/vayne.jpg", "Vayne"),
                           ("imagenes/veigar.jpg", "Veigar"),
                           ("imagenes/velkoz.jpg", "Velkoz"),
                           ("imagenes/vex.jpg", "Vex"),
                           ("imagenes/vi.jpg", "Vi"),
                           ("imagenes/viego.jpg", "Viego"),
                           ("imagenes/viktor.jpg", "Viktor"),
                           ("imagenes/vladimir.jpg", "Vladimir"),
                           ("imagenes/volibear.jpg", "Volibear"),
                           ("imagenes/warwick.jpg", "Warwick"),
                           ("imagenes/wukong.jpg", "Wukong"),
                           ("imagenes/xerath.jpg", "Xerath"),
                           ("imagenes/xinzhao.jpg", "Xinzhao"),
                           ("imagenes/yasuo.jpg", "Yasuo"),
                           ("imagenes/yi.jpg", "Yi"),]:
            col1, col2 = st.columns([1, 1])  # Proporciones iguales para columnas
            with col1:
                st.image(img, width=60)  # Ajusta el tamaño de la imagen
            with col2:
                if st.button(title):  # Al presionar un botón, se actualiza el mensaje
                    mensaje = title
    
    # Mostrar el mensaje en la página principal
    if title:
        st.markdown(
        f"""
        <div style="text-align: center;">
            <h1 style="color: white;">{mensaje}</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

                

elif opcion == 'Competitivo':
    st.markdown("<h1 style='color: white;'>Competitivo</h1>", unsafe_allow_html=True)
    video_url = "https://www.youtube.com/watch?v=Kv2rswmxBVs"
    st.video(video_url)
    
elif opcion == 'Acerca de':
     #TITULO
    st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: white;">Acerca De</h1>
    </div>
    """,
    unsafe_allow_html=True
    )
    
   #iNTEGRANTES
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Integrantes</h3>
    </div>
    """,
    unsafe_allow_html=True
    )

    #INTEGRANTES REAL
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Diego Abarca</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Cristobal Camousseight</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Rodrigo Manríquez</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Profesora</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Monica Otero Ferreiro</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Ing. Civil Informatica</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">USS All rights reserved</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>League of legends es un juego de riot games</p>
    </div>
    """, unsafe_allow_html=True)

    st.image('imagenes/logouss.png', use_column_width=True)

    
    

    






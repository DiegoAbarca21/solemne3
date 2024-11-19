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
                           ("imagenes/drmundo.jpg", "Drmundo"),
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
                           ("imagenes/mf.jpg", "Mf"),
                           ("imagenes/mordekaiser.jpg", "Mordekaiser"),
                           ("imagenes/morgana.jpg", "Morgana"),
                           ("imagenes/nami.jpg", "Nami"),
                           ("imagenes/nasus.jpg", "Nasus"),
                           ("imagenes/nautilus.jpg", "Nautilus"),
                           ("imagenes/neeko.jpg", "Neeko"),
                           ("imagenes/nidalee.jpg", "Nidalee"),
                           ("imagenes/nilah.jpg", "Nilah"),
                           ("imagenes/nocturne.jpg", "Nocturne"),
                           ("imagenes/nunu.jpg", "Nunu"),
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
    if mensaje == "Aatrox":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Aatrox</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ahri":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ahri</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Akali":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Akali</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Akshan":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Akshan</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Alistar":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Alistar</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ambessa":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ambessa</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Amumu":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Amumu</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Anivia":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Anivia</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Annie":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Annie</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Aphelios":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Aphelios</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ashe":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ashe</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Aurelion":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Aurelion</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Azir":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Azir</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Bardo":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Bardo</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Belvet":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Belvet</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Blitzcrank":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Blitzcrank</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Brand":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Brand</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Braum":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Braum</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Caitlyn":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Caitlyn</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Camille":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Camille</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Cassiopeia":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Cassiopeia</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Chogath":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Chogath</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Corki":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Corki</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Darius":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Darius</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Diana":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Diana</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Draven":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Draven</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Drmundo":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Drmundo</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ekko":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ekko</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Elisse":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Elisse</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Evelynn":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Evelynn</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ezreal":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ezreal</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Fiddlesticks":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Fiddlesticks</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Fiora":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Fiora</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Fizz":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Fizz</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Galio":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Galio</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Gangplank":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Gangplank</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Garen":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Garen</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Gnar":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Gnar</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Gragas":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Gragas</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Graves":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Graves</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Gwen":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Gwen</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Hecarim":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Hecarim</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Heimerdinger":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Heimerdinger</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Illaoi":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Illaoi</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Irelia":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Irelia</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ivern":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ivern</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Janna":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Janna</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Jarvan":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Jarvan</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Jax":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Jax</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Jayce":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Jayce</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Jhin":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Jhin</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Jinx":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Jinx</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kaisa":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kaisa</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kalista":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kalista</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Karma":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Karma</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Karthus":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Karthus</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kassadin":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kassadin</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Katarina":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Katarina</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kayle":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kayle</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kayn":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kayn</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kennen":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kennen</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Khazix":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Khazix</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kindred":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kindred</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kled":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kled</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Kogmaw":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Kogmaw</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ksante":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ksante</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Leblanc":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Leblanc</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Leesin":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Leesin</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Leona":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Leona</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Lillia":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Lillia</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Lissandra":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Lissandra</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Lucian":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Lucian</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Lulu":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Lulu</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Lux":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Lux</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Malphite":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Malphite</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Malzahar":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Malzahar</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Maokai":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Maokai</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Mf":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Mf</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Mordekaiser":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Mordekaiser</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Morgana":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Morgana</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Nami":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Nami</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Nasus":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Nasus</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Nautilus":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Nautilus</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Neeko":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Neeko</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Nidalee":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Nidalee</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Nilah":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Nilah</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Nocturne":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Nocturne</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Nunu":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Nunu</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Olaf":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Olaf</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Orianna":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Orianna</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ornn":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ornn</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Pantheon":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Pantheon</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Poppy":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Poppy</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Pyke":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Pyke</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Qiyana":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Qiyana</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Quinn":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Quinn</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Rammus":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Rammus</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Renataglasc":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Renataglasc</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Renekton":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Renekton</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Rengar":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Rengar</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Riven":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Riven</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Rumble":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Rumble</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Ryze":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Ryze</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Sejuani":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Sejuani</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Senna":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Senna</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Sett":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Sett</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Shaco":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Shaco</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Shen":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Shen</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Shyvana":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Shyvana</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Singed":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Singed</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Sion":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Sion</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Sivir":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Sivir</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Skarner":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Skarner</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Sona":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Sona</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Soraka":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Soraka</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Swain":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Swain</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Sylas":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Sylas</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Syndra":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Syndra</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Taliyah":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Taliyah</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Talon":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Talon</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Taric":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Taric</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Teemo":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Teemo</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Thresh":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Thresh</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Tristana":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Tristana</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Trundle":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Trundle</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Tryndamere":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Tryndamere</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Twistedfate":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Twistedfate</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Twitch":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Twitch</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Udyr":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Udyr</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Urgot":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Urgot</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Varus":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Varus</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Vayne":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Vayne</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Veigar":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Veigar</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Velkoz":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Velkoz</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Vex":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Vex</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Vi":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Vi</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Viego":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Viego</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Viktor":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Viktor</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Vladimir":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Vladimir</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Volibear":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Volibear</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Warwick":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Warwick</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Wukong":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Wukong</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Xerath":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Xerath</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Xinzhao":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Xinzhao</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Yasuo":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Yasuo</h1>
        </div>
        """,
        unsafe_allow_html=True
        )

    elif mensaje == "Yi":
        st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: white;">Yi</h1>
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

    
    

    






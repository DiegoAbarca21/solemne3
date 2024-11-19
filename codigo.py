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
                st.image(img, width=50)  # Ajusta el tamaño de la imagen
            with col2:
                if st.button(title):  # Al presionar un botón, se actualiza el mensaje
                    mensaje = title
    
    # Mostrar el mensaje en la página principal
    if mensaje == "Aatrox":
        st.write("Haz seleccionado a Aatrox")
    elif mensaje == "Ahri":
        st.write("Haz seleccionado a Ahri")
    elif mensaje == "Akali":
        st.write("Haz seleccionado a Akali")
    elif mensaje == "Akshan":
        st.write("Haz seleccionado a Akshan")
    elif mensaje == "Alistar":
        st.write("Haz seleccionado a Alistar")
    elif mensaje == "Ambessa":
        st.write("Haz seleccionado a Ambessa")
    elif mensaje == "Amumu":
        st.write("Haz seleccionado a Amumu")
    elif mensaje == "Anivia":
        st.write("Haz seleccionado a Anivia")
    elif mensaje == "Annie":
        st.write("Haz seleccionado a Annie")
    elif mensaje == "Aphelios":
        st.write("Haz seleccionado a Aphelios")
    elif mensaje == "Ashe":
        st.write("Haz seleccionado a Ashe")
    elif mensaje == "Aurelion":
        st.write("Haz seleccionado a Aurelion")
    elif mensaje == "Azir":
        st.write("Haz seleccionado a Azir")
    elif mensaje == "Bardo":
        st.write("Haz seleccionado a Bardo")
    elif mensaje == "Belvet":
        st.write("Haz seleccionado a Belvet")
    elif mensaje == "Blitzcrank":
        st.write("Haz seleccionado a Blitzcrank")
    elif mensaje == "Brand":
        st.write("Haz seleccionado a Brand")
    elif mensaje == "Braum":
        st.write("Haz seleccionado a Braum")
    elif mensaje == "Caitlyn":
        st.write("Haz seleccionado a Caitlyn")
    elif mensaje == "Camille":
        st.write("Haz seleccionado a Camille")
    elif mensaje == "Cassiopeia":
        st.write("Haz seleccionado a Cassiopeia")
    elif mensaje == "Chogath":
        st.write("Haz seleccionado a Chogath")
    elif mensaje == "Corki":
        st.write("Haz seleccionado a Corki")
    elif mensaje == "Darius":
        st.write("Haz seleccionado a Darius")
    elif mensaje == "Diana":
        st.write("Haz seleccionado a Diana")
    elif mensaje == "Draven":
        st.write("Haz seleccionado a Draven")
    elif mensaje == "Drmundo":
        st.write("Haz seleccionado a Drmundo")
    elif mensaje == "Ekko":
        st.write("Haz seleccionado a Ekko")
    elif mensaje == "Elisse":
        st.write("Haz seleccionado a Elisse")
    elif mensaje == "Evelynn":
        st.write("Haz seleccionado a Evelynn")
    elif mensaje == "Ezreal":
        st.write("Haz seleccionado a Ezreal")
    elif mensaje == "Fiddlesticks":
        st.write("Haz seleccionado a Fiddlesticks")
    elif mensaje == "Fiora":
        st.write("Haz seleccionado a Fiora")
    elif mensaje == "Fizz":
        st.write("Haz seleccionado a Fizz")
    elif mensaje == "Galio":
        st.write("Haz seleccionado a Galio")
    elif mensaje == "Gangplank":
        st.write("Haz seleccionado a Gangplank")
    elif mensaje == "Garen":
        st.write("Haz seleccionado a Garen")
    elif mensaje == "Gnar":
        st.write("Haz seleccionado a Gnar")
    elif mensaje == "Gragas":
        st.write("Haz seleccionado a Gragas")
    elif mensaje == "Graves":
        st.write("Haz seleccionado a Graves")
    elif mensaje == "Gwen":
        st.write("Haz seleccionado a Gwen")
    elif mensaje == "Hecarim":
        st.write("Haz seleccionado a Hecarim")
    elif mensaje == "Heimerdinger":
        st.write("Haz seleccionado a Heimerdinger")
    elif mensaje == "Illaoi":
        st.write("Haz seleccionado a Illaoi")
    elif mensaje == "Irelia":
        st.write("Haz seleccionado a Irelia")
    elif mensaje == "Ivern":
        st.write("Haz seleccionado a Ivern")
    elif mensaje == "Janna":
        st.write("Haz seleccionado a Janna")
    elif mensaje == "Jarvan":
        st.write("Haz seleccionado a Jarvan")
    elif mensaje == "Jax":
        st.write("Haz seleccionado a Jax")
    elif mensaje == "Jayce":
        st.write("Haz seleccionado a Jayce")
    elif mensaje == "Jhin":
        st.write("Haz seleccionado a Jhin")
    elif mensaje == "Jinx":
        st.write("Haz seleccionado a Jinx")
    elif mensaje == "Kaisa":
        st.write("Haz seleccionado a Kaisa")
    elif mensaje == "Kalista":
        st.write("Haz seleccionado a Kalista")
    elif mensaje == "Karma":
        st.write("Haz seleccionado a Karma")
    elif mensaje == "Karthus":
        st.write("Haz seleccionado a Karthus")
    elif mensaje == "Kassadin":
        st.write("Haz seleccionado a Kassadin")
    elif mensaje == "Katarina":
        st.write("Haz seleccionado a Katarina")
    elif mensaje == "Kayle":
        st.write("Haz seleccionado a Kayle")
    elif mensaje == "Kayn":
        st.write("Haz seleccionado a Kayn")
    elif mensaje == "Kennen":
        st.write("Haz seleccionado a Kennen")
    elif mensaje == "Khazix":
        st.write("Haz seleccionado a Khazix")
    elif mensaje == "Kindred":
        st.write("Haz seleccionado a Kindred")
    elif mensaje == "Kled":
        st.write("Haz seleccionado a Kled")
    elif mensaje == "Kogmaw":
        st.write("Haz seleccionado a Kogmaw")
    elif mensaje == "Ksante":
        st.write("Haz seleccionado a Ksante")
    elif mensaje == "Leblanc":
        st.write("Haz seleccionado a Leblanc")
    elif mensaje == "Leesin":
        st.write("Haz seleccionado a Leesin")
    elif mensaje == "Leona":
        st.write("Haz seleccionado a Leona")
    elif mensaje == "Lillia":
        st.write("Haz seleccionado a Lillia")
    elif mensaje == "Lissandra":
        st.write("Haz seleccionado a Lissandra")
    elif mensaje == "Lucian":
        st.write("Haz seleccionado a Lucian")
    elif mensaje == "Lulu":
        st.write("Haz seleccionado a Lulu")
    elif mensaje == "Lux":
        st.write("Haz seleccionado a Lux")
    elif mensaje == "Malphite":
        st.write("Haz seleccionado a Malphite")
    elif mensaje == "Malzahar":
        st.write("Haz seleccionado a Malzahar")
    elif mensaje == "Maokai":
        st.write("Haz seleccionado a Maokai")
    elif mensaje == "Mf":
        st.write("Haz seleccionado a Mf")
    elif mensaje == "Mordekaiser":
        st.write("Haz seleccionado a Mordekaiser")
    elif mensaje == "Morgana":
        st.write("Haz seleccionado a Morgana")
    elif mensaje == "Nami":
        st.write("Haz seleccionado a Nami")
    elif mensaje == "Nasus":
        st.write("Haz seleccionado a Nasus")
    elif mensaje == "Nautilus":
        st.write("Haz seleccionado a Nautilus")
    elif mensaje == "Neeko":
        st.write("Haz seleccionado a Neeko")
    elif mensaje == "Nidalee":
        st.write("Haz seleccionado a Nidalee")
    elif mensaje == "Nilah":
        st.write("Haz seleccionado a Nilah")
    elif mensaje == "Nocturne":
        st.write("Haz seleccionado a Nocturne")
    elif mensaje == "Nunu":
        st.write("Haz seleccionado a Nunu")
    elif mensaje == "Olaf":
        st.write("Haz seleccionado a Olaf")
    elif mensaje == "Orianna":
        st.write("Haz seleccionado a Orianna")
    elif mensaje == "Ornn":
        st.write("Haz seleccionado a Ornn")
    elif mensaje == "Pantheon":
        st.write("Haz seleccionado a Pantheon")
    elif mensaje == "Poppy":
        st.write("Haz seleccionado a Poppy")
    elif mensaje == "Pyke":
        st.write("Haz seleccionado a Pyke")
    elif mensaje == "Qiyana":
        st.write("Haz seleccionado a Qiyana")
    elif mensaje == "Quinn":
        st.write("Haz seleccionado a Quinn")
    elif mensaje == "Rammus":
        st.write("Haz seleccionado a Rammus")
    elif mensaje == "Renataglasc":
        st.write("Haz seleccionado a Renataglasc")
    elif mensaje == "Renekton":
        st.write("Haz seleccionado a Renekton")
    elif mensaje == "Rengar":
        st.write("Haz seleccionado a Rengar")
    elif mensaje == "Riven":
        st.write("Haz seleccionado a Riven")
    elif mensaje == "Rumble":
        st.write("Haz seleccionado a Rumble")
    elif mensaje == "Ryze":
        st.write("Haz seleccionado a Ryze")
    elif mensaje == "Sejuani":
        st.write("Haz seleccionado a Sejuani")
    elif mensaje == "Senna":
        st.write("Haz seleccionado a Senna")
    elif mensaje == "Sett":
        st.write("Haz seleccionado a Sett")
    elif mensaje == "Shaco":
        st.write("Haz seleccionado a Shaco")
    elif mensaje == "Shen":
        st.write("Haz seleccionado a Shen")
    elif mensaje == "Shyvana":
        st.write("Haz seleccionado a Shyvana")
    elif mensaje == "Singed":
        st.write("Haz seleccionado a Singed")
    elif mensaje == "Sion":
        st.write("Haz seleccionado a Sion")
    elif mensaje == "Sivir":
        st.write("Haz seleccionado a Sivir")
    elif mensaje == "Skarner":
        st.write("Haz seleccionado a Skarner")
    elif mensaje == "Sona":
        st.write("Haz seleccionado a Sona")
    elif mensaje == "Soraka":
        st.write("Haz seleccionado a Soraka")
    elif mensaje == "Swain":
        st.write("Haz seleccionado a Swain")
    elif mensaje == "Sylas":
        st.write("Haz seleccionado a Sylas")
    elif mensaje == "Syndra":
        st.write("Haz seleccionado a Syndra")
    elif mensaje == "Taliyah":
        st.write("Haz seleccionado a Taliyah")
    elif mensaje == "Talon":
        st.write("Haz seleccionado a Talon")
    elif mensaje == "Taric":
        st.write("Haz seleccionado a Taric")
    elif mensaje == "Teemo":
        st.write("Haz seleccionado a Teemo")
    elif mensaje == "Thresh":
        st.write("Haz seleccionado a Thresh")
    elif mensaje == "Tristana":
        st.write("Haz seleccionado a Tristana")
    elif mensaje == "Trundle":
        st.write("Haz seleccionado a Trundle")
    elif mensaje == "Tryndamere":
        st.write("Haz seleccionado a Tryndamere")
    elif mensaje == "Twistedfate":
        st.write("Haz seleccionado a Twistedfate")
    elif mensaje == "Twitch":
        st.write("Haz seleccionado a Twitch")
    elif mensaje == "Udyr":
        st.write("Haz seleccionado a Udyr")
    elif mensaje == "Urgot":
        st.write("Haz seleccionado a Urgot")
    elif mensaje == "Varus":
        st.write("Haz seleccionado a Varus")
    elif mensaje == "Vayne":
        st.write("Haz seleccionado a Vayne")
    elif mensaje == "Veigar":
        st.write("Haz seleccionado a Veigar")
    elif mensaje == "Velkoz":
        st.write("Haz seleccionado a Velkoz")
    elif mensaje == "Vex":
        st.write("Haz seleccionado a Vex")
    elif mensaje == "Vi":
        st.write("Haz seleccionado a Vi")
    elif mensaje == "Viego":
        st.write("Haz seleccionado a Viego")
    elif mensaje == "Viktor":
        st.write("Haz seleccionado a Viktor")
    elif mensaje == "Vladimir":
        st.write("Haz seleccionado a Vladimir")
    elif mensaje == "Volibear":
        st.write("Haz seleccionado a Volibear")
    elif mensaje == "Warwick":
        st.write("Haz seleccionado a Warwick")
    elif mensaje == "Wukong":
        st.write("Haz seleccionado a Wukong")
    elif mensaje == "Xerath":
        st.write("Haz seleccionado a Xerath")
    elif mensaje == "Xinzhao":
        st.write("Haz seleccionado a Xinzhao")
    elif mensaje == "Yasuo":
        st.write("Haz seleccionado a Yasuo")
    elif mensaje == "Yi":
        st.write("Haz seleccionado a Yi")
    
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

    
    

    






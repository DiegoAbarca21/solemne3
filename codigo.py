import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64


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
    st.markdown("<h1 style='color: white;'>Información</h1>", unsafe_allow_html=True)
    
    #QUE ES LEAGUE OF LEGENDS?
    st.markdown("<h3 style='color: white;'>¿Qué es League of Legends?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>League of Legends es un juego de estrategia por equipos en el que dos equipos conformados por cinco poderosos campeones se enfrentan para destruir la base del otro. Elige de entre más de 140 campeones para realizar jugadas épicas, asegurar asesinatos y destruir torretas mientras avanzas hacia la victoria.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image('imagenes/informacionuno.jpg', use_column_width=True)
    
    #DESTRUYE EL NEXO DEL ENEMIGO
    st.markdown("<h3 style='color: white;'>Destruye el nexo del enemigo</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>El nexo es el corazón de las bases de ambos equipos. Destruye el nexo enemigo para ganar la partida.</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    nexoazul = "imagenes/nexoazul.jpg"  # Cambia esto por la ruta de tu primera imagen
    nexorojo = "imagenes/nexorojo.jpg"
    with col1:
        st.image(image1, caption="nexoazul")
    with col2:
        st.image(image2, caption="nexorojo")
        
elif opcion == 'Campeones':
    st.write('Aquí van los datos.')
    
elif opcion == 'Competitivo':
    st.markdown("<h1 style='color: white;'>Competitivo</h1>", unsafe_allow_html=True)
    video_url = "https://www.youtube.com/watch?v=Kv2rswmxBVs"
    st.video(video_url)
    
elif opcion == 'Acerca de':
    st.write('Aquí se mostraría la información adicional.')






import streamlit as st
from PIL import Image
st.title("Hola mundo")

st.header("En este espacio comienzo a desarroollar mis aplicaciones")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Sin título-1_Mesa de trabajo 1.jpg')
st.image(image, caption='Sin título-1_Mesa de trabajo 1')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')


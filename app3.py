#el llamado a la librería streamlit con el alias st
import streamlit as st 
#hacemos el llamado a la función
from img_classification import teachable_machine_classification 
import keras
from PIL import Image, ImageOps
import numpy as np
#le ponemos un título a nuestra aplicación
st.title('Aplicación de reconocimiento de perros :dog: y gatos :cat:')
#le voy a decir que tipos de archivos está recibiendo:
uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
#si el contenido no está vacío, se va a leer con el comando image
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  #le voy a decir que me despliegue en la página la misma imagen
  #st.image(image)
  st.sidebar.image(image)
  #aquí estoy llamando la función teachable machine, va a leer la imagen e importar el modelo keras
  #la salida de esta función va a ser una etiqueta 0 si es un perro, 1 si es un gato
  label = teachable_machine_classification(image, 'keras_model.h5')
  if label == 0:
    st.write('Es un perrito :dog:') 

  else:
    st.write('Es un gatito :cat:')

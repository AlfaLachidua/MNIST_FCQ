#importar las librerías
import streamlit as st 
st.title("Mi aplicación") #título
st.sidebar.header("Esta aplicación es solo un demo")
#st.sidebar.image("")
boton = st.button("globos")
if boton:
  st.balloon()
  
  

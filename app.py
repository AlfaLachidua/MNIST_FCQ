#importar las librerías
import streamlit as st 
st.title("Mi aplicación") #título
st.sidebar.header("Esta aplicación es solo un demo")
st.sidebar.image("https://cdn.dribbble.com/userupload/3250764/file/original-8901511465fba8c4f7a4329ae6a9a565.png?compress=1&resize=1024x768")
boton = st.button("globos")
if boton:
  st.balloons()
  
  

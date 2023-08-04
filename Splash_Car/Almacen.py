import streamlit as st

st.write("""
# Mi pagina web
Bienvenido a mi pagina web
""")

ped = st.radio("¿Que desea hacer?", ("Ingresar", "Registrar"))
file = st.file_uploader("Subir archivo", type=["txt"])

if file is not None:
    st.write(file)
    file.seek(0)
    content = file.read()
    st.write(content)

#   streamlit run Splash_Car\Almacen.py

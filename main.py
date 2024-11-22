import streamlit as st

Introduccion = st.Page("paginas/uno.py", title="Introducción")
prueba = st.Page("paginas/dos.py", title="prueba")

pg = st.navigation([Introduccion, prueba])
pg.run()



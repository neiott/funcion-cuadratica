import streamlit as st

Introduccion = st.Page("paginas/uno.py", title="Introducción")
prueba = st.Page("paginas/dos.py", title="Partes de la función")
pagina2 = st.Page("paginas/tres.py", title="Ecuación canónica de la parábola")
pagina3 = st.Page("paginas/cuatro.py", title="Métodos de solución")
pagina4 = st.Page("paginas/cinco.py", title="Evaluación")
pagina5 = st.Page("paginas/seis.py", title="¿Quién soy?")
pg = st.navigation([Introduccion, prueba, pagina2, pagina3, pagina4, pagina5])
pg.run()



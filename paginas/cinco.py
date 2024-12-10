import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.subheader("Prueba Final")
st.markdown('''Para finalizar vamos a ver que tanto aprendiste por medio de esta página web sobre la función cuadrática, sus elementos y las formas en que esta se puede solucionar.''')
st.markdown('''**Pregunta 1:**''')
st.markdown('''De la siguiente ecuación, ¿Cuál es su vértice?''')
st.latex("(x-5)^2=-8(y+2)")
opc = st.selectbox("opcion del usuario:", options=["Seleccionar", "A.(-2,-5)", "B.(-5,-2)", "C.(5,2)", "D.(5,-2)"])
if opc == "A.(-2,-5)":
    st.error("la opción seleccionada es incorrecta")

elif opc == "B.(-5,-2)":
    st.error("la opción seleccionada es incorrecta")

elif opc == "C.(5,2)":
    st.error("la opción seleccionada es incorrecta")

elif opc == "D.(5,-2)":
    st.success("la opción seleccionada es correcta")

st.markdown('''**Pregunta 2:**''')
st.markdown('''De la siguiente ecuación, ¿Hacía dónde abre la parábola?''')
st.latex("(x-5)^2=-8(y+2)")
opc = st.selectbox("opcion del usuario:", options=["Seleccionar", "Arriba", "Abajo", "Izquierda", "Derecha"])
if opc == "Arriba":
    st.error("la opción seleccionada es incorrecta")

elif opc == "Abajo":
    st.success("la opción seleccionada es correcta")

elif opc == "Izquierda":
    st.error("la opción seleccionada es incorrecta")

elif opc == "Derecha":
    st.error("la opción seleccionada es incorrecta")

st.markdown('''**Pregunta 3:**''')
st.markdown('''De la siguiente ecuación, ¿Cómo es su forma general?''')
st.latex("(x-5)^2=-8(y+2)")
opc = st.selectbox("opcion del usuario:", options=["Seleccionar", "x^2-10x+8y+41=0", "x^2-10x+8y+41=8", "y^2-10y+8x+41=0", "x^2+10x-8y-41=0"])
if opc == "x^2-10x+8y+41=0":
    st.success("la opción seleccionada es correcta")

elif opc == "x^2-10x+8y+41=8":
    st.error("la opción seleccionada es incorrecta")

elif opc == "y^2-10y+8x+41=0":
    st.error("la opción seleccionada es incorrecta")

elif opc == "x^2+10x-8y-41=0":
    st.error("la opción seleccionada es incorrecta")


st.markdown('''**Pregunta 4:**''')
st.markdown('''El vértice de la siguiente ecuación es''')
st.latex("f(x)=2x^2-8x+6")
opc = st.selectbox("opcion del usuario:", options=["Seleccionar", "A.(3,-8)", "B.(5,10)", "C.(2,-2)", "D.(10,5)"])
if opc == "A.(3,-8)":
    st.error("la opción seleccionada es incorrecta")

elif opc == "B.(5,10)":
    st.error("la opción seleccionada es incorrecta")

elif opc == "C.(2,-2)":
    st.success("la opción seleccionada es correcta")

elif opc == "D.(10,5)":
    st.error("la opción seleccionada es incorrecta")

st.markdown('''**Pregunta 5:**''')
st.markdown('''¿La directriz al vértice tiene la misma distancia del foco al vértica?''')

opc = st.selectbox("opcion del usuario:", options=["Seleccionar", "Verdadero", "Falso"])
if opc == "Verdadero":
    st.success("la opción seleccionada es correcta")

elif opc == "Falso":
    st.error("la opción seleccionada es incorrecta")


st.markdown('''**Pregunta 6:**''')
st.markdown('''¿Cómo es la ecuación de una parábola con eje de simetría vertical y foco positivo''')
opc = st.selectbox("opcion del usuario:", options=["Seleccionar", "A.(x-h)^2=-4p(y-k)", "B.(y-k)^2=-4p(x-h)", "C.(x-h)^2=4p(y-k)", "D.(y-k)^2=4p(x-h)"])
if opc == "A.(x-h)^2=-4p(y-k)":
    st.error("la opción seleccionada es incorrecta")

elif opc == "B.(y-k)^2=-4p(x-h)":
    st.error("la opción seleccionada es incorrecta")

if opc == "C.(x-h)^2=4p(y-k)":
    st.success("la opción seleccionada es correcta")

elif opc == "D.(y-k)^2=4p(x-h)":
    st.error("la opción seleccionada es incorrecta")

st.markdown('''**Pregunta 7:**''')
st.markdown('''Dada la ecuación''')
st.latex("x^2-5x+6=0")
st.markdown('''cuales son sus 2 soluiones''')
opc = st.selectbox("opcion del usuario:", options=["Seleccionar", "A. x1=6, x2=7", "B.x1= 3 x2=4", "C.x1=2, x2=3",])
if opc == "A.x1=6, x2=7":
    st.error("la opción seleccionada es incorrecta")

elif opc == "B.x1= 3 x2=4":
    st.error("la opción seleccionada es incorrecta")

elif opc == "C.x1=2, x2=3":
    st.success("la opción seleccionada es correcta")


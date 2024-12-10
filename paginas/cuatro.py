import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.html("<center> <h1> Métodos De Solución </h1> </center>")
st.subheader("Fórmula general")
st.markdown('''
   Este es el método mas común y el mas sencillo usado para encontrar que soluciones tiene una función cuadrática. La fórmula se ve de la siguiente manera:
    ''')
st.latex(r"x=\frac{-b± √b^2 - 4ac }{2a}")
st.markdown('''
   **Paso 1:** Lo primero que tenemos que hacer es identificar que letra de número de nuestra función pertenecen a las letras "a", "b" y "c" para poderlo reemplazar en nuestra formula. Tomaremos de ejemplo la siguiente ecuación.
    ''')
st.latex("f(x)=2x^2+3x-5")
st.markdown('''
   En donde tenemos que:
   a = 2, b = 3, y c = -5. Despues de esto lo reemplazaremos en nuestra fórmula
    ''')
st.latex(r"x=\frac{-3± √3^2 - 4(2)(-5) }{2(-5)}")

st.markdown('''
**Paso 2:** Nuestro segundo paso que tenemos que hacer es hallar el discriminante de nuestra ecuación, es decir, hallar que número está dentro de la raíz, de la siguiente manera
  
   ''')
st.latex("dis=3^2 - 4(2)(-5)")
st.markdown(''' Esto nos da como resultado''')
st.latex("dis=40")

st.markdown('''
**Paso 3:** Por ultimo paso separamos la solución positiva de la solución negativa y finalmente operamos para lograr encontrar nuestras dos posibles soluciones.
  
   ''')
st.latex(r"x1=\frac{-3 + √40) }{2(-5)}")
st.latex(r"x2=\frac{-3 - √40) }{2(-5)}")
st.markdown(''' Al operar esto tenemos como resultado:''')
st.latex(r"x1=1")
st.latex(r"x2=-2.5")

st.markdown('''
**Dato:** Si nuestro discriminante nos da 0 la ecuación tiene una sola solución, si el discriminante es negativo la ecuación no tiene solución real y por último si el dismcrimante es mayor a 0 tiene dos respuestas diferentes.
  
   ''')
st.subheader("Factorización")
st.markdown(''' Existe otro método para resolver estas ecuaciones y es por la factorización. Para la explicación de este usaremos la siguiente ecuación cuadrática:''')
st.latex("f(x)=x^2+5x+6")
st.markdown(''' **Paso 1:** Igual que con la formula general tenemos que identificar que valores son a, b y c, entonces tenemos que a = 1, b = 5 y c = 6''')

st.markdown(''' **Paso 2:** Despues de haberlos identificado tenemos que hallar dos números que mútiplicados den como resultado C y al sumarse den como resultado 5, es decir, que al multiplicarsen su resultado sea 6 y al ser sumados me den 5, podemos ver que los números que satisfacen estas operaciones son el 2 y el 3, y lo escribimos de esta manera''')
st.latex("(x+2)(x+3)=0")
st.markdown(''' **Paso 3:** Nuestro tercer paso consiste en coger para termino e igualarlo a cero, de esta manera''')
st.latex("x+2 = 0")
st.latex("x+3 = 0")
st.markdown(''' **Paso 3:** Por último, resolvemos las ecuaciones que obtuvimos y esto serán los resultados de nuestra ecuación cuadrática ''')
st.latex("x =-2")
st.latex("x = -3")
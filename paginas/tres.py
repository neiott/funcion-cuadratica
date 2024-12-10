import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.html("<center> <h1> Ecuación canónica </h1> </center>")
st.markdown('''
    La función cuadrática también es conocida por su forma canónica, la ecuación canónica es una forma mas sencilla de mostrar una parábola en función de su vertice y su fistancia focal, su ecuación tiene cambios y existen 4 diferentes.
    ''')
st.markdown(''' **Parábola con eje de simetría vertical y foco positivo:** La forma de esta parabola que abre hacia arriba es
''')
st.latex("(x-h)^2=4p(y-k)")
st.markdown(''' **Parábola con eje de simetría vertical y foco negativo:** La forma de esta parabola que abre hacia abajo es
''')
st.latex("(x-h)^2=-4p(y-k)")
st.markdown(''' **Parábola con eje de simetría horizontal y foco positivo:** La forma de esta parabola que abre hacia la derecha es
''')
st.latex("(y-k)^2=4p(x-h)")
st.markdown(''' **Parábola con eje de simetría horizontal y foco negativo:** La forma de esta parabola que abre hacia la derecha es
''')
st.latex("(y-k)^2=-4p(x-h)")
st.markdown(''' Gracias a las canónicas tenemos más facilidad de encontrar el vertice y la distancia focal de las parábolas que nos den. El vértice de una parábola está nombrado por:
''')
st.latex("v(h,k)")
st.markdown(''' Como vemos todas nuestras ecuaciones sin importar hacía donde abran tienen las letras h y k, h es nuestra coordenada en X del vértice y k es nuestra coordenada en Y del vértice.
Al tener una ecuación canónica y si se quiere saber su vértice lo unico que tenemos que hacer coger el número que está en "h" cambiarlo de signo y asi ya tenemos nuestra coordenada en X, de la misma lo hacemos para saber nuestra coordenada en Y, cogemos el número que esté en la posición de la k y lo cambiamos de signo.
''')
st.markdown('''**Ejemplo.**''')
st.latex("(x-2)^2 = 4 (y-3)")
st.markdown('''Lo primero que tenemos que hacer para encontrar el vértice de esta parábola es saber hacia dónde abre, como vemos que antes del igual está la X, eso nos quiere decir que es una parábola que abre hacía arriba o hacia abajo, después del igual tenemos la distancia focal y podemos ver que esta es positiva, por lo tanto esta parábola abre hacia arriba ''')
st.markdown(''' Como ya sabemos la h es nuestro valor en x de la coordenada para encontrar el vertice y lo que tenemos que hacer es cambiarle el signo, por lo tanto nuestra coordenada en x es de "+2", por lo tanto el otro parentesis contiene a "k", hacemos lo mismo, le cambiamos su signo. Después de esto podemos obtener el véritice y vemos que es''' )
st.latex("V(2,3)")

st.subheader("**De general a canónica**")
st.markdown(''' Nuestra parábola lo mas común es que nos la entreguen de forma general, es decir, de forma ax^2+b+cy+c=0, pero para más comodidad hay una forma de poder llegar a su forma canónica y cada que podamos lo haremos''')
st.markdown('''**Ejemplo.**''')
st.latex("2x^2-12x-16y-14=0")
st.markdown('''**Paso 1**: Nuestro primer paso es dividir cada termino de nuestra ecuación general entre el número que está acompañando a X^2, es decir, nuestra ecuación toma la forma:
''')
st.latex("x^2-6x-8y-7=0")
st.markdown('''**Paso 2:** Nuestro segundo paso es separar los números que están acompañados con la X y pasando al otro lado del igual los otros términos.
''')
st.latex("x^2-6x=8y+7")
st.markdown('''**Paso 3:** Nuestro tercer paso es completar el trinomio cuadrado perfecto, sin olvidar que lo que se suma en una parte del igual se debe sumar al otro lado también.
''')
st.latex("x^2-6x+9=8y+7+9")
st.markdown('''**Paso 4:** Ahora factorizamos nuestro trinomio perfecto cuadrado y sumamos los terminos independientes.
''')
st.latex("(x-3)^2=8y+16")
st.markdown('''**Paso 5:** Como en la forma canónica nuestra Y está en un parentesis y sola, sin ningun número, lo que tenemos que hacer es factorizar estos términos que están despue
s del igual.''')
st.latex("(x-3)^2=8(y+2)")
st.markdown('''Al finalizar todo esto podemos ver que obtenemos el vértice de una mánera más visual y practica, tenemos que nuestro vértice de esta parabola es''')
st.latex("V(3,-2)")
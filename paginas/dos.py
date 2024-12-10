import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.html("<center> <h1> Partes de la función </h1> </center>")
st.markdown('''
    Los elementos que conforman a una parábola son llamados vértice, foco, eje de simetría, directriz y el lado recto. Miraremos que significa cada parte que componen una parábola y como los podríamos hallar.
    ''')
st.subheader("**Vértice**")
st.markdown('''
     El vértice representado por la letra "V" es el punto extremo de la parábola, es decir, si la parábola abre hacía arriba entonces tenemos que su vértice es su punto extremo más bajo, pero de lo contrario, si la parábola es una curva que abre hacía abajo su vértice es el punto más alto, de la misma manera, una parábola puede puede abrirse hacía la izquierda o derecha, si abre hacía la izquierda su vértice se encontrará a la derecha pero si es abierta hacía la derecha su vértice será encontrado en el punto extremo en la izquierda.
      ''')
st.markdown(''' 
        **¿Cómo encontrar el vértice de una parábola?**
    Como vimos el vértice es el punto extremo de una parábola y todo punto de cualquier función tiene una coordenada en X y otra coordenada en Y. Para poder encontrar estas coordenadas tenemos que usar la formula
    ''')
st.latex(r"V(\frac{-b}{2a})")
st.markdown(''' 
        Con esta formula podemos hallar la coordenada en X del vértice de nuestra parábola, identificamos que parte de nuestra ecuación es "b" y también identificamos "a", al saber que números corresponden a estas letras nos queda reemplazar en la formula respetando los signos tanto de la formula como de la ecuación. Al conseguir nuestro valor en X tenemos que reemplazar el resultado en la función en cada parte en la que se encuentre la X, para así poder obtener nuestra coordenada en Y y tener el vértice completo.
    ''')
st.markdown(''' 
        **Ejemplo:** Tenemos nuestra función cuadrática.
    ''')
st.latex("f(x)=2x^2-8x+6")
#hacer que python me de esta grafica
st.markdown(''' 
        Identificamos que "a" en nuestra función corresponde al número "2" y que "b" es el número "-8". Nos queda reemplazar estos valores en la formula respetando los signos tanto de la ecuación como de la formula de la siguiente manera.
    ''')
st.latex(r"V(\frac{-(-8)}{2(2)})")
st.markdown(''' 
        Esto nos da como resultado "2", nuestro siguiente paso es reemplazar cada X de nuestra ecuación por el número "2" de la siguiente manera:''')
st.latex("f(x)=2(2)^2-8(2)+6")
st.markdown(''' 
        Al hacer las respectivas operaciones nos da como resultado "-2", esto quiere decir que nuestro vértice sería "v(2,-2)"''')
c1, c2 = st.columns(2)
with c1: 
   st.latex("f(x)=2x^2-8x+6")
with c2:
   

    # Parámetros de la función cuadrática (puedes cambiarlos si es necesario)
    a = 2
    b = -8
    c = 6

    # Definir la función cuadrática
    def f(x):
        return a * x**2 + b * x + c

    # Calcular el vértice de la parábola
    vertice_x = -b / (2 * a)
    vertice_y = f(vertice_x)

    # Crear los datos para la gráfica
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)

    # Crear la figura de la gráfica
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=r'$f(x) = ax^2 + bx + c$')
    ax.scatter(vertice_x, vertice_y, color='red', zorder=5, label=f'Vértice ({vertice_x:.2f}, {vertice_y:.2f})')
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.legend()

    # Mostrar la gráfica
    st.pyplot(fig) 



st.subheader("**Foco**")
st.markdown('''
     El foco nombrado con la letra "P" es un punto fijo que se encuentra dentro de la parábola y también en el eje de simetria. El foco se puede definir como la distancia que posee cada punto de la parábola hasta la recta llamada directriz.
     ''')
st.markdown(''' 
        **¿Cómo encontrar el foco de una parábola?**
    Lo primero que debemos hacer es pasar nuestra formula general a la forma canonica de la parábola, es decir a la forma 
    
        ''')
st.latex("(x-h)^2 = 4p (y-k)")
st.markdown(''' 
        En donde "p" es nuestro foco, que se multiplica por 4, podemos entender, que para poder encontrar nuestro foto tenemos que dividir nuestro número que está despues del igual entre 4
    
        ''')
st.markdown(''' 
        **Ejemplo:** Tenemos nuestra función cuadrática de forma canonica.
    ''')
st.latex("(x-2)^2 = 4 (y-3)")
st.markdown(''' 
        Nuestro número despues del igual es el 4, o sea, lo que tenemos que hacer es dividir este número entre 4, como ya lo habiamos mencionado. El resultado de dividir 4 entre 4 es 1, lo que quiere decir que nuestro foco "p" en nuestro ejemplo es 1.
    ''')
st.subheader("**Eje de simetria**")
c1, c2 = st.columns(2)
with c1:
    st.markdown('''
            El eje de simetria en una parábola es una recta vertical u horizontal (dependiendo de hacia donde abre la parábola) que divide nuestra parábola en dos mitades iguales y pasa por el vertice de nuestra parábola.
        ''')
    st.markdown(''' 
        **¿Cómo encontrar el eje de simetria de una parábola?**
  Para poder obtener nuestro eje de simetria, lo primero que tenemos que hacer es identificar si nuestra parábola abre hacía arriba, abajo o hacia la izquierda o derecha. Despues de saber esto lo que tenemos que hacer es encontrar nuestro vértice como ya lo hemos hecho anteriormente, si nuestra parábola abre hacía     ''')
    
with c2:
    st.image("https://flamath.com/wp-content/uploads/eje-de-simetria-1.webp")
st.markdown('''arriba o hacia abajo nuestro eje de simetria debe pasar por nuestro vertice de forma perpendicular al eje x, pero si al contrario, nuestra parábola abre hacia la derecha o hacia la izquierda, el eje de simetria también pasa por su vertice pero de forma perpendicular al eje y. ''')
st.subheader("**Directriz**")
st.markdown(''' 
        La directriz es la linea recta que se encuentra en frente de la parábola, o sea, afuera de ella, para poder representar a la directriz usamos la letra "d", la distancia que hay entre la directriz y el vértice es la misma distancia que tenemos desde el vértice y el foco
        ''')
st.markdown(''' 
        **¿Cómo encontrar la directriz de una parábola?**
para que podamos encontrar nuestra recta directriz tenemos que hacer encontrar nuestro foco, para saber que distancia tendra nuestra recta desde el vértice, también tenemos que hacer un procedimiento parecido al del eje de simetria. Tenemos que identificar hacia donde abre nuestra parábola, sea hacia arriba, abajo, derecha o izquierda, al tener esta información tomamos la misma distancia que tiene el vértice y el foco y la ponemos por fuera de nuestra parábola desde el vértice, es decir, si nuestra parábola abre hacia arriba o abajo nuestra directriz será perpendicular al eje X, pero si al contrario, nuestra parábola abre hacia izquierda o derecha nuestra directriz será perpendicular al eje Y.''')
st.subheader("**Lado recto**")
c1, c2 = st.columns(2)
with c1:
    st.markdown(''' 
            El lado recto de una parábola es un segmento perpendicular al eje de simetria, es perpendicular al eje de la parábola y sus extremos tocan la parábola, este lado recto es 4 veces la longitud de la distancia focal''')
    st.markdown(''' 
            **¿Cómo encontrar el lado recto de una parábola?**
    Para poder encontar nuestro lado recto lo que tenemos que hacer es simplemente una operación.''')
    st.latex("Ld = 4p")
with c2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/Par%C3%A1bola-lado_recto.svg")

st.markdown(''' 
            Lo que esta formula nos quiere decir es que el lado recto equivale a 4 veces la distancia que hay entre el foco al vétice. Esta longitud siempre está representada en la ecuación canónica después del signo igual''')

st.markdown(''' 
        **Ejemplo:** Tenemos nuestra ecuación de la forma canónica de forma:
''')
st.latex("(x-2)^2 = 4 (y-3)")
st.markdown(''' 
       Por lo que podemos concluir de este ejemplo es que nuestro lado recto equivale a 4.
''')
st.subheader("¿En que influye el lado recto?")
st.markdown('''Agrega el valor que desees para el lado recto de la parábola y mira como cambia''')
st.latex("f(x)=x^2")
c1, c2 = st.columns(2)
with c1:
    st.markdown("### Ingrese el valor del Lado Recto de la Parábola:")
    
    
    lado_recto = st.number_input("Lado Recto (p):", min_value=0.1, max_value=1000.0, value=1.0, step=0.1)


    def parabola_x_to_y(x, p):
        return (x**2) / (4 * p)

with c2:   
    x_vals = np.linspace(-10, 10, 400)  # Valores de x
    y_vals = parabola_x_to_y(x_vals, lado_recto)  

        
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=r'$y = \frac{x^2}{4p}$')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
        
        # Fijar los límites del eje y para que no cambien
    ax.set_ylim(0, 10)
        
    ax.set_title(f'Parábola con Lado Recto p = {lado_recto}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

        # Mostrar la gráfica en Streamlit
    st.pyplot(fig)
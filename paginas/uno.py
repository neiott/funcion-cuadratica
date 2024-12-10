import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.html("<center> <h1> Función cuadrática </h1> </center>")
st.subheader("Definición e historia")
st.markdown('''
   Una **función cuadrática**, o también conocida como una **parábola**, es aquella función polinómica de segundo grado. Es decir, su mayor exponente es al cuadrado. La función cuadrática tiene la forma
    ''')
st.latex("f(x)=ax^2+bx+c")

st.markdown('''
    La parábola "principal" está definida por:
    ''')
st.latex("y=x^2")
st.markdown('''
    Esta función cuadrática se logra ver de la siguiente manera
    ''')



a= 1
b = 0
c = 0

    
def f(x):
    return a * x**2 + b * x + c



# Crear los datos para la gráfica
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

    
fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label=r'$f(x) = x^2 $')
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.legend()

# Mostrar la gráfica
st.pyplot(fig)



#grafica de la funcion cuadratica principal


st.markdown('''
    Esta función, al tener su variable más importante elevada al cuadrado, logra verse  su gráfica como una curva en forma de U.  Como lo podemos ver en este ejemplo:
    ''')
c1, c2 = st.columns(2)
with c1:   
    st.subheader("Ejemplo")
    st.latex("f(x)=x^2+8x+16")

with c2:
    a= 1
    b = 8
    c = 16

    
    def f(x):
        return a * x**2 + b * x + c

    

    
    x_vals = np.linspace(-15, 7, 400)
    y_vals = f(x_vals)

    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=r'$f(x) = x^2 $')
    
    ax.axhline(0, color='black',linewidth=1)
    ax.axvline(0, color='black',linewidth=1)
    ax.legend()

    # Mostrar la gráfica
    st.pyplot(fig)




st.markdown('''
    En donde "a" es el valor que está acompañando a la x cuadrada, "b" lo podemos ver como el valor que está con la x y "c" es el término independiente.
    ''')
st.markdown('''
    También podemos definir la parábola como el lugar geométrico de todos aquellos puntos que se encuentran a la misma distancia del foco y de la directriz.
    ''')


#grafica de la parabola del ejemplo


st.subheader("Un poco de historia")
c1, c2 = st.columns(2)
with c1:
    st.markdown('''
            En la historia de la función cuadrática fueron varias las culturas que manifestaron una consideración de situaciones cuadráticas.
        ''')
    st.markdown('''**Babilonia**: En esta cultura, las naciones cuadráticas se encontraron asociadas a situaciones en donde el concepto de cuadrado tenía una concepción aritmetica, usaban las funciones cuadráticas en situaciones como *Hallar un número tal que sumado a su inverso dé un número dado*, esto los conducía a una ecuación cuadrática.''')
with c2:
    st.image("https://www.geometriaanalitica.info/wp-content/uploads/2020/08/ecuacion-de-la-parabola.jpg?ezimgfmt=rs:364x364/rscb2/ng:webp/ngcb2")
st.markdown('''

**Grecia**: Los griegos marcaron un hito más importante en la construcción de las nociones cuadráticas. La Grecia tenía la función cuadrática con un carácter aritmético, la escuela pitagórica estableció razonamientos númericos para sucesiones y progresiones.
        ''')


# Contenedor principal
with st.container():
    st.subheader("Crea tu función cuadrática")
    
    st.markdown("Utiliza los deslizadores para elegir el valor que tu quieras para los coeficientes de la ecuación, te mostrarán su vértice, gráfica y ecuación.")

# Deslizadores para los coeficientes de la función cuadrática
c1, c2 = st.columns(2)

# Primera columna: Deslizadores para los coeficientes a, b, c
with c1:
    st.markdown("### Ajusta los coeficientes de la función cuadrática")
    a = st.slider('Coeficiente a', min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
    b = st.slider('Coeficiente b', min_value=-10.0, max_value=10.0, value=-2.0, step=0.1)
    c = st.slider('Coeficiente c', min_value=-10.0, max_value=10.0, value=1.0, step=0.1)

# Definir la función cuadrática
def f(x):
    return a * x**2 + b * x + c

# Calcular el vértice de la parábola
vertice_x = -b / (2 * a)
vertice_y = f(vertice_x)

# Crear los datos para la gráfica
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

# Segunda columna: Mostrar la gráfica
with c2:
    
    
    # Crear la figura de la gráfica
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=r'$f(x) = ax^2 + bx + c$')
    
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.legend()

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)

    st.latex(f"f(x) = {a}x^2 + ({b}x) + {c}")









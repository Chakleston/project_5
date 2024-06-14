import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV del conjunto de datos
car_data = pd.read_csv(
    'C:/Users/Carlos Gonzalez Mena/Desktop/Triple Ten/projects/project_5/vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis Exploratorio de Datos de Vehículos Usados')

# Crear botones para construir gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Acción al hacer clic en el botón de histograma
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Acción al hacer clic en el botón de gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Usar casillas de verificación en lugar de botones
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Construcción de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write(
        'Construcción de un gráfico de dispersión para las columnas odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

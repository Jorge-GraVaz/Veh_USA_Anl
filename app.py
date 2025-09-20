import streamlit as st
import pandas as pd
import plotly.express as px

vehicle_data = pd.read_csv(
    "D:\\Data Analyst\\Sptint 7\\Veh_USA_Anl\\Veh_USA_Anl\\vehicles_us.csv")  # leer los datos

st.header(
    f"📊 Análisis de vehículos en EE.UU. — {len(vehicle_data):,} registros y {len(vehicle_data.columns)} columnas")

hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(vehicle_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')  # crear un botón
if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje')
    # crear un histograma
    fig_scatter = px.scatter(vehicle_data, x="odometer",
                             y="price", title="Precio vs Kilometraje", opacity=0.5)
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

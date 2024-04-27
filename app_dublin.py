
# --------------------LIBRERÍAS----------------------------#
import os
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import joblib
import datetime
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import folium




# --------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
st.set_page_config(
    page_title="air bnb",
    page_icon= "🇮🇪",
    layout="wide", #centered, wire
    initial_sidebar_state="expanded" #auto, collapsed, expanded
)

logo = "Streamlitapp\Imágenes\Dublín.png"




# --------------------COSAS QUE VAMOS A USAR EN TODA LA APP----------------------------#

df1 = pd.read_csv("C:\\Users\\alede\\Desktop\\PRIMER_PROYECTO\\Streamlitapp\\Datos\\calendar_df.csv")
df2 = pd.read_csv("C:\\Users\\alede\\Desktop\\PRIMER_PROYECTO\\Streamlitapp\\Datos\\listing_df.csv")
df3 = pd.read_csv("C:\\Users\\alede\\Desktop\\PRIMER_PROYECTO\\Streamlitapp\\Datos\\neighbourhoods_df.csv")
df4 = pd.read_csv("C:\\Users\\alede\\Desktop\\PRIMER_PROYECTO\\Streamlitapp\\Datos\\reviews_df.csv")
df5 = pd.read_csv(r"C:\Users\alede\Desktop\PRIMER_PROYECTO\SEGUNDO_PROY\listing_df.csv1")




# --------------------HEADER----------------------------#
st.image(logo, width=250)
st.title("Conoce Dublin al mejor precio")
st.subheader("Para el gobierno de Irlanda, Dublín es una ciudad crucial y estratégica, donde se implementan diversas iniciativas para atraer a un mayor número de visitantes cada año.")


#---------------Imagenes Dublin-----------#
imagenes = ["Streamlitapp\Imágenes\Dublín Grafton Street (1).png", "Streamlitapp\Imágenes\Dublín Grafton Street (2).png", "Streamlitapp\Imágenes\Dublín Grafton Street (3).png","Streamlitapp\Imágenes\Dublín Grafton Street.png" ]

# Mostrar imagenes
st.image(imagenes, width=500)





#-------PANEL INTERACTIVO---#
def generar_iframe():
    codigo_insercion = """
    <iframe title="AirBnb" width="100%" height="600" 
    src="https://app.powerbi.com/view?r=eyJrIjoiN2I1YWQ4ODAtMGQ5OS00YzdjLWJhZTYtMjU1NWExN2I3ZjM0IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" 
    frameborder="0" allowFullScreen="true"></iframe>
    """
    return codigo_insercion

# Título en la barra lateral
st.sidebar.title("Panel Interactivo")

# Casilla de verificación para mostrar el panel interactivo
mostrar_panel_principal = st.sidebar.checkbox("Mostrar Panel Interactivo")

# Coloca esto al principio para que aparezca primero
if mostrar_panel_principal:
    st.markdown(generar_iframe(), unsafe_allow_html=True)
# --------------------SIDEBAR----------------------------#
st.sidebar.image(logo, width=120)
st.sidebar.title("Programa tu viaje")
st.sidebar.write("-------------")



# --------------------FILTRO CALENDARIO----------------------------#
min_date = datetime.date(2024, 1, 1)
max_date = datetime.date(2025, 12, 31) #para que muestre hasta el año 2025

calendario = st.sidebar.date_input(
    "Selecciona tus vacaciones para el próximo año",
    value=(min_date, min_date), 
    min_value=min_date,
    max_value=max_date,
    format="YYYY-MM-DD"
)


#-----------------------FILTROS ELEGIR PROPIEDAD, PRECIO Y DESTINO--------------------------------#
#Primero filtra tipos de barrios
barrios = df5['neighbourhood'].unique()
barrio_seleccionado = st.sidebar.selectbox('Selecciona en qué barrio quieres vivir', barrios)

#Mostrar los tipos de propiedades en el sidebar
propiedades_barrio = df5[df5['neighbourhood'] == barrio_seleccionado]
if propiedades_barrio.shape[0] > 0:
    tipos_propiedades = propiedades_barrio['property_type'].unique()
    tipo_seleccionado = st.sidebar.selectbox('Selecciona el tipo de propiedad', tipos_propiedades)
 # Convertir los precios a un formato numérico
    propiedades_barrio['price_list'] = propiedades_barrio['price_list'].replace('[\$,]', '', regex=True).astype(float)
 # Rango de precios
    precio_minimo = int(propiedades_barrio['price_list'].min())
    precio_maximo = int(propiedades_barrio['price_list'].max())
# Crear una linea que muestre el rango de precio en el sidebar
    rango_precio = st.sidebar.slider('Selecciona el rango de precio', precio_minimo, precio_maximo, (precio_minimo, precio_maximo), step=10000)
        
#--------------------FILTRO MOSTRAR LAS PROPIEDADES----------------------#
# Título para la sección de mostrar propiedades
st.title('Explora tu nueva casa')

# Primero se relacionan los precios y los tipos de propiedades
propiedades_filtradas = propiedades_barrio[(propiedades_barrio['price_list'] >= rango_precio[0]) & (propiedades_barrio['price_list'] <= rango_precio[1])]

# Mostrar fotos de las propiedades filtradas en un diseño de cuadrícula
if propiedades_filtradas.shape[0] > 0:
    num_columns = 3  # Número de columnas
    col_width = st.sidebar.checkbox("Ancho de las columnas ajustable", False)
    
    # Crear columnas para mostrar las imágenes
    columns = st.columns(num_columns)
    
    # Agregar CSS para el efecto de zoom
    css_code = """
        <style>
            img:hover {
                transform: scale(1.1);
            }
        </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)
    
    for i, row in enumerate(propiedades_filtradas.iterrows()):
        # Obtener el índice de la columna actual
        column_index = i % num_columns
        
        # Mostrar la imagen en la columna correspondiente
        with columns[column_index]:
            # Mostrar la imagen con el enlace
            st.image(row[1]['picture_url'], caption=f"Propiedad en {row[1]['neighbourhood']}, {row[1]['property_type']}, Precio: ${row[1]['price_list']}")



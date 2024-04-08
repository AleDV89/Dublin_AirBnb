# Dublin Airbnb ✈️
En este repositorio encontrarás sobre el análisis de los datos Air Bnb de la ciudad de Dublín. Se investiga quién, cuándo y cómo se alquila en Airbnb Dublín.

![logo](https://private-user-images.githubusercontent.com/161485153/320519436-1ea31b8f-1751-401a-ad5d-d999950d1824.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTI1ODY1NTAsIm5iZiI6MTcxMjU4NjI1MCwicGF0aCI6Ii8xNjE0ODUxNTMvMzIwNTE5NDM2LTFlYTMxYjhmLTE3NTEtNDAxYS1hZDVkLWQ5OTk5NTBkMTgyNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQwOFQxNDI0MTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZTFlZDJiOTAzNmIxNWU3MDE1OWVkODZiODIwZTE1NzBhNGU0YjIyNTgwZTJjMzUyNjM4ZTdjZjZjNWJhN2JmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.HltR0cnJlzi6toELSztLzM1L3faZrOq382GMC4T0yXo)

### 🔍 Obtención de Datos:

En este análisis exploratorio se utilizó la base de datos de: 
[url_air_bnb](https://insideairbnb.com/get-the-data)

📚 PDFS:

[PDF1](https://www.dublincity.ie/sites/default/files/2023-12/dublin-city-council_tourism-strategy_online_aw_sml.pdf)

### 🧪 Requisitos: 
`pandas` , `numpy` , `seaborn`, `plt`, `os`, `streamlit`, `PyPDFLoader` , ` Chroma` ,
` ChatOpenAI` , `StrOutputParser` , `RunnablePassthrough` , `gr`, `PdfFileReader`

### 🕵️‍♂️ Estructura del proyecto

El proyecto está compuesto por:
* Procesamiento de datos.
* Limpieza de datos.
* Análisis Exploratorio de datos.
* Interpretación de escenarios.
* Visualización de datos en Power Bi.
* Desarrollo de App con Streamlit.

  #### 📊 Procesamiento de los Datos

  Todos los datos se cargan en un DF de pandas y se procede a la lectura del mismo.
  Uno de los archivos es Geojson y se utilizará para elaborar los mapas.
  Además:
  ✔️ Se verifican los nulos de cada DF
  usando el código:
  ```python
  .duplicated().sum()
  ```
  ✔️Número de columnas y filas
  ✔️ Info y tipo de dato

  #### 🧹 Limpieza de Datos
  Se eiminan las columnas con datos duplicados usando el código:
  ```python
  .drop_duplicates
  ```
Se encuentran varias columnas con datos NaN
se identifican cuales son usando:
  ```python
.isna().any()
   ```

Se vuelve a eliminar columnas que tengan 100% NaN

💡 Muchas columnas tienen el mismo nombre pero no todas tienen los mismos contenidos
Este código ayudó a poder comparar los contenidos entre DF y columnas
```python
pd.merge(df, on='columna', how='inner')

coincidencias = len(neig_comparado) > 0
print(coincidencias)
```
(Recuerda reemplazar los nombres con los de tus datos)

### 📊 Análisis Exploratorio de los Datos

1- Analizar la distribución de los barrios
```python
[barrios].value_counts(normalize=True)
```
Resultado: Todos los barrios cuentan con la misma distribución

2- Tratamiento de la columna # Tratamiento de la columna `reviews_per_month`
```python
.fillna({'reviews_per_month':0}, inplace=True)
```

### 📈 Correlación de las variables

[correl](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140736746)

##### Se correlacionan las variables: `reviews` y `tipo de propiedad` 

* 'calculated_host_listings_count_entire_homes' el alquiler de casas o pisos enteros tiene más relación con 'review_scores_location' y menos relacion con 'review_scores_value'
* 'calculated_host_listings_count_private_rooms' el alquiler de habitaciones privadas tiene más relación con 'review_scores_cleanliness' (aunque sea negativo entre todos los reviews es el que más cerca del 1 está) y menos relación con 'review_scores_location'
* 'calculated_host_listings_count_shared_rooms' alquiler de habitaciones compartidas tiene más relación con 'review_scores_checkin' y menos que 'review_scores_cleanliness'
- En conclusión: no tienen mucha correlacion las variables analizadas ya que todos estan por debajo del 1. Entre los tres el ultimo se puede decir que tiene un poco más de correlación



### 📈 Conteo de palabras que más se repiten en la columna `comentarios` con `WordCloud`

[graf_pal](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140736941)

Tambien se utiliza la función.value_count() y se verifica cuantas veces se usan las palabras
* Very se usa_ 103.062 veces
* Great se usa 60.801
* Location se usa 37.336

  
### 📈 Se visualizan los barrios y sus importancias
[barrios](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140737155)

Dublín cuenta con cuatros barrios
Con el gráfico se observa que hay más viviendas en Dublin City comparando con los otros barrios.


### 🏰 Clasificación según tipo de viviendas
[tipos de viviendas](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140737248)

Se observan cuatro tipos de viviendas y del tipo enteras son las que se observa mayor cantidad.

### 📊 Visualización de tipos de barios y viviendas disponibles todo el año
[box](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140737496)

Según el gráfico diagrama de caja se visualiza la distribución y la variablidad de los 4 barrios de Dublin con la variable disponible 365 días. 
Con respecto a la dispersión de los datos en las cuatro cajas se observa la linea donde se centran los datos representando el rango intercuartil más alto el barrio Dn Laoghaire-Rathdown es la linea dentro de la caja más alta, quiere decir que la media de sus datos es mayor a la de los demás. 
Aunque la variablididad entre grupos es bastante similar excepto en Dublin City.

### 📊 Mapa de los grupos de barrio

[mapa](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140737582)


### 📊 Mapa de tipos de habitación por barrio

[room](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140737640)


### 📊 Disponibilidad de habitaciones según disponibilidad
Este gráfico es muy interesantes porque no todas las viviendas están disponibles todo los dias. 
Con este gráfico se puede ver por medio de puntos y colores donde y cuantos hay. 


[dispo](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140737731)

# Streamlit App

El primer paso para crear la App es guardar los df limpios en archivos csv 
```python
.to_csv('nombre', sep=';', header=True, index=False)
```
[portada](https://github.com/AleDV89/Dublin_AirBnb/commit/5c2df8c800bdf44527abe7e9d403fc436a1e8497#commitcomment-140738115)




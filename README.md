# Dublin Airbnb ✈️
En este repositorio encontrarás sobre el análisis de los datos Air Bnb de la ciudad de Dublín. Se investiga quién, cuándo y cómo se alquila en Airbnb Dublín.

![logo](https://private-user-images.githubusercontent.com/161485153/320519436-1ea31b8f-1751-401a-ad5d-d999950d1824.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTI1ODY1NTAsIm5iZiI6MTcxMjU4NjI1MCwicGF0aCI6Ii8xNjE0ODUxNTMvMzIwNTE5NDM2LTFlYTMxYjhmLTE3NTEtNDAxYS1hZDVkLWQ5OTk5NTBkMTgyNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQwOFQxNDI0MTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZTFlZDJiOTAzNmIxNWU3MDE1OWVkODZiODIwZTE1NzBhNGU0YjIyNTgwZTJjMzUyNjM4ZTdjZjZjNWJhN2JmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.HltR0cnJlzi6toELSztLzM1L3faZrOq382GMC4T0yXo)

### 🔍 Obtención de Datos:

En este análisis exploratorio se utilizó la base de datos de: 
[url_air_bnb](https://insideairbnb.com/get-the-data)

📚 PDFS:

[PDF1](https://www.dublincity.ie/sites/default/files/2023-12/dublin-city-council_tourism-strategy_online_aw_sml.pdf)

## Ver notebbok con códigos utiizados
[Códigos](https://github.com/AleDV89/Dublin_AirBnb/blob/main/%5BSOLUCIONES%5D%5BEjercicio%201%5D%20AirBnb.ipynb)

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

### 📈 Gráficos y Códigos en el notebook 
[Códigos](https://github.com/AleDV89/Dublin_AirBnb/blob/main/%5BSOLUCIONES%5D%5BEjercicio%201%5D%20AirBnb.ipynb) 

# Streamlit App

[Códigos_App](https://github.com/AleDV89/Dublin_AirBnb/blob/main/app_dublin.py)

El primer paso para crear la App es guardar los df limpios en archivos csv 
```python
.to_csv('nombre', sep=';', header=True, index=False)
```

* Portada de la página
![portada](images/app1.png.png)







  






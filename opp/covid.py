# import requests as req 
import json
import funcovid  
import time
import os
from std import Estadistica
# import matplotlib.pyplot as plt

cwd = os.path.dirname(__file__)


# Traigo la información de internet y escribo el json

# res = req.get("https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json").json()
# with open("./opp/covid_data.json", "w", encoding="utf8") as file:
#     json.dump(res,file, indent=4, ensure_ascii=False)

# Leo el json que he escrito bajo el nombre de covid_data.json

with open(f"{cwd}/covid_data.json", "r", encoding="utf8") as file:
    data = json.load(file)["data"]

# 1. Cantidad total de municipios. Creo una lista con los municipios a una fecha dada. Quito la hora de la fecha con [0:10] para que no me afecte la hora

fecha = "2020/07/01 09:00:00"
mun1 = funcovid.get_by_date(fecha, data)

print(f"La cantidad total de municipios es: {len(mun1)}")

# 2. confirmados totales a 26-FEB-2020. Uso la formula anterior:

fecha1 = "2020/02/26 09:00:00"
mun26feb = funcovid.get_by_date(fecha1, data)
cases_26feb = funcovid.get_total_cases(mun26feb)
print(f"Los casos totales a {fecha1} son: {cases_26feb} ")

# 3. confirmados totales a 1-JUL-2020

fecha2 = "2020/07/01 09:00:00"
mun1jul = funcovid.get_by_date(fecha2, data)
cases_1jul = funcovid.get_total_cases(mun1jul)
print(f"Los casos totales a {fecha2} son: {cases_1jul} ")

# 4. Obtener los 10 municipios con mayor cantidad de confirmados totales

rank = 10
mun1jul_ok = funcovid.get_key_total_cases(mun1jul)
worst_mun = funcovid.get_worst_muns(mun1jul_ok)
funcovid.print_pretty((worst_mun[0:rank]))

# 5. Crear una lista con la sumatoria de los casos confirmados totales por día. (Al final creamos un diccionario)


Y = funcovid.create_y(data)
Y = dict(sorted(Y.items(), key=lambda tupla: tupla[0]))
dates = list(Y.keys())
Y = list(Y.values())
X = [num for num in range(1, len(Y)+ 1)]

covid_data = Estadistica(X,Y)


# Observamos la gráfica para encontrar en que rango es más lineal. A parti del día 65 más o menos tiene un comportamiento lineal.
# Cogemos los datos del X e Y a partir del día 65 y generamos nuestra predicción.

Y_a65 = Y[66:]
X_a65 = [num for num in range(67, len(Y)+ 1)]
# plt.plot(X_a65,Y_a65)
# plt.ylabel("Confirmados")
# plt.xlabel("Días")
# plt.show()

# Cuántos confirmados tendremos el 1 de agosto del año 2020?


after65 = Estadistica(X_a65,Y_a65)
# print(after65.rxy)
print(f"El día 20 de Agosto se estima que hayan: {after65.prediction(157)} casos de Covid-19 en Madrid")


# plt.plot(X,Y)
# plt.ylabel("Confirmados")
# plt.xlabel("Días")
# plt.show()
    












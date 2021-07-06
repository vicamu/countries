import requests as req
import funcs
import csv
import json


# Encontrar los 10 países mas grandes:

# res = req.get("https://restcountries.eu/rest/v2/all").json()

# user_rank = int(input("Introduzca el número de países mas grande que desea ver: "))
# funcs.bigger_countries(user_rank, res)


funcs.most_spoken()



continents = ["Europe", "Africa", "Asia", "Americas", "Oceania"]
user = 0
while user != "q":
    funcs.menu()
    user = input("\nSeleccione opción: ")
    if user == "1":
        user_countrie = input("\nIntroduzca el nombre del país que desea buscar: ")
        resultado = funcs.get_by_name(user_countrie)
        print(resultado)
        funcs.write_csv(resultado)

    elif user == "2":
        funcs.print_pretty(continents)
        user_continent = int(input("Seleccione el continente: "))
        try:
            population = funcs.get_population(user_continent,continents)
            print(f"La poblacion total del continente {continents[user_continent - 1 ]} es de {population}")
        except FileNotFoundError:
            resultado = funcs.get_by_continent(continents, user_continent)
            data = funcs.write_json(resultado,continents,user_continent)
            population = funcs.get_population(user_continent,continents)
            print(f"La poblacion total del continente {continents[user_continent - 1 ]} es de {population}")
        

    elif user == "3":
        user_language = input("Introduzca un idioma: ")
        iso_lan = funcs.get_iso_language(user_language)
        resultado = funcs.get_language_country(iso_lan)
        print(f"El número de paises que con idioma oficial '{user_language}' son: {resultado}")
        
    elif user == "4":
        user = input("Introduzca el país cuya bandera quiere descargar: ")
        country = funcs.get_by_name(user)
        funcs.get_flag(country)
    
    elif user == "5":
        print("----HISTORIAL----".center(50))
        funcs.read_csv()


    






 
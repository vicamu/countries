import requests as req
import csv
import json
import os
from languages import languages

real_path = os.path.dirname(__file__)

def menu():
    print("MENU".center(50))
    print("1. Buscar País: ")
    print("2. Buscar Continente: ")
    print("3. Paises por idioma: ")
    print("4. Descargar bandera: ")
    print("5. Historial: ")
    print("Q. Quit: ")


def print_pretty(data):
    for i , con in enumerate(data):
        print(f"{i + 1}. {con}")

def bigger_countries(rank,data):
    res = [pais for pais in data if type(pais["area"]) == float]
    res_ordenado = sorted(res, key=lambda pais: pais["area"], reverse=True)
    print(res_ordenado[0:rank+1])

def most_spoken():
    res = req.get("https://restcountries.eu/rest/v2/all?fields=name;languages;").json()
    result = {} 
    for country in res:
        try:
            result[country["languages"][0]["name"]] += 1
        except KeyError:
            result[country["languages"][0]["name"]] = 1
    

    pais_mas_hablado = sorted(result.items(),key = lambda pais: pais[1], reverse=True)
    print(pais_mas_hablado[0])
        
        


  

def get_by_name(user):
    res = req.get(f"https://restcountries.eu/rest/v2/name/{user}").json()

    if type(res) == list:
            print(f"\nSe ha encontrado 1 país: ")
            return [res[0]["name"],res[0]["capital"],res[0]["region"],res[0]["population"],res[0]["area"],res[0]["languages"][0]["name"], res[0]["flag"]]  
    
    elif type(res) == dict:
        return res["message"]
        
def get_by_continent(continents, user_continent):
    if user_continent == int and user_continent < 5:

        res = req.get(f"https://restcountries.eu/rest/v2/region/{continents[user_continent - 1]}").json()
        return res


def write_csv(data):
    if type(data) == list:
        with open("./countries/historial.csv", "a",encoding="utf8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)

def write_json(resultado, continents, user_continent):
    if type(resultado) == list:
        with open(f"./countries/{continents[user_continent - 1]}.json", "w",encoding="utf8") as file:
            json.dump({"data": resultado}, file, ensure_ascii=False, indent=4)

def get_population(user_continent, continents):
    resultado = 0
    with open(f"{real_path}/{continents[user_continent - 1]}.json", "r", encoding="utf8") as file:
        data = json.load(file)["data"]
    for pais in data:
        resultado += pais["population"]
    return resultado


def get_language_country(user_language):
    for language in languages:
        if language[1].lower().find(user_language) == 0:
            lan = (language[0])
    return lan

def get_iso_language(iso_language):

    result = req.get(f"https://restcountries.eu/rest/v2/lang/{iso_language}").json()
    return result

def get_flag(country):
    if country != "Not Found" :
        res = req.get(f"{country[-1]}").content
        with open(f"{real_path}/img/{country[0]}.svg", "wb") as file:
            file.write(res)
    else:
        print("Country not found")
        
def read_csv():
    resultado = []
    with open(f"{real_path}/historial.csv", "r", encoding="utf8") as file:
        data = csv.reader(file)
        for row in data:
            if row[0] != "name":
                print(f"name: {row[0]}    /    population: {row[3]}")

    



    
    


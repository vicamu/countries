class Mun:
    def __init__(self, ine_code, sup_km2, den_km2):
        self.ine_code = ine_code
        self.sup_km2 = sup_km2
        self.den_km2 = den_km2

    def population(self):
        return self.sup_km2 * self.den_km2


municipio_1 = {
    "codigo_ine": "280006",
    "sup_km2": 5,
    "den_km2": 3.72
}

municipio_2 = {
    "codigo_ine": "28007",
    "sup_km2": 3,
    "den_km2": 5.72
}

obj_municipio_1 = Mun("280006", 5, 3.72)
obj_municipio_2 = Mun("28007", 4, 10)


class Human:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    
    def IMC(self):
        return (self.weight * self.height)/2
    def h20(self):
        return (self.weight)

andres = Human("Andres", 70, 1.76)
renzo = Human("Renzo", 76.4, 1.87)


print(f"IMC DE ANDRES: {andres.IMC()}" )
print(f"IMC DE RENZO: {renzo.IMC()}" )

for human in list_humans:
    result = 0
    a = Human(human["name"], human["weight"], human["height"])
    result += a.IMC()
    print(sum(result)/len(result))

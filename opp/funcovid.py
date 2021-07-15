def print_pretty(data):
    for i,mun in enumerate(data):
        print(f"{i+1}. {mun['municipio_distrito']}: {mun['casos_confirmados_totales']}")

def get_by_date(date,data):
    result = [] 
    for mun in data:
        if mun["fecha_informe"].split(" ") == date.split(" "):
            result.append(mun)
    return result

def get_total_cases(muns):
    result = 0
    for mun in muns:
        try:
            result += mun["casos_confirmados_totales"]
        except KeyError:
            result += 0
    return result

def get_key_total_cases(data):
    result = []
    for mun in data:
        try:
            if type(mun["casos_confirmados_totales"]) == int:
                result.append(mun)
        except:
            continue
    return result
  


def get_worst_muns(data):
    try:
        result = sorted(data, key=lambda mun: mun["casos_confirmados_totales"], reverse=True)
    except KeyError:
        next 
    return result

# Función que crea un diccionario cuyas claves son las fechas y los valores los casos totales por cada fecha. La función va creando las claves y si no existen maneja el error y las crea.

def create_y(data):
    result = {}
    for mun in data:
        date = mun["fecha_informe"].split(" ")[0]
        try:
            result[date]
            try:
                result[date] += mun["casos_confirmados_totales"]
            except KeyError:
                continue                
        except KeyError:
            try:
                result[date] = 0
                result[date] += mun["casos_confirmados_totales"]
            except KeyError:
                continue
    return result

    
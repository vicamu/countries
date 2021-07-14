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

def get_sum_by_date(data):
    count = 0
    result = {}

    fecha = "2020/03/02"
    for mun in data:
        control = True
        if "2020/03/02" == fecha:
            try:
                count += mun["casos_confirmados_totales"]
            except KeyError:
                control = False
        elif control:
            result[fecha] = count
            count = 0
            fecha = "2020/03/02"
            control = True
    for k,v in result.items():
        print(f"{k}: {v}")

    print(len(result))

    

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

def get_worst_muns(rank,data):

    try:
        result = (sorted(data, key=lambda mun: mun["casos_confirmados_totales"], reverse=False))
    except KeyError:
        next 
    return result


    
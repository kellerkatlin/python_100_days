capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
}

# Lista anidada en el diccionario

# travel_log = {
#     "Francia": ["Paris", "Lille", "Dijon"],
#     "Alemania": ["Berlin", "Hamburg", "Stuttgart"],
# }

# print(travel_log['Francia'][1])
# Lista de diccionarios en un diccionario 



# nested_list = ["a", "b", [ "c", "d"]]
# print(nested_list[2][0])

travel_log = {
    "Francia": {
        "total_visitas": 12,
        "ciudades_visitadas": ["Paris", "Lille", "Dijon"], },
    "Alemania": {
        "total_visitas": 5,
         "ciudades_visitadas": ["Berlin", "Hamburg", "Stuttgart"], },
}
print(travel_log["Alemania"]["ciudades_visitadas"][0])
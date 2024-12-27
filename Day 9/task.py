programing_dictionary = { 
    "Bug": "Un error en un programa que previene que funcione correctamente",
    "Function": "Un pedazo de código que puedes reusar",
}


print(programing_dictionary["Bug"] )

programing_dictionary["Loop"] = "La acción de hacer algo repetidamente de manera rápida"

print(programing_dictionary)

# Crear un diccionario vacio

# empty_dictionary = {}
# programing_dictionary= empty_dictionary
# print(programing_dictionary)

# Editar un item en un diccionario
programing_dictionary["Bug"] = "Un mosquito en tu computadora"
print(programing_dictionary)

# Loop a través de un diccionario

for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])   
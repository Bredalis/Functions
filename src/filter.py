
# Filtrar edades menores o iguales a 18
edades = [1, 12, 19, 30, 23, 35, 11]
edades_menores = list(filter(lambda x: x <= 18, edades)) 

print(f"Edades menores o iguales a 18: {edades_menores}")
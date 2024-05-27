
# El conjunto Set

nombres_1 = {"Juan", "Pedro", "Juan", "Pedro"}
nombres_2 = {"Luis", "Maria", "Rosa"}

print("Sets:", nombres_1, nombres_2)
print("Tipos:", type(nombres_1), type(nombres_2))

# Agregar datos

nombres_1.add("Luis")
nombres_2.add("Jose")

# Borrar

nombres_2.remove("Luis")

# Union o merge

nombres = nombres_1.union(nombres_2)

print("\nSet 2:", nombres_2)
print("Union de Sets:", nombres)

ambos_nombres = nombres_1.intersection(nombres_2)
print("\nDatos comunes del Set:", ambos_nombres)

sin_repetidos = nombres.difference(ambos_nombres)
print(sin_repetidos)

print("\nSi hay subconjuntos:", nombres_2.issubset(nombres))
print("Si es un super Set:", nombres.issuperset(nombres_2))
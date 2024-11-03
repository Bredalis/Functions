
# Ejemplo de uso de conjuntos (set)
nombres_1 = {"Juan", "Pedro", "Juan", "Pedro"}
nombres_2 = {"Luis", "Maria", "Rosa"}

print("Sets:", nombres_1, nombres_2)
print("Tipos:", type(nombres_1), type(nombres_2))

# Agregar elementos
nombres_1.add("Luis")
nombres_2.add("Jose")

# Borrar un elemento
nombres_2.remove("Luis")

# Unión de conjuntos
nombres = nombres_1.union(nombres_2)

print("\nSet 2:", nombres_2)
print("Unión de sets:", nombres)

# Operaciones con conjuntos
ambos_nombres = nombres_1.intersection(nombres_2)
print("\nDatos comunes de los sets:", ambos_nombres)

sin_repetidos = nombres.difference(ambos_nombres)
print("Datos sin repiten en los sets:", sin_repetidos)

print("\n¿Es un subconjunto?:", nombres_2.issubset(nombres))
print("¿Es un superconjunto?:", nombres.issuperset(nombres_2))
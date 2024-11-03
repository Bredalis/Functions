
# Funciones anónimas (Lambda)
suma = lambda a, b: a + b
multiplicacion = lambda a, b, c: a * b * c
constante = lambda x: x

datos_de_personas = [("Juan", 89, 5), ("Lucia", 45, 10), ("Pedro", 23, 30)]

print("Estructura de datos:")
print("Lista desordenada:", datos_de_personas)

# Ordenar la lista de personas por la segundo posición (edad)
datos_de_personas.sort(key = lambda persona: persona[1])
print("Lista ordenada:", datos_de_personas)

print("\nOperaciones:")
print("Suma:", suma(2, 3))
print("Multiplicación:", multiplicacion(1, 2, 3))
print("Constante:", constante(3))
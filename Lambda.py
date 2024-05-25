
# Funciones cortas (Lambda)

suma = lambda a, b: a + b
multiplicacion = lambda a, b, c: a * b * c
constante = lambda x: x

datos_de_personas = [("Juan", 89, 5), ("Lucia", 45, 10), ("Pedro", 23, 30)]

print("Lista Desordenada:", datos_de_personas)
datos_de_personas.sort(key = lambda persona: persona[1])
print("Lista Ordenada:", datos_de_personas)

print("\nSuma:", suma(2, 3))
print("Multiplicacion:", multiplicacion(1, 2, 3))
print("Constante:", constante(3))

def decorador(funcion):
	"""Decora una función, mostrando un mensaje de inicio y fin."""

	def decorador_interno(parametro_1, parametro_2):
		print("Inicio")
		funcion(parametro_1, parametro_2)
		print("Final")

	return decorador_interno

@decorador
def potencia(base, exponente):
	"""Imprime el resultado de elevar la base al exponente."""
	print(pow(base, exponente))

potencia(1, 8)
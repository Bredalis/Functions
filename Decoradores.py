
def decorador(funcion):
	"""Decora una función, mostrando un mensaje de inicio y fin."""
	
	def decorador_interno():
		print("Inicio")
		funcion()
		print("Final")

	return decorador_interno

@decorador
def suma():
	"""Imprime el resultado de la suma 1 + 2."""
	print(1 + 2)

suma()
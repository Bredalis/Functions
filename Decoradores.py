
def decorador(funcion):
	def decorador_interno():

		print("Inicio")
		funcion()
		print("Final")

	return decorador_interno

@decorador
def suma():
	print(1 + 2)

suma()
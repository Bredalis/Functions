
def decorador(funcion):
	def decorador_interno(parametro_1, parametro_2):

		print("Inicio")
		funcion(parametro_1, parametro_2)
		print("Final")

	return decorador_interno

@decorador
def potencia(base, exponente):
	print(pow(base, exponente))

potencia(1, 8)
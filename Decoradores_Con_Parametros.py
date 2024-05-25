
def decorador(espacio):
	def funcion_interna(base, exponente):

		print("Inicio")
		espacio(base, exponente)
		print("Final")

	return funcion_interna

@decorador
def potencia(base, exponente):
	print(pow(base, exponente))

potencia(base = 1, exponente = 8)
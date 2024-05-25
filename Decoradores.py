
def decorador(espacio):
	def funcion_interna():

		print("Inicio")
		espacio()
		print("Final")

	return funcion_interna

@decorador
def suma():
	print(1 + 2)

suma()
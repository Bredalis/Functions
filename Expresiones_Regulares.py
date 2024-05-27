
import re

class BuscadorDePalabras:
	def __init__(self):

		self.cadena = input("Introduce una cadena de texto: ")
		self.texto_buscar = input("Introduce el texto que quieres buscar: ")

	def buscar(self):

		# Si se encontro la palabra o no

		if re.search(self.texto_buscar, self.cadena) is not None:
			print(f"Hemos encontrado la palabra: {self.texto_buscar}")

		else:
			print(f"No hemos encontrado la palabra: {self.texto_buscar}")

	def imprimir(self):
		print(f"Veces que se repite la palabra {self.texto_buscar}: {len(re.findall(self.texto_buscar, self.cadena))}")

if __name__ == "__main__":

	clase = BuscadorDePalabras()

	clase.buscar()
	clase.imprimir()
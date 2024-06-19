
import re

class BuscadorDePalabras:
	def __init__(self):

		self.cadena = input("Introduce una cadena de texto: ")
		self.texto_buscar = input("Introduce el texto que quieres buscar: ")

	def encontrar_palabra(self):
		buscar_palabra = re.search(self.texto_buscar, self.cadena)

		if buscar_palabra is None:
			print(f"No hemos encontrado la palabra: {self.texto_buscar}")
			return

		print(f"Hemos encontrado la palabra: {self.texto_buscar}")

	def cantidad_palabra(self):
		veces_palabra = len(re.findall(self.texto_buscar, self.cadena))
		print(f"Veces que se repite la palabra {self.texto_buscar}: {veces_palabra}")

if __name__ == "__main__":

	clase = BuscadorDePalabras()

	clase.encontrar_palabra()
	clase.cantidad_palabra()

import re

class BuscadorDePalabras:
	"""Clase para buscar una palabra en una cadena de texto y contar su frecuencia."""
	
	def __init__(self):
		self.cadena = input("Introduce una cadena de texto: ")
		self.texto_buscar = input("Introduce el texto que quieres buscar: ")

	def encontrar_palabra(self):
		"""Buscar una palabra en la cadena y muestra un mensaje si se encuentra."""
		resultado = re.search(self.texto_buscar, self.cadena)

		if resultado is None:
			return f"No hemos encontrado la palabra: {self.texto_buscar}"

		print(f"Hemos encontrado la palabra: {self.texto_buscar}")

	def cantidad_palabra(self):
		"""Cuenta cuántas veces se repite la palabra en la cadena."""
		frecuencia = len(re.findall(self.texto_buscar, self.cadena))
		print(f"Veces que se repite la palabra '{self.texto_buscar}': {frecuencia}")

if __name__ == "__main__":
	buscador = BuscadorDePalabras()
	buscador.encontrar_palabra()
	buscador.cantidad_palabra()
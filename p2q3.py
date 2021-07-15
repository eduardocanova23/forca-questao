class Forca:

	def __init__(self, palavra):
		self.palavra = palavra
		self.erros = []
		self.acertos = []

	def joga(self,letra):
		try:
			if type(letra) != str or len(letra) > 1 or letra in self.acertos:
				raise ValueError()
		except ValueError:
			return print("Palpite Inválido:", f"{letra}")

		if letra not in self.palavra:
			self.erros += letra
			print(self)
			try:
				if len(self.erros) == 6:
					raise IndexError()
			except IndexError:
				print("Você perdeu")
				quit()

		for x,y in enumerate(self.palavra):
			if y == letra:
				self.acertos += letra
				print(self)
				break

	def __repr__(self):
		self.display = ""
		for x,y in enumerate(self.palavra):
			if y in self.acertos:
				self.display += y
			else:
				self.display += "_"
		if self.display == self.palavra:
			print(self.display)
			print ("Você ganhou")
			quit()
		else:
			return self.display

	def start(self):
		while True:
			chute = input('Faça um palpite de letra: ').lower()
			f1.joga(chute)

strings = (input('Escolha uma palavra para a forca começar: ')).lower()
f1 = Forca(strings)

f1.start()

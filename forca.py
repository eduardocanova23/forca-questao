class Forca:

	def __init__(self, palavra):
		self.palavra = palavra
		self.erros = []
		self.acertos = []
		# Duas listas vazias sao criadas: uma de acertos e outra de erros

	def joga(self,letra):
		try:
			if type(letra) != str or len(letra) > 1 or letra in self.acertos:
				raise ValueError()
		except ValueError:
			return print("Palpite Inválido:", f"{letra}")
		# se o chute nao for uma letra ou tiver mais de um caractere,
		# é levantado um erro.

		if letra not in self.palavra:
			self.erros += letra
			print(self)
			try:
				if len(self.erros) == 6:
					raise IndexError()
			except IndexError:
				print("Você perdeu")
				quit()
		# tentativas maximas permitidas: 6

		for x,y in enumerate(self.palavra):
			if y == letra:
				self.acertos += letra
				print(self)
				break
		# avaliar acertos

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
		#formação de um display de amostragem do jogo

	def start(self):
		while True:
			chute = input('Faça um palpite de letra: ').lower()
			f1.joga(chute)
		# loop que roda o jogo

strings = (input('Escolha uma palavra para a forca começar: ')).lower()
f1 = Forca(strings)

f1.start()

from classes.image import Image


class Card:
	card_height = 300

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.swapping = False
		self.image = Image(f"img/cards/card{self.suit}{self.rank}.png", 0, Card.card_height)

	def __str__(self):
		return f"{self.rank} of {self.suit}"

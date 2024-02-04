import random
from classes.card import Card


class Deck:
	def __init__(self):
		self.reset_deck()

	def reset_deck(self):
		suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
		self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
		self.shuffle()

	def shuffle(self):
		random.shuffle(self.cards)

	def deal_cards(self, amount:int) -> list:
		dealt_cards = self.cards[:amount]
		self.cards = self.cards[amount:]
		return dealt_cards

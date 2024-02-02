import random


class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank


class Deck:
	def __init__(self):
		suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

	def shuffle(self):
		random.shuffle(self.cards)

	def deal_cards(self, amount:int):
		dealt_cards = self.cards[:amount]
		self.cards = self.cards[amount:]
		return dealt_cards


class Player:
	def __init__(self):
		self.hand = []


class Game:
	def __init__(self):
		self.deck = Deck()

	def start_game(self, player:Player):
		self.deck.shuffle()
		player.hand = self.deck.deal_cards(5)

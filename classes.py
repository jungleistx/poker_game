import random


class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"{self.rank} of {self.suit}"


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


	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n < len(self.hand):
			card = self.hand(self.n)
			self.n += 1
			return card
		else:
			raise StopIteration

	def __str__(self):
		return f"Hand:\n{', '.join(map(str, self.hand))}"


class Game:
	def __init__(self):
		self.deck = Deck()

	def start_game(self, player:Player):
		self.deck.shuffle()
		player.hand = self.deck.deal_cards(5)
		print(player)
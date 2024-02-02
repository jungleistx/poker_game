import random


class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"{self.rank} of {self.suit}"


class Deck:
	def __init__(self):
		self.reset_deck()

	def reset_deck(self):
		suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
		self.shuffle()

	def shuffle(self):
		random.shuffle(self.cards)

	def deal_cards(self, amount:int):
		dealt_cards = self.cards[:amount]
		self.cards = self.cards[amount:]
		return dealt_cards


class Hand(Card):

	def __init__(self, cards:list):
		super().__init__('', '')
		self.reset_cards(cards)

	def reset_cards(self, cards:list):
		self.ranks = {rank: 0 for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']}
		self.suits = {suit: 0 for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']}

		for card in self.cards:
			self.ranks[card.rank] += 1
			self.suits[card.suit] += 1

	def check_hand(self):
		pass

	def check_straight(self):
		pass

	def check_flush(self):
		pass

	def check_same_of_a_kind(self, amount:int):
		if amount in self.ranks.values():
			return True
		return False




class Player:
	def __init__(self):
		self.hand = []

	def check_hand(self):
		self.sort_hand()
		return Hand.check_hand()

	def sort_hand(self):
		def rank_value(card):
			rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
			return rank_order.get(card.rank, 0)
		self.hand.sort(key=lambda card: (rank_value(card), card.suit))

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
	def __init__(self, player:Player):
		self.player = player
		self.deck = Deck()

	def start_game(self):
		self.deck.reset_deck()
		self.player.hand = self.deck.deal_cards(5)
		print(self.player)
		print(self.player.check_hand())
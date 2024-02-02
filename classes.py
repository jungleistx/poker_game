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
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
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

	def count_cards(self):
		self.ranks = {rank: 0 for rank in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']}
		self.suits = {suit: 0 for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']}

		for card in self.cards:
			self.ranks[card.rank] += 1
			self.suits[card.suit] += 1

	@classmethod
	def check_hand(self, cards:list):
		self.cards = cards
		self.count_cards(self)
		if self.check_royal_flush(self):
			return f"You got a royal flush!"
		elif self.check_straight_flush(self):
			return f"You got a straight flush!"
		elif self.check_same_of_a_kind(self, 4):
			return f"You got four-of-a-kind!"
		elif self.check_same_of_a_kind(self, 3) and self.check_same_of_a_kind(self, 2):
			return f"You got a full house!"
		elif self.check_flush(self):
			return f"You got a flush!"
		elif self.check_straight(self):
			return f"You got a straight!"
		elif self.check_same_of_a_kind(self, 3):
			return f"You got three-of-a-kind!"
		elif self.check_pairs(self, 2):
			return f"You got 2 pairs!"
		elif self.check_pairs(self, 1):
			return f"You got a pair!"
		else:
			return f"You got {self.cards[4].rank} high!"

	def check_royal_flush(self):
		if self.check_flush(self) and self.check_straight(self) and self.cards[4].rank == 'A':
			return True
		return False

	def check_straight_flush(self):
		if self.check_flush(self) and self.check_straight(self):
			return True
		return False

	def check_straight(self):
		ranks_high = '23456789TJQKA'
		rank_indeces_high = [ranks_high.index(card.rank) for card in self.cards]
		ranks_low = 'A23456789TJQK'
		rank_indeces_low = [ranks_low.index(card.rank) for card in self.cards]

		if max(rank_indeces_high) - min(rank_indeces_high) == 4 and len(set(rank_indeces_high)) == 5:
			return True
		elif max(rank_indeces_low) - min(rank_indeces_low) == 4 and len(set(rank_indeces_low)) == 5:
			return True
		else:
			return False

	def check_pairs(self, amount:int):
		pairs = [rank for rank in self.ranks.values() if rank == 2]
		return len(pairs) == amount

	def check_flush(self):
		if 5 in self.suits.values():
			return True
		return False

	def check_same_of_a_kind(self, amount:int):
		if amount in self.ranks.values():
			return True
		return False


class Player:
	def __init__(self):
		self.hand = []

	def check_hand(self):
		self.sort_hand()
		print(self)
		print(Hand.check_hand(self.hand))

	def sort_hand(self):
		def rank_value(card):
			rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
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
		self.player.check_hand()
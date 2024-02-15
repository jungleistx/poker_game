from classes.deck import Deck
from classes.card import Card


class Hand():
	def __init__(self, deck:Deck):
		self._deck = deck
		self.reset_hand()

	def count_card_types(self):
		self.ranks = {rank: 0 for rank in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']}
		self.suits = {suit: 0 for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']}
		for card in self.cards:
			self.ranks[card.rank] += 1
			self.suits[card.suit] += 1

	def select_swaps(self) -> bool:
		self.swap_positions = []
		for card in self.cards:
			if card.swapping:
				self.swap_positions.append(self.cards.index(card))
		if self.swap_positions:
			self.swap_cards()
			return True
		return False

	def swap_cards(self):
		for pos in self.swap_positions:
			new_card = self.get_new_cards(1)[0]
			card_to_remove = self.cards[pos]
			self.cards.insert(pos, new_card)
			self.cards.remove(card_to_remove)
		self.sort_by_winning_hand()

	def reset_hand(self):
		self.cards = []
		self.cards.extend(self.get_new_cards(5))
		self.sort_by_winning_hand()

	def reset_card_positions(self):
		for card in self.cards:
			card.image.y = Card.card_height
			card.swapping = False
			card.image.set_current_rect()

	def get_new_cards(self, amount:int):
		new_cards = self._deck.deal_cards(amount)
		return new_cards

	def sort_hand_by_rank(self):
		def rank_value(card):
			rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
			return rank_order.get(card.rank, 0)
		self.cards.sort(key=lambda card: (rank_value(card), card.suit), reverse=True)

	def sort_by_winning_hand(self):
		self.sort_hand_by_rank()
		winning_hand, bet_multiplier = self.check_hand()

		if winning_hand == 'Four-of-a-kind':
			for card in self.cards:
				if self.ranks[card.rank] == 4:
					rank_to_sort = card.rank
					for card in self.cards[:]:
						if card.rank == rank_to_sort:
							self.cards.remove(card)
							self.cards.insert(0, card)
					break

		elif winning_hand == 'Full house':
			for card in self.cards:
				if self.ranks[card.rank] == 3:
					three_of_a_kind = card.rank
				elif self.ranks[card.rank] == 2:
					two_of_a_kind = card.rank
			for card in self.cards[:]:
				if card.rank == three_of_a_kind:
					self.cards.remove(card)
					self.cards.insert(0, card)
			for card in self.cards[:]:
				if card.rank == two_of_a_kind:
					self.cards.remove(card)
					self.cards.insert(3, card)

		elif winning_hand == 'Three-of-a-kind':
			for card in self.cards:
				if self.ranks[card.rank] == 3:
					three_of_a_kind = card.rank
					for card in self.cards[:]:
						if card.rank == three_of_a_kind:
							self.cards.remove(card)
							self.cards.insert(0, card)
					break

		elif winning_hand == 'Two pairs':
			pair_ranks = []
			for card in self.cards:
				if self.ranks[card.rank] == 2 and card.rank not in pair_ranks:
					pair_ranks.append(card.rank)
			for card in self.cards[:]:
				if card.rank == max(pair_ranks):
					self.cards.remove(card)
					self.cards.insert(0, card)
				elif card.rank == min(pair_ranks):
					self.cards.remove(card)
					self.cards.insert(2, card)

		elif winning_hand == 'Pair':
			for card in self.cards:
				if self.ranks[card.rank] == 2:
					rank_to_sort = card.rank
					for card in self.cards[:]:
						if card.rank == rank_to_sort:
							self.cards.remove(card)
							self.cards.insert(0, card)
					break

	def check_hand(self):
		self.count_card_types()
		if self.check_royal_flush():
			return f"Royal flush", 500
		elif self.check_straight_flush():
			return f"Straight flush", 100
		elif self.check_same_of_a_kind(4):
			return f"Four-of-a-kind", 50
		elif self.check_same_of_a_kind(3) and self.check_same_of_a_kind(2):
			return f"Full house", 15
		elif self.check_flush():
			return f"Flush", 10
		elif self.check_straight():
			return f"Straight", 6
		elif self.check_same_of_a_kind(3):
			return f"Three-of-a-kind", 4
		elif self.check_pairs(2):
			return f"Two pairs", 3
		elif self.check_pairs(1):
			return f"Pair", 1
		else:
			return f"{self.cards[0].rank} high", 0

	def check_royal_flush(self):
		if self.check_flush() and self.check_straight() and self.cards[0].rank == 'A':
			return True
		return False

	def check_straight_flush(self):
		if self.check_flush() and self.check_straight():
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

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n < len(self.cards):
			card = self.cards[self.n]
			self.n += 1
			return card
		else:
			raise StopIteration

	def __str__(self):
		return f"Hand:\n{', '.join(map(str, self.cards))}"

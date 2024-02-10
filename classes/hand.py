from classes.deck import Deck


class Hand():
	def __init__(self, deck:Deck):
		self.cards = deck.deal_cards(5)

	def count_card_types(self):
		self.ranks = {rank: 0 for rank in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']}
		self.suits = {suit: 0 for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']}

		for card in self.cards:
			self.ranks[card.rank] += 1
			self.suits[card.suit] += 1

	def check_hand(self):
		self.count_card_types()
		if self.check_royal_flush():
			return f"You got a royal flush!", 500
		elif self.check_straight_flush():
			return f"You got a straight flush!", 100
		elif self.check_same_of_a_kind(4):
			return f"You got four-of-a-kind!", 50
		elif self.check_same_of_a_kind(3) and self.check_same_of_a_kind(2):
			return f"You got a full house!", 15
		elif self.check_flush():
			return f"You got a flush!", 10
		elif self.check_straight():
			return f"You got a straight!", 6
		elif self.check_same_of_a_kind(3):
			return f"You got three-of-a-kind!", 4
		elif self.check_pairs(2):
			return f"You got 2 pairs!", 3
		elif self.check_pairs(1):
			return f"You got a pair!", 2
		else:
			return f"You got {self.cards[4].rank} high!", 0

	def check_royal_flush(self):
		if self.check_flush() and self.check_straight() and self.cards[4].rank == 'A':
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
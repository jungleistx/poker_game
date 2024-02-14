from classes.deck import Deck
from classes.hand import Hand


class Player:
	def __init__(self, deck:Deck):
		self.hand = Hand(deck)

	def check_hand(self):
		self.hand.check_hand()

	def reset_hand(self):
		self.hand.reset_hand()

	def check_swaps(self):
		return self.hand.check_swaps()

	def __str__(self):
		return f"{self.hand}"

	# def check_swaps(self, game:Game):
	# 	swap_amount = 0
	# 	swapping = True
	# 	while swapping:
	# 		swapping = False
	# 		for card in self.hand:
	# 			if card.swapping:
	# 				swap_amount += 1
	# 				self.hand.remove(card)
	# 				swapping = True
	# 	if swap_amount:
	# 		self.deal_new_cards(swap_amount, game.deck)
	# 		game.swap_used = True
	# 	self.sort_hand()

	# def swapping_cards(self, deck:Deck):
	# 	index = 1
	# 	for card in self.hand:
	# 		print(f"{index}{'.':<4}{card}")
	# 		index += 1

	# 	prompt = input("\nWould you like to swapping cards? (y/n): ")
	# 	if prompt == 'y':
	# 		positions = input("Enter the positions. If multiple, write them together (1 OR 235): ")
	# 		new_card_amount = len(positions)
	# 		positions = positions[::-1]
	# 		for char in positions:
	# 			del self.hand[int(char) - 1]

	# 		new_cards = deck.deal_cards(new_card_amount)
	# 		print('New cards:')
	# 		for card in new_cards:
	# 			print(card)

	# 		self.hand.extend(new_cards)
	# 		self.sort_hand()
	# 		return True
	# 	return False

from classes.deck import Deck
from classes.hand import Hand
from pygame_manager import pygame_instance


class Player:
	def __init__(self, deck:Deck):
		self.hand = Hand(deck)


	def check_hand(self):
		return self.hand.check_hand()


	def reset_hand(self):
		self.hand.reset_hand()


	def swap_cards(self):
		return self.hand.select_swaps()


	def reset_card_positions(self):
		self.hand.reset_card_positions()


	def sort_hand(self):
		self.hand.sort_by_winning_hand()


	def move_card_with_key(self, key:int):
		self.hand.move_card_with_key(key)


	def set_starting_coins(self):
		self.coins = 50


	def draw_coins(self, window):
		text_colour = (227, 192, 64)
		text = f"COINS: {str(self.coins)}"
		font = pygame_instance.freetype.SysFont('chalkboard', 26)
		font.render_to(window, (15, 20), text, text_colour)


	def __str__(self):
		return f"{self.hand}"

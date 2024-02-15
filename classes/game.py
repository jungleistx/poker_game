from classes.player import Player
from classes.deck import Deck


class Game:
	nr_of_players = 0

	def __init__(self):
		self.card_swap_used = False
		self.deck = Deck()
		self.player = self.add_player()

	def add_player(self) -> Player:
		Game.nr_of_players += 1
		return Player(self.deck)

	def reset_deck(self):
		self.deck.reset_deck()
		self.player.reset_hand()
		self.card_swap_used = False

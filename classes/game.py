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
		return Player()

	def start_game(self):
		self.deck.reset_deck()
		window = GameWindow()
		self.player.hand = self.deck.deal_cards(5)
		self.player.check_hand()
		window.run(self)

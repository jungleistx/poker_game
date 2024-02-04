from classes.player import Player
from classes.deck import Deck


class Game:
	def __init__(self, player:Player):
		self.player = player
		self.deck = Deck()
		self.swap_used = False

	def start_game(self):
		self.deck.reset_deck()
		window = GameWindow()
		self.player.hand = self.deck.deal_cards(5)
		self.player.check_hand()
		window.run(self)

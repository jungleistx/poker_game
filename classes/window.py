from classes.image import Image
from classes.button import Button
from classes.game import Game

# from classes.card import Card
import pygame


class Window:
	height = 680
	width = 1100

	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Poker Game')
		self.window = pygame.display.set_mode((Window.width, Window.height))
		self.__set_background()
		self.__set_buttons()

	def __set_background(self):
		self.background = Image('img/background/poker_table.jpg')
		self.background.image = pygame.transform.scale(self.background.image, (Window.width, Window.height))

	def __set_buttons(self):
		swap_button_location = (350, 535, 358, 556)
		submit_button_location = (580, 535, 604, 556)
		self.swap = Button('Swap cards', swap_button_location)
		self.submit = Button('Continue', submit_button_location)

	def check_mouseclick_cards(self, game:Game):
		mouse_pos = pygame.mouse.get_pos()
		for card in game.player.hand:
			if card.image.is_clicked(mouse_pos) and card.swapping == False:
				card.image.y -= 50
				card.swapping = True
			elif card.image.is_clicked(mouse_pos) and card.swapping == True:
				card.swapping = False
				card.image.y += 50

	def check_mouseclick_buttons(self, game:Game):
		mouse_pos = pygame.mouse.get_pos()
		self.swap.update_coordinates()
		if self.swap.image.is_clicked(mouse_pos):
			if not game.swap_used:
				game.player.check_swaps(game)
			else:
				print('Swap used!')
		elif self.submit.image.is_clicked(mouse_pos):
			game.player.check_hand()

	def draw_buttons(self):
		self.swap.draw_button(self.window)
		self.submit.draw_button(self.window)

	def draw_cards(self, game:Game):
		for card in game.player.hand:
			card.image.draw_image(self)

	def set_card_locations(self, game:Game):
		card_width = 140
		card_gap = 50
		x = 100
		for card in game.player.hand:
			card.image.x = x
			card.image.set_current_rect()
			x += card_gap + card_width

	def check_event_keys(self, event, game:Game):
		if event.key == pygame.K_s:
			if not game.swap_used:
				game.player.check_swaps(game)
			else:
				print('Swap used!')
		if event.key == pygame.K_c:
			game.player.check_hand()

	def check_events(self, game:Game):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print('Thank you come again!')
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.check_mouseclick_cards(game)
					self.check_mouseclick_buttons(game)
			if event.type == pygame.KEYDOWN:
				self.check_event_keys(event, game)

	def run(self, game:Game):
		# intro screen
		# new game

		while True:
			self.background.draw_image(self)
			self.set_card_locations(game)
			self.check_events(game)
			self.draw_cards(game)
			self.draw_buttons()

			pygame.display.flip()
			# pygame.time.delay(200)

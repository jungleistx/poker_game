from classes.image import Image
from classes.button import Button
from classes.game import Game
from pygame_manager import pygame_instance


class Window:
	HEIGHT = 680
	WIDTH = 1100

	def __init__(self):
		pygame_instance.display.set_caption('Poker Game')
		self.window = pygame_instance.display.set_mode((Window.WIDTH, Window.HEIGHT))
		self.__set_background()
		self.__set_buttons()
		self.game = Game()

	def __set_background(self):
		self.background = Image('img/background/poker_table.jpg')
		self.background.image = pygame_instance.transform.scale(self.background.image, (Window.WIDTH, Window.HEIGHT))

	def __set_buttons(self):
		swap_x, swap_y, swap_text_x, swap_text_y = 350, 535, 358, 556
		submit_x, submit_y, submit_text_x, submit_text_y = 580, 535, 604, 556

		self.swap = Button('Swap cards', swap_x, swap_y, swap_text_x, swap_text_y)
		self.submit = Button('Continue', submit_x, submit_y, submit_text_x, submit_text_y)
		self.swap.update_coordinates()
		self.submit.update_coordinates()

	def check_mouseclick_cards(self):
		mouse_pos = pygame_instance.mouse.get_pos()
		for card in self.game.player.hand:
			if card.image.is_clicked(mouse_pos) and card.swapping == False:
				card.image.y -= 50
				card.swapping = True
			elif card.image.is_clicked(mouse_pos) and card.swapping == True:
				card.swapping = False
				card.image.y += 50

	def check_mouseclick_buttons(self):
		mouse_pos = pygame_instance.mouse.get_pos()
		# self.swap.update_coordinates()
		# self.submit.update_coordinates()
		if self.swap.image.is_clicked(mouse_pos):
			if not self.game.swap_used:
				self.game.player.check_swaps(self.game)
			else:
				print('Swap used!')
		elif self.submit.image.is_clicked(mouse_pos):
			self.game.player.check_hand()

	def draw_buttons(self):
		self.swap.draw_button(self.window)
		self.submit.draw_button(self.window)

	def draw_cards(self):
		for card in self.game.player.hand:
			card.image.draw_image(self.window)

	def set_card_locations(self):
		card_width = 140
		card_gap = 50
		x = 100
		for card in self.game.player.hand:
			card.image.x = x
			card.image.set_current_rect()
			x += card_gap + card_width

	def check_event_keys(self, event):
		if event.key == pygame_instance.K_s:
			if not self.game.swap_used:
				self.game.player.check_swaps(self.game)
			else:
				print('Swap used!')
		if event.key == pygame_instance.K_c:
			self.game.player.check_hand()

	def check_events(self):
		for event in pygame_instance.event.get():
			if event.type == pygame_instance.QUIT:
				print('Thank you come again!')
				pygame_instance.quit()
				exit()
			if event.type == pygame_instance.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.check_mouseclick_cards()
					self.check_mouseclick_buttons()
			if event.type == pygame_instance.KEYDOWN:
				self.check_event_keys(event)

	def run(self):
		# intro screen
		# new game

		clock = pygame_instance.time.Clock()

		while True:
			self.background.draw_image(self.window)
			self.set_card_locations()
			self.check_events()
			self.draw_cards()
			self.draw_buttons()

			pygame_instance.display.flip()
			# pygame.time.delay(200)
			clock.tick(60)

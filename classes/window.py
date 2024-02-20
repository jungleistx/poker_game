from classes.image import Image
from classes.button import Button
from classes.game import Game
from pygame_manager import pygame_instance, game_font


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
		submit_x, submit_y, submit_text_x, submit_text_y = 578, 535, 604, 556
		quit_x, quit_y, quit_text_x, quit_text_y = 810, 535, 860, 556

		self.swap = Button('Swap cards', swap_x, swap_y, swap_text_x, swap_text_y)
		self.submit = Button('Continue', submit_x, submit_y, submit_text_x, submit_text_y)
		self.quit = Button('Quit', quit_x, quit_y, quit_text_x, quit_text_y)


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
		if self.swap.image.is_clicked(mouse_pos):
			self.check_swaps()
		elif self.submit.image.is_clicked(mouse_pos):
			self.continue_button()
		elif self.quit.image.is_clicked(mouse_pos):
			self.quit_and_exit()


	def check_swaps(self):
		if not self.game.card_swap_used:
			if self.game.player.swap_cards():
				self.game.card_swap_used = True
		else:
			self.game.player.reset_card_positions()


	def continue_button(self):
		self.check_swaps()
		self.draw_endgame_screen()


	def draw_continue_instructions(self):
		space_button = Button('Press SPACE to continue or Q to quit')
		space_button.change_button_size()
		space_button.set_new_location(Window.WIDTH, 210)
		space_button.draw_button(self.window)


	def spacekey_to_continue(self):
		while True:
			for event in pygame_instance.event.get():
				if event.type == pygame_instance.QUIT:
					self.quit_and_exit()
				elif event.type == pygame_instance.KEYDOWN:
					if event.key == pygame_instance.K_SPACE:
						return
					elif event.key == pygame_instance.K_q:
						self.quit_and_exit()


	def draw_endgame_screen(self):
		best_hand, win_multiplier = self.game.player.check_hand()
		# win_amount = self.game.player.bet * win_multiplier
		win_amount = win_multiplier
		if win_amount > 0:
			win_text = f"You win {win_amount}!"
		else:
			win_text = f"You lost your bet."

		result_button = Button(win_text)
		result_button.change_button_size()
		result_button.set_new_location(Window.WIDTH, 125)
		result_button.draw_button(self.window)

		self.draw_continue_instructions()
		self.draw_cards()
		self.draw_hand_info(best_hand)
		pygame_instance.display.flip()
		self.spacekey_to_continue()
		self.run()


	def draw_buttons(self):
		self.swap.draw_button(self.window)
		self.submit.draw_button(self.window)
		self.quit.draw_button(self.window)


	def draw_cards(self):
		self.set_card_locations()
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
			self.check_swaps()
		elif event.key == pygame_instance.K_c:
			self.continue_button()
		elif event.key == pygame_instance.K_SPACE:
			self.continue_button()
		elif event.key == pygame_instance.K_q:
			self.quit_and_exit()
		elif event.key == pygame_instance.K_1:
			self.game.player.move_card_with_key(1)
		elif event.key == pygame_instance.K_2:
			self.game.player.move_card_with_key(2)
		elif event.key == pygame_instance.K_3:
			self.game.player.move_card_with_key(3)
		elif event.key == pygame_instance.K_4:
			self.game.player.move_card_with_key(4)
		elif event.key == pygame_instance.K_5:
			self.game.player.move_card_with_key(5)


	def check_events(self):
		for event in pygame_instance.event.get():
			if event.type == pygame_instance.QUIT:
				self.quit_and_exit()
			if event.type == pygame_instance.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.check_mouseclick_cards()
					self.check_mouseclick_buttons()
			if event.type == pygame_instance.KEYDOWN:
				self.check_event_keys(event)


	def quit_and_exit(self):
		pygame_instance.quit()
		exit()


	def draw_hand_info(self, best_hand:str=None):
		text_colour = (227, 192, 64)
		if best_hand == None:
			hand, multiplier = self.game.player.check_hand()
		else:
			hand = best_hand
		font = pygame_instance.freetype.SysFont('chalkboard', 26)
		font.render_to(self.window, (40, 530), hand, text_colour)


	def draw_intro_texts(self):
		text_colour = (227, 192, 64)
		text_lines_1 = ['', 'TRY TO GET THE BEST HAND POSSIBLE.', 'YOU HAVE ONE SWAP, YOU CAN SWAP ANY CARD.',  '']
		text_lines_2 = ['PRESS KEYS 1-5 TO SELECT CARDS FOR SWAPPING.', 'PRESS SPACE KEY TO CONFIRM SWAPS, OR TO END GAME.', 'IF YOU PREFER, YOU CAN USE MOUSE.', '', 'GOOD LUCK, HAVE FUN!', '']
		header_text = 'WELCOME TO VIDEO POKER!'
		bold_text = ['INSTRUCTIONS:', 'PRESS SPACE TO START!']

		header_font = pygame_instance.font.SysFont('chalkboard', 48, bold=True)
		text = header_font.render(header_text, True, text_colour)
		header_width = text.get_width()
		header_font = pygame_instance.freetype.SysFont('chalkboard', 48, bold=True)
		x = Window.WIDTH // 2 - header_width // 2 - 15
		header_font.render_to(self.window, (x, 80), header_text, text_colour)

		mid_font = pygame_instance.freetype.SysFont('chalkboard', 28)
		y = 120
		for line in text_lines_1:
			text = game_font.render(line, True, text_colour)
			text_width = text.get_width()
			text_height = text.get_height()
			x = Window.WIDTH // 2 - text_width // 2
			mid_font.render_to(self.window, (x, y), line, text_colour)
			y += text_height + 5

		bold_font = pygame_instance.font.SysFont('chalkboard', 38, bold=True)
		text = bold_font.render(bold_text[0], True, text_colour)
		bold_width_0 = text.get_width()
		text = bold_font.render(bold_text[1], True, text_colour)
		bold_width_1 = text.get_width()
		bold_font = pygame_instance.freetype.SysFont('chalkboard', 38, bold=True)
		x = Window.WIDTH // 2 - bold_width_0 // 2

		bold_font.render_to(self.window, (x, y), bold_text[0], text_colour)

		y += 50
		for line in text_lines_2:
			text = game_font.render(line, True, text_colour)
			text_width = text.get_width()
			text_height = text.get_height()
			x = Window.WIDTH // 2 - text_width // 2
			mid_font.render_to(self.window, (x, y), line, text_colour)
			y += text_height + 5

		x = Window.WIDTH // 2 - bold_width_1 // 2
		bold_font.render_to(self.window, (x, y), bold_text[1], text_colour)


	def intro_window(self):
		intro_screen_colour = (102, 128, 103)
		self.window.fill(intro_screen_colour)

		self.draw_intro_texts()
		pygame_instance.display.flip()
		self.spacekey_to_continue()
		self.game.player.set_starting_coins()


	def new_game(self):
		self.intro_window()
		self.run()


	def run(self):
		self.game.reset_deck()
		clock = pygame_instance.time.Clock()

		while True:
			self.background.draw_image(self.window)
			self.set_card_locations()
			self.check_events()
			self.draw_cards()
			self.draw_buttons()
			self.draw_hand_info()

			pygame_instance.display.flip()
			clock.tick(60)

from classes.image import Image
from pygame_manager import pygame_instance, game_font


class Button:
	HEIGHT = 80
	WIDTH = 160
	TEXT_COLOUR = (2, 36, 8)


	def __init__(self, text:str, x:int=0, y:int=0, b_x:int=0, b_y:int=0):
		self.text = text
		self.image = Image('img/button/button.png', x, y)
		self.image.image = pygame_instance.transform.scale(self.image.image, (Button.WIDTH, Button.HEIGHT))
		self.text_x = b_x
		self.text_y = b_y
		self.update_coordinates()

	def update_coordinates(self):
		self.image.set_current_rect()


	def draw_button(self, window):
		self.update_coordinates()
		window.blit(self.image.image, (self.image.x, self.image.y))
		self.draw_text(window)


	def draw_text(self, window):
		text = game_font.render(self.text, True, (Button.TEXT_COLOUR))
		window.blit(text, (self.text_x,self.text_y))


	def change_button_size(self):
		text_box = game_font.render(self.text, True, (Button.TEXT_COLOUR))
		self.text_box_width = text_box.get_width()
		self.text_box_height = text_box.get_height()
		self.image.image = pygame_instance.transform.scale(self.image.image, (self.text_box_width + 60, self.text_box_height + 30))


	def set_new_location(self, window_width:int, y:int=0):
		self.image.x = window_width // 2 - self.text_box_width // 2 - 30
		self.text_x = self.image.x + 30
		self.image.y = y
		self.text_y = self.image.y + 15

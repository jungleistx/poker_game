from classes.image import Image
from pygame_manager import pygame_instance, game_font


class Button:
	HEIGHT = 80
	WIDTH = 160

	def __init__(self, text:str, x:int=0, y:int=0, b_x:int=0, b_y:int=0):
		self.text = text
		self.image = Image('img/button/button.png', x, y)
		self.image.image = pygame_instance.transform.scale(self.image.image, (Button.WIDTH, Button.HEIGHT))
		self.text_x = b_x
		self.text_y = b_y

	def update_coordinates(self):
		self.image.set_current_rect()

	def draw_button(self, window):
		self.update_coordinates()
		window.blit(self.image.image, (self.image.x, self.image.y))
		self.draw_text(window)

	def draw_text(self, window):
		text = game_font.render(self.text, True, (2, 36, 8))
		window.blit(text, (self.text_x,self.text_y))

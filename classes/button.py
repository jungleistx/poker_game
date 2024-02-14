from classes.image import Image
from main import pygame_instance


class Button:
	HEIGHT = 80
	WIDTH = 160

	def __init__(self, text:str, x:int=0, y:int=0, b_x:int=0, b_y:int=0):
		self.text = text
		self.image = Image('img/button/button.png', x, y)
		self.image.image = pygame_instance.transform.scale(self.image.image, (Button.WIDTH, Button.HEIGHT))
		self.game_font = pygame_instance.font.SysFont('chalkboard', 28)
		self.text_x = b_x
		self.text_y = b_y

	def update_coordinates(self):
		self.image.set_current_rect()

	def draw_button(self, window):
		self.update_coordinates()
		window.blit(self.image.image, (self.image.x, self.image.y))
		self.draw_text(window)

	def draw_text(self, window):
		text = self.game_font.render(self.text, True, (255, 0, 0))
		window.blit(text, (self.text_x,self.text_y))

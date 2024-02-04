import pygame


class Image():
	def __init__(self, path:str, pygame, x:int=0, y:int=0):
		self.image = pygame.image.load(path)
		self.x = x
		self.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def is_clicked(self, mouse_pos) -> bool:
		return self.rect.collidepoint(mouse_pos)

	def print_coordinates(self):
		print(f'({self.x},{self.y})', end=' - ')
		print(f'({self.x + self.width},{self.y})')
		print(f'({self.x},{self.y + self.height})', end=' - ')
		print(f'({self.x + self.width},{self.y + self.height})')

	def set_current_rect(self):
		self.rect = self.image.get_rect(topleft=(self.x, self.y))

	def draw_image(self, window):
		window.blit(self.image, (self.x, self.y))

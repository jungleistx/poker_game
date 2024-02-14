from pygame_manager import pygame_instance


class Image():
	def __init__(self, path:str, x:int=0, y:int=0):
		self.image = pygame_instance.image.load(path)
		self.__image_path = path
		self.x = x
		self.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def is_clicked(self, mouse_pos) -> bool:
		return self.rect.collidepoint(mouse_pos)

	def set_current_rect(self):
		self.rect = self.image.get_rect(topleft=(self.x, self.y))

	def draw_image(self, window):
		window.blit(self.image, (self.x, self.y))

	def __str__(self) -> str:
		return f"\'{self.__image_path}\':\n({self.x},{self.y}) - ({self.x + self.width},{self.y + self.height})"

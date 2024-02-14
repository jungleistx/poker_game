from classes.image import Image


class Button:
	BUTTON_HEIGHT = 80
	BUTTON_WIDTH = 160

	def __init__(self, text:str, pygame, x:int=0, y:int=0, b_x:int=0, b_y:int=0):
		self.text = text
		self.image = Image('img/button/button.png', pygame, x, y)
		self.image.image = pygame.transform.scale(self.image.image, (Button.BUTTON_WIDTH, Button.BUTTON_HEIGHT))
		self.game_font = pygame.font.SysFont('chalkboard', 28)
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

import random
import pygame

CARD_HEIGHT = 300

class GameWindow:
	pass

class Image():
	def __init__(self, path:str, x:int=0, y:int=0):
		self.image = pygame.image.load(path)
		self.x = x
		self.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def is_clicked(self, mouse_pos):
		return self.rect.collidepoint(mouse_pos)

	def print_coordinates(self):
		print(f'({self.x},{self.y})', end='-')
		print(f'({self.x + self.width},{self.y})')
		print(f'({self.x},{self.y + self.height})', end='-')
		print(f'({self.x + self.width},{self.y + self.height})')
		print()

	def set_current_rect(self):
		self.rect = self.image.get_rect(topleft=(self.x, self.y))

	def draw_image(self, gamewindow:GameWindow):
		gamewindow.window.blit(self.image, (self.x, self.y))


class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.swapping = False
		self.image = Image(f"img/cards/card{self.suit}{self.rank}.png", 0, CARD_HEIGHT)

	def __str__(self):
		return f"{self.rank} of {self.suit}"


class Deck:
	def __init__(self):
		self.reset_deck()

	def reset_deck(self):
		suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
		self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
		self.shuffle()

	def shuffle(self):
		random.shuffle(self.cards)

	def deal_cards(self, amount:int):
		dealt_cards = self.cards[:amount]
		self.cards = self.cards[amount:]
		return dealt_cards


class Hand(Card):
	def __init__(self, cards:list):
		super().__init__('', '')

	def count_cards(self):
		self.ranks = {rank: 0 for rank in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']}
		self.suits = {suit: 0 for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']}

		for card in self.cards:
			self.ranks[card.rank] += 1
			self.suits[card.suit] += 1

	@classmethod
	def check_hand(self, cards:list):
		self.cards = cards
		self.count_cards(self)
		if self.check_royal_flush(self):
			return f"You got a royal flush!"
		elif self.check_straight_flush(self):
			return f"You got a straight flush!"
		elif self.check_same_of_a_kind(self, 4):
			return f"You got four-of-a-kind!"
		elif self.check_same_of_a_kind(self, 3) and self.check_same_of_a_kind(self, 2):
			return f"You got a full house!"
		elif self.check_flush(self):
			return f"You got a flush!"
		elif self.check_straight(self):
			return f"You got a straight!"
		elif self.check_same_of_a_kind(self, 3):
			return f"You got three-of-a-kind!"
		elif self.check_pairs(self, 2):
			return f"You got 2 pairs!"
		elif self.check_pairs(self, 1):
			return f"You got a pair!"
		else:
			return f"You got {self.cards[4].rank} high!"

	def check_royal_flush(self):
		if self.check_flush(self) and self.check_straight(self) and self.cards[4].rank == 'A':
			return True
		return False

	def check_straight_flush(self):
		if self.check_flush(self) and self.check_straight(self):
			return True
		return False

	def check_straight(self):
		ranks_high = '23456789TJQKA'
		rank_indeces_high = [ranks_high.index(card.rank) for card in self.cards]
		ranks_low = 'A23456789TJQK'
		rank_indeces_low = [ranks_low.index(card.rank) for card in self.cards]

		if max(rank_indeces_high) - min(rank_indeces_high) == 4 and len(set(rank_indeces_high)) == 5:
			return True
		elif max(rank_indeces_low) - min(rank_indeces_low) == 4 and len(set(rank_indeces_low)) == 5:
			return True
		else:
			return False

	def check_pairs(self, amount:int):
		pairs = [rank for rank in self.ranks.values() if rank == 2]
		return len(pairs) == amount

	def check_flush(self):
		if 5 in self.suits.values():
			return True
		return False

	def check_same_of_a_kind(self, amount:int):
		if amount in self.ranks.values():
			return True
		return False


class Player:
	def __init__(self):
		self.hand = []

	def check_hand(self):
		self.sort_hand()
		print(self)
		print(Hand.check_hand(self.hand))
		print()

	def sort_hand(self):
		def rank_value(card):
			rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
			return rank_order.get(card.rank, 0)
		self.hand.sort(key=lambda card: (rank_value(card), card.suit))

	def swapping_cards(self, deck:Deck):
		index = 1
		for card in self.hand:
			print(f"{index}{'.':<4}{card}")
			index += 1

		prompt = input("\nWould you like to swapping cards? (y/n): ")
		if prompt == 'y':
			positions = input("Enter the positions. If multiple, write them together (1 OR 235): ")
			new_card_amount = len(positions)
			positions = positions[::-1]
			for char in positions:
				del self.hand[int(char) - 1]

			new_cards = deck.deal_cards(new_card_amount)
			print('New cards:')
			for card in new_cards:
				print(card)

			self.hand.extend(new_cards)
			self.sort_hand()
			return True
		return False

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n < len(self.hand):
			card = self.hand(self.n)
			self.n += 1
			return card
		else:
			raise StopIteration

	def __str__(self):
		return f"Hand:\n{', '.join(map(str, self.hand))}"


class Game:
	def __init__(self, player:Player):
		self.player = player
		self.deck = Deck()

	def start_game(self):
		self.deck.reset_deck()
		window = GameWindow()
		self.player.hand = self.deck.deal_cards(5)
		self.player.check_hand()
		window.run(self)
		if self.player.swapping_cards(self.deck):
			self.player.check_hand()


class Button:
	BUTTON_HEIGHT = 130
	BUTTON_WIDTH = 260

	def __init__(self, text:str, x=0, y=0):
		self.text = text
		self.x = x
		self.y = y
		self.coordinates = (self.x, self.y)
		self.image = Image('img/button/button.png', 0, 0)
		self.image.image = pygame.transform.scale(self.image.image, (Button.BUTTON_WIDTH, Button.BUTTON_HEIGHT))

	def update_coordinates(self):
		self.coordinates = (self.x, self.y)
		self.image.set_current_rect()



class GameWindow:
	BLACK_BACKGROUND = (0, 0, 0)
	TOPLEFT = (0, 0)

	def __init__(self):
		height = 680
		width = 1100
		pygame.init()
		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption('Poker Game')
		self.background = Image('img/background/poker_table.jpg', 0)
		self.background.image = pygame.transform.scale(self.background.image, (1100, 680))

	def check_mouseclick_cards(self, game:Game):
		mouse_pos = pygame.mouse.get_pos()
		for card in game.player.hand:
			if card.image.is_clicked(mouse_pos) and card.swapping == False:
				card.image.y -= 50
				card.swapping = True
			elif card.image.is_clicked(mouse_pos) and card.swapping == True:
				card.swapping = False
				card.image.y += 50

	def run(self, game:Game):
		while True:

			card_width = 140
			card_gap = 50
			x = 100
			for card in game.player.hand:
				card.image.set_coordinates(x)
				x += card_gap + card_width

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						self.check_mouseclick_cards(game)

			self.window.blit(self.background.image, (GameWindow.TOPLEFT))

			for card in game.player.hand:
				self.window.blit(card.image.image, (card.image.x, card.image.y))

			pygame.display.flip()
			pygame.time.delay(200)

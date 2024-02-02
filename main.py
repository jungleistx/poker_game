from classes import *

player = Player()
game = Game(player)

while True:
	game.start_game()

	new_game = input("New hand? (y/n): ")
	if new_game != 'y':
		break


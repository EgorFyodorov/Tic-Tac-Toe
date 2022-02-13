def cross(i, q):
	color = (255, 0, 0)
	pygame.draw.line(GlobalScreen, color, [q * 200 + 10, i * 200 + 10], [q * 200 + 190, i * 200 + 190], 10)
	pygame.draw.line(GlobalScreen, color, [q * 200 + 10, i * 200 + 190], [q * 200 + 190, i * 200 + 10], 10)
def zero(i, q):
	pygame.draw.circle(GlobalScreen, (0, 102, 204), (q * 200 + 100, i * 200 + 100), 73)
	pygame.draw.circle(GlobalScreen, (255, 255, 255), (q * 200 + 100, i * 200 + 100), 62)

def field_painting(field):
	for i in range(3):
		for q in range(3):
			if field[i][q] == 1:
				cross(i, q)
			elif field[i][q] == -1:
				zero(i, q)

def lines_painting():
	pygame.draw.line(GlobalScreen, (0, 0, 0), [200, 0], [200, 600])
	pygame.draw.line(GlobalScreen, (0, 0, 0), [400, 0], [400, 600])
	pygame.draw.line(GlobalScreen, (0, 0, 0), [600, 0], [600, 600])
	pygame.draw.line(GlobalScreen, (0, 0, 0), [0, 200], [600, 200])
	pygame.draw.line(GlobalScreen, (0, 0, 0), [0, 400], [600, 400])

import pygame
from mainpyg import *

pygame.init()
W = 800
H = 600
GlobalScreen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

clock = pygame.time.Clock()
FPS = 60

Title = 'Tic Tac Toe'
pygame.display.set_caption(Title)
pygame.display.update()

q = 0
while True:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			pygame.quit()
	q += 1
	if q == 5000:
		FPS = 1
	GlobalScreen.fill((255, 255, 255))
	clock.tick(FPS)

	field, move_number, game_number, error = main_part()
	field_painting(field)
	lines_painting()

	f = pygame.font.Font(None, 25)
	d = pygame.font.Font(None, 20)
	text1 = f.render('Move number: ' + str(move_number), 1, (0, 0, 0))
	text2 = f.render('Game number: ' + str(game_number), 1, (0, 0, 0))
	text3 = f.render('Output error: ', 1, (0, 0, 0))
	text4 = d.render(str(error), 1, (0, 0, 0))	
	GlobalScreen.blit(text1, [602, 15])
	GlobalScreen.blit(text2, [602, 40])
	GlobalScreen.blit(text3, [602, 65])
	GlobalScreen.blit(text4, [602, 80])


	pygame.display.update()

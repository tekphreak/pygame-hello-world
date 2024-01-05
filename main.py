import sys
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption('HELLO WORLD')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = pygame.Rect((300,250,50,50))

run= True
while run:
	
	screen.fill((0, 0, 0))

	pygame.draw.rect(screen, (255, 0, 0), player)	
	
	key = pygame.key.get_pressed()
	if key[pygame.K_a] == True:	
		player.move_ip(-1, 0)	
	if key[pygame.K_d] == True:	
		player.move_ip(1, 0)	
	if key[pygame.K_w] == True:	
		player.move_ip(0, -1)
	if key[pygame.K_s] == True:
		player.move_ip(0, 1)
	if key[pygame.K_SPACE] == True:
		player.move_ip(0, 2)
	if key[pygame.K_UP] == True:
		player.move_ip(0, -1)
	if key[pygame.K_DOWN] == True:
		player.move_ip(0, 1)
	if key[pygame.K_LEFT] == True:
		player.move_ip(-1, 0)
	if key[pygame.K_RIGHT] == True:
		player.move_ip(1, 0)





	if key[pygame.K_END] == True:
		pygame.quit()
			
		


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			sys.exit()

	pygame.display.update()

pygame.quit()			
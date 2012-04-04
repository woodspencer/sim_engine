import sys, os, pygame
pygame.init()


size = width, height = 900,600
speed = [2,2]

#colours
black = 0,0,0

screen = pygame.display.set_mode(size)

char = pygame.image.load("data/gfx/character/char_marie_00.png")
char_rect = char.get_rect()
char_rect.move_ip(100,120)

char1 = pygame.image.load("data/gfx/character/char_marie_00.png")
char_rect1 = char1.get_rect()
char_rect1.move_ip(200,120)

char2 = pygame.image.load("data/gfx/character/char_marie_00.png")
char_rect2 = char2.get_rect()
char_rect2.move_ip(400,120)


bg = pygame.image.load("data/gfx/background/bg_00.png")
bg_rect = bg.get_rect()
bg_rect.fit(char_rect)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	
		
	screen.blit(bg, bg_rect)
	screen.blit(char, char_rect)
	screen.blit(char1, char_rect1)
	screen.blit(char2, char_rect2)
	pygame.display.flip()

import pygame

if __name__=="__main__":
#start pygame
	pygame.init()
	main_screen = pygame.display.set_mode((500,500))
	main_screen.fill((255,255,255))
#background colour
	button_rec =pygame.Rect(100, 100, 20, 20)
	button_sq = pygame.Surface([20,20])
	main_screen.blit(button_sq, button_rec)
#FREAK OUT HERE!!!!!

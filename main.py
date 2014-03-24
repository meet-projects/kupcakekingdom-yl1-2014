import pygame
import Box

if __name__=="__main__":
#start pygame
	pygame.init()
	main_screen = pygame.display.set_mode((450,600))
	main_screen.fill((255,255,255))
#background colour
	button_rec =pygame.Rect(100, 100, 20, 20)
	button_sq = pygame.Surface([20,20])
	main_screen.blit(button_sq, button_rec)
#button
	while True: 
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			x, y = ev.pos
			if button_rec.collidepoint(x,y): 
				q = Box.Box(300, 300, 100, 100, 0, 0, 0)
				button_rec =pygame.Rect(150, 150, 20, 20)
				button_sq = pygame.Surface([20,20])
				main_screen.blit(button_sq, button_rec)	
				main_screen.blit(q.sq, button_rec)
		pygame.display.flip()



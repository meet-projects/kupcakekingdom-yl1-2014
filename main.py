import pygame
import Box

def erase(color):
	main_screen.fill(color)

if __name__=="__main__":
#start pygame
	pygame.init()
	main_screen = pygame.display.set_mode((450,600))
	main_screen.fill((255,255,224))

	start = Box.Box(135, 500, 180, 50, 64, 224, 208)
	Box.Box.draw(start, main_screen)

	while True: 
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			x, y = ev.pos
			if start.rec.collidepoint(x,y):
				erase((255, 255, 224))
				
				one = Box.Box(37.5, 150, 100, 100, 64, 224, 208)
				Box.Box.draw(one, main_screen)
				one.drawimg("Frostings/Gluten-free-chocolate-Nutella-cupcakes-close-up-21.jpg", main_screen)

				two = Box.Box(170, 150, 100, 100, 64, 224, 208)				
				Box.Box.draw(two, main_screen)
				two.drawimg("Frostings/5_single_cupcake_crop.jpg", main_screen)

				Box.Box.draw(two, main_screen)
				three = Box.Box(302.5, 150, 100, 100, 64, 224, 208)
				Box.Box.draw(three, main_screen)
				four = Box.Box(37.5, 337.5, 100, 100, 64, 224, 208)
				Box.Box.draw(four, main_screen)
				five = Box.Box(170, 337.5, 100, 100, 64, 224, 208)
				Box.Box.draw(five, main_screen)
				six = Box.Box(302.5, 337.5, 100, 100, 64, 224, 208)
				Box.Box.draw(six, main_screen)
			if one.rec.collidepoint(x,y):
				print "hi"
		
		pygame.display.flip()



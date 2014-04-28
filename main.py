import pygame
import Box

def erase(color):
	main_screen.fill(color)

def fro():

	one = Box.Box(37.5, 150, 100, 100, 64, 224, 208)
	Box.Box.draw(one, main_screen)
	one.drawimg("Frostings/frosting1.jpg", main_screen)

	two = Box.Box(170, 150, 100, 100, 64, 224, 208)				
	Box.Box.draw(two, main_screen)
	two.drawimg("Frostings/frosting2.jpg", main_screen)

	three = Box.Box(302.5, 150, 100, 100, 64, 224, 208)
	Box.Box.draw(three, main_screen)
	three.drawimg("Frostings/frosting3.jpg", main_screen)

	four = Box.Box(37.5, 337.5, 100, 100, 64, 224, 208)
	Box.Box.draw(four, main_screen)
	four.drawimg("Frostings/frosting4.jpg", main_screen)
				
	five = Box.Box(170, 337.5, 100, 100, 64, 224, 208)
	Box.Box.draw(five, main_screen)
	five.drawimg("Frostings/cs.jpg", main_screen)

	six = Box.Box(302.5, 337.5, 100, 100, 64, 224, 208)
	Box.Box.draw(six, main_screen)
	six.drawimg("Frostings/cs.jpg", main_screen)

	global pg
	pg=1

def top():
	one = Box.Box(37.5, 150, 100, 100, 64, 224, 208)
	Box.Box.draw(one, main_screen)
	one.drawimg("Toppings/t1.jpg", main_screen)

	two = Box.Box(170, 150, 100, 100, 64, 224, 208)				
	Box.Box.draw(two, main_screen)
	two.drawimg("Toppings/t2.jpg", main_screen)

	three = Box.Box(302.5, 150, 100, 100, 64, 224, 208)
	Box.Box.draw(three, main_screen)
	three.drawimg("Toppings/t3.jpg", main_screen)

	four = Box.Box(37.5, 337.5, 100, 100, 64, 224, 208)
	Box.Box.draw(four, main_screen)
	four.drawimg("Toppings/t4.jpg", main_screen)
	
	five = Box.Box(170, 337.5, 100, 100, 64, 224, 208)
	Box.Box.draw(five, main_screen)
	five.drawimg("Toppings/cs.jpg", main_screen)
	
	six = Box.Box(302.5, 337.5, 100, 100, 64, 224, 208)
	Box.Box.draw(six, main_screen)
	six.drawimg("Toppings/cs.jpg", main_screen)

	global pg
	pg=2

def end():
	erase((64, 224, 208))


if __name__=="__main__":
#start pygame
	pygame.init()
	main_screen = pygame.display.set_mode((450,600))
	main_screen.fill((255,255,224))

	start = Box.Box(135, 500, 180, 50, 64, 224, 208)
	Box.Box.draw(start, main_screen)

	pg=0

	while True: 
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			x, y = ev.pos
			if start.rec.collidepoint(x,y):
				erase((255, 255, 224))
				
				one = Box.Box(37.5, 150, 100, 100, 64, 224, 208)
				Box.Box.draw(one, main_screen)
				one.drawimg("Actual/a1.jpg", main_screen)

				two = Box.Box(170, 150, 100, 100, 64, 224, 208)				
				Box.Box.draw(two, main_screen)
				two.drawimg("Actual/a2.jpg", main_screen)

				three = Box.Box(302.5, 150, 100, 100, 64, 224, 208)
				Box.Box.draw(three, main_screen)
				three.drawimg("Actual/a3.jpg", main_screen)

				four = Box.Box(37.5, 337.5, 100, 100, 64, 224, 208)
				Box.Box.draw(four, main_screen)
				four.drawimg("Actual/a4.jpg", main_screen)
				
				five = Box.Box(170, 337.5, 100, 100, 64, 224, 208)
				Box.Box.draw(five, main_screen)
				five.drawimg("Actual/cs.jpg", main_screen)
				
				six = Box.Box(302.5, 337.5, 100, 100, 64, 224, 208)
				Box.Box.draw(six, main_screen)
				six.drawimg("Actual/cs.jpg", main_screen)


			if one.rec.collidepoint(x,y):
				if pg==0:
					fro()
				elif pg==1:
					top()
				elif pg==2:
					end()
			if two.rec.collidepoint(x,y):
				if pg==0:
					fro()
				elif pg==1:
					top()
				elif pg==2:
					end()
			if three.rec.collidepoint(x,y):
				if pg==0:
					fro()
				elif pg==1:
					top()
				elif pg==2:
					end()
			if four.rec.collidepoint(x,y):
				if pg==0:
					fro()
				elif pg==1:
					top()
				elif pg==2:
					end()
		
		pygame.display.flip()



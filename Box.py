import pygame

class Box(object):
	def __init__(self, lo_x, lo_y, si_x, si_y, r, g, b):
		self.rec = pygame.Rect(lo_x, lo_y, si_x, si_y)
		self.sq = pygame.Surface([si_x, si_y])
		self.sq.fill((r, g, b))
	
	def drew_out(self):
		main_screen.blit(self.sq, self.rec)
	


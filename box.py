class box(object):
	def __init__(self, lo_x, lo_y, si_x, si_y, r, g, b):
		self.rec = pygame.Rect(lo_x, lo_y, si_x, si_y)
		self.sq = pygame.Surface([si_x, si_y])
		self.sq.fill((r, g, b))
	def drew_out(self):
		main_screen.blit(self.sq, self.rec)
	
#	pygame.init()
#	main_screen = pygame.display.set_mode((600, 600))
#	main_screen.fill((255, 252, 195))
#	x = box(150, 150, 100, 100, 0, 0, 0)
#	x.drew_out()
	


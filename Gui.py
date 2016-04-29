from tkinter import *
import time
import World

class gui:
	def __init__(self, window, size, world):
		self.grid = world
		self.c = Canvas(window, width=size, height=size)
		self.c.pack()
		self.drawGrid(size, size)
		for i in range(len(world)):
			for j in range(len(world[i])):
				if world[i][j] == -1:
					self.placePit(size/22,  i, j)
				elif world[i][j] == 1:
					self.placeGold(size/22, i, j)
		self.c.update()
		window.mainloop()
	
	def placeGold(self, size, y, x):
		newx = size * x + 2
		newy = size * y + 2
		self.c.create_rectangle(newx, newy, newx+size - 4, newy+size - 4, fill="gold")
	
	def placePlayer(self, size, y, x):
		newx = size * x + 2
		newy = size * y + 2
		self.player = self.c.create_oval(newx, newy, newx+size - 4, newy+size - 4, fill="blue", tag='player')
	
	def placePit(self, size, y, x):
		newx = size * x + 2
		newy = size * y + 2
		self.c.create_rectangle(newx, newy, newx+size - 4, newy+size -4, fill="black")

	def drawGrid(self, w, h):
		# border
		self.c.create_line(0, 0, 0, h, width=5) # left
		self.c.create_line(0, h, w, h, width=5) # bottom
		self.c.create_line(0, 0, w, 0, width=5) # top
		self.c.create_line(w, 0, w, h, width=5) # right
		# columns
		p = 0
		for i in range(22):
			p += w / 22
			self.c.create_line(p, 0, p, h, width=5)
		# rows
		p = 0
		for i in range(22):
			p += h / 22
			self.c.create_line(0, p, w, p, width=5)

if __name__ == "__main__":
	w = Tk()
	world = World.loadWorld('world.txt')
	app = gui(w, 700, world)
	#w.mainloop()

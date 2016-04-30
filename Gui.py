from tkinter import *
import time
import World

class gui:
	def __init__(self, size, world):
		self.window = Tk()
		self.size = size
		self.grid = world
		self.c = Canvas(self.window, width=size, height=size)
		self.c.pack()
		self.drawGrid(size, size)
		for i in range(len(world)):
			for j in range(len(world[i])):
				if world[i][j] == -1:
					self.placePit(size/22,  i, j)
				elif world[i][j] == 1:
					self.placeGold(size/22, i, j)
		self.c.update()
		#self.window.mainloop()
	
	def placeGold(self, size, x, y):
		newx = size * x + 2
		newy = size * y + 2
		self.c.create_rectangle(newx, newy, newx+size - 4, newy+size - 4, fill="gold")
	
	def placeAgent(self, x, y):
		self.c.delete('agent')
		newx = (self.size / 22) * x + 2
		newy = (self.size / 22) * y + 2
		self.agentPos = (x, y)
		self.player = self.c.create_oval(newx, newy, newx+self.size/22 - 4, newy+self.size/22 - 4, fill="blue", tag='agent')
		self.c.update()
	
	def placePit(self, size, x, y):
		newx = size * x + 2
		newy = size * y + 2
		self.c.create_rectangle(newx, newy, newx+size - 4, newy+size -4, fill="black")
	
	def moveAgent(self, pos):
		x = pos[0] * (self.size / 22)
		y = pos[1] * (self.size /22)
		self.c.move('agent', x, y)
		self.c.update()
	
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
	world = World.loadWorld('world.txt')
	app = gui(700, world)
	app.placeAgent(5,5)
	#app.window.mainloop()
	#thread.thread.start_new_thread(app.window.mainloop())
	app.moveAgent((1,0))
	while True:
		app.moveAgent((0, 1))
		time.sleep(1)
	app.window.mainloop()

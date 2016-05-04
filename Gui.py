from tkinter import *
from tkinter import filedialog
import math
import time
import World
import numpy as np
import pickle

class Start:
	def __init__(self):
		self.w = w = Tk()
		self.fn = ""
		Button(w, text="Open Save", command=self.__getFile).pack()
		Button(w, text="Create New", command=self.__createNew).pack()
		w.mainloop()
	
	def __createNew(self):
		self.w.destroy()
		inp = InputDialog()
		self.params = inp.params
		self.fn = inp.fn
		"""
		params = ParameterInput()
		self.fn = params.fn
		"""
	
	def __getFile(self):
		self.fn = filedialog.askopenfilename(filetypes=[('save files', '.save'), ('all files', '.*')])
		if self.fn != "":
			self.params = pickle.load(open(self.fn, "rb"))
			self.w.destroy()

class InputDialog:
	def __init__(self):
		self.w = w = Tk()
		self.fn = ""
		Label(w, text="Alpha ").grid(row=0, column=0)
		Label(w, text="Gamma ").grid(row=1, column=0)
		Label(w, text="Lambda ").grid(row=2, column=0)
		Label(w, text="Epsilon Decay ").grid(row=3, column=0)
		self.inputs = [Entry(w) for x in range(4)]
		for i in range(len(self.inputs)):
			self.inputs[i].grid(row=i, column=1)
		Button(w, text="OK", command=self.ok).grid(row=4)
		w.mainloop()
	
	def ok(self):
		try:
			params = [float(entry.get()) for entry in self.inputs]
		except ValueError:
			Label(self.w, text="Invalid input", fg="red").grid(row=5, column=0)
			return
		if self.fn == "":
			self.fn = filedialog.asksaveasfilename(filetypes=[('save files', '.save'), ('all files', '.*')])
		if self.fn != "":
			# Initialize a new q table with random small values
			q_table = []
			for i in range(22):
				q_table.append([])
				for j in range(22):
					q_table[i].append([])
					for k in range(4):
						q_table[i][j].append(np.random.rand() * .1)
			params.append(.9)
			params.append(q_table)
			self.params = params
			self.w.destroy()
				
class gui:
	def __init__(self, size, world):
		self.window = Tk()
		self.size = size
		self.grid = world
		self.c = Canvas(self.window, width=size, height=size)
		self.c.pack()
		self.drawGrid(size, size)
		self.scale = Scale(self.window, from_=1, to=100, orient=HORIZONTAL,
                              length=200)
		self.scale.pack()
		for i in range(len(world)):
			for j in range(len(world[i])):
				if world[i][j] == -1:
					self.placePit(size/22,  i, j)
				elif world[i][j] == 1:
					pass
					self.placeGold(i, j)
		self.c.update()
		#self.window.mainloop()
	
	def placeGold(self, x, y):
		global goldImage
		goldImage = PhotoImage(file="rec/goal.png")
		goldImage = goldImage.subsample(math.ceil(max(goldImage.height(), goldImage.width()) / (self.size / 22)) + 2)
		ydiff = abs(goldImage.height() - (self.size / 22)) / 2
		xdiff = abs(goldImage.width() - (self.size / 22)) / 2
		x = (self.size / 22) * x + xdiff + (goldImage.width() / 2)
		y = (self.size / 22) * y + ydiff + (goldImage.height() / 2)
		self.c.create_image((x, y), image=goldImage)
	"""
		newx = size * x + 2
		newy = size * y + 2
		self.c.create_rectangle(newx, newy, newx+size - 4, newy+size - 4, fill="gold")
		"""
	
	def getSpeed(self):
		return 1 / float(self.scale.get())
	
	def placeAgent(self, x, y):
		self.c.delete('agent')
		global agentImage
		agentImage = PhotoImage(file='rec/Agent.png')
		agentImage = agentImage.subsample(math.ceil(max(agentImage.height(), agentImage.width()) / (self.size / 22)) + 3)
		ydiff = abs(agentImage.height() - (self.size / 22)) / 2
		xdiff = abs(agentImage.width() - (self.size / 22)) / 2
		x = (self.size / 22) * x + xdiff + (agentImage.width() / 2)
		y = (self.size / 22) * y + ydiff + (agentImage.height() / 2)
		self.c.create_image((x, y), image=agentImage, tag='agent')
		self.c.update()
		"""
		newx = (self.size / 22) * x + 2
		newy = (self.size / 22) * y + 2
		self.agentPos = (x, y)
		self.player = self.c.create_oval(newx, newy, newx+self.size/22 - 4, newy+self.size/22 - 4, fill="blue", tag='agent')
		self.c.update()
		"""
	
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
	s = Start()
"""
	world = World.loadWorld('world.txt')
	app = gui(700, world)
	app.placeAgent(5,5)
	app.moveAgent((-1, 0))
	app.window.mainloop()
"""

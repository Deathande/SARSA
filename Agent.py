import numpy as np
import World
import Gui
import time
import pickle
import sys
import curses

class Agent:
	def __init__(self, world, gui, fn, q_table, e, alpha, gamma, lamb, ed):
		self.world = world
		self.gui = gui
		self.q_table = q_table
		self.epsilon = e
		self.fileName = fn
		self.ed = ed
		self.e_table = []
		self.gamma = gamma
		self.alpha = alpha
		self.lamb = lamb
		self.action = np.random.randint(0, 4)
		self.actions = [np.array([1, 0]),  # move right
                                np.array([-1, 0]), # move left
                                np.array([0, -1]), # move down 
                                np.array([0, 1])]  # move up
		self.pos = np.array([5, 5])
		gui.placeAgent(self.pos[0], self.pos[1])
		for i in range(22):
			self.e_table.append([])
			for j in range(22):
				self.e_table[i].append([])
				for k in range(4):
					self.e_table[i][j].append(0)
	
	# Test if we should go where no Agent has gone before
	def newAction(self):
		rand = np.random.rand()
		if rand < self.epsilon:
			return np.random.randint(0, 4)
		maxum = 0
		index = 0
		x, y = self.pos
		for i in range(len(self.q_table[x][y])):
			if self.q_table[x][y][i] > maxum:
				maxum = self.q_table[x][y][i]
				index = i
		return index

	def epsilonDecay(self):
		# Subtract a percentage from epsilon after a terminal state has been reached
		# Don't go past .1
		if self.epsilon > .1:
			self.epsilon -= self.ed 
	
	def restart(self, dc):
		for i in range(22):
			for j in range(22):
				for k in range(4):
					#self.q_table[i][j][k] = np.random.rand() * .1
					self.e_table[i][j][k] = 0
		self.action = np.random.randint(0, 4)
		while True:
			self.pos = np.array([np.random.randint(1, 21), np.random.randint(1, 21)])
			x,y = self.pos
			if self.world[x][y] == 0:
				break
		if dc:
			self.epsilonDecay()
		self.gui.placeAgent(self.pos[0], self.pos[1])
	
	def takeAction(self):
		s = self.pos # save the current state
		self.pos += self.actions[self.action] # update current position, aka get s'
		self.gui.moveAgent(self.actions[self.action]) # update the gui
		x, y = self.pos
		r = self.world[x][y] # get the reward of the new state
		a = self.newAction() # get a new action from the new state
		delta = r + self.gamma * self.q_table[x][y][a] - self.q_table[s[0]][s[1]][self.action]
		self.e_table[s[0]][s[1]][self.action] += 1
		for i in range(len(self.q_table)):
			for j in range(len(self.q_table[i])):
				for k in range(4):
					self.q_table[i][j][k] += (self.alpha * delta  * self.e_table[i][j][k])
					self.e_table[i][j][k] *= (self.gamma * self.lamb )
		self.save()
		sys.stdout.write("Epsilon: " + str(self.epsilon) + "    \r")
		if r == -1:
			self.restart(False)
		if r == 1:
			#print()
			#print("goal!")
			self.restart(True) # Only decay epsilon if the goal state is reached.
		self.action = a
		time.sleep(self.gui.getSpeed())
	
	def load(self, fn):
		loaded = pickle.load(open(fn, "rb"))
		self.epsilon = loaded[-2]
		self.q_table = loaded[-1]
	
	def save(self):
		saveList = [self.alpha, self.gamma, self.lamb, self.ed, self.epsilon, self.q_table]
		pickle.dump(saveList, open(self.fileName, "wb"))

if __name__ == '__main__':
	if len(sys.argv) < 2:
		#print("Please specify name of save file")
		#print()
		exit(1)
	fn = sys.argv[1]
	world = World.loadWorld('world.txt')
	gui = Gui.gui(700, world)
	p = Agent(world,gui, fn, .4, .5, .4) # alpha, gamma, lambda
	while True:
		p.takeAction()


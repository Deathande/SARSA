import numpy as np
import World

class Agent:
	def __init__(self, world):
		self.world = world
		self.q_table = []
		self.e_table = []
		self.gamma = .5
		self.alpha = .5
		self.lamb = .5
		self.action = np.random.randint(0, 3)
		self.actions = [np.array([1, 0]),  # move right
                                np.array([-1, 0]), # move left
                                np.array([0, -1]), # move down 
                                np.array([0, 1])]  # move up
		self.epsilon = .9
		self.pos = np.array([5, 5])
		for i in range(20):
			self.q_table.append([])
			self.e_table.append([])
			for j in range(20):
				self.q_table[i].append([])
				self.e_table[i].append([])
				for k in range(4):
					self.q_table[i][j].append(np.random.rand() * .1)
					self.e_table[i][j].append(0)

	# Test if we should go where no Agent has gone before
	def doExplore(self):
		rand = np.random.rand()
		if rand < self.epsilon:
			return True
		return False
	
	def takeAction(self):
		if self.doExplore():
			# pick a random action
			action = self.actions[np.random.randint(0,3)]
		else:
			# Find the action with the largest value
			m = 0
			x = self.pos[0]
			y = self.pos[1]
			for i in range(len(self.q_table[self.pos[0]][self.pos[1]])):
				if self.q_table[x][y] > m:
					m = self.q_table[x][y][i]
					index = i
			action = self.actions[index]
		oldq = self.q_table[self.pos[0]][self.pos[1]][self.action]
		self.pos += action
		r = self.world[self.pos[0]][self.pos[1]]
		x = self.pos[0]
		y = self.pos[1]
		delta = r + self.gamma * self.q_table[x][y][action] - oldq
					
if __name__ == '__main__':
	world = World.loadWorld('world.txt')
	for line in world:
		print (line)
	p = Agent(world)

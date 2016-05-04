import Agent
import numpy as np
import World
import Gui
import sys
import pickle
import threading

# This keeps the animation loop from blocking the slider.
# Otherwise when the action method reaches the sleep
# timer, it blocks everything and the slider can't be
# moved. This method get's its own thread of execution.
def actionLoop(agent):
	try:
		while True:
			agent.takeAction()
	except KeyboardInterrupt:
		agent.save()
		exit(0)

if len(sys.argv) == 2:
	fn = sys.argv[1]
	params = pickle.load(open(fn, "rb"))
	a = params[0]
	g = params[1]
	l = params[2]
	ed = params[3]
	e = params[4]
	q_table = params[5]

elif len(sys.argv) == 6:
	fn = sys.argv[1]
	a = float(sys.argv[2])
	g = float(sys.argv[3])
	l = float(sys.argv[4])
	ed = float(sys.argv[5])
	e = .9
	q_table = []
	for i in range(22):
		q_table.append([])
		for j in range(22):
			q_table[i].append([])
			for k in range(4):
				q_table[i][j].append(np.random.rand() * .1)
else:
	gui = Gui.Start()
	a = gui.params[0]
	g = gui.params[1]
	l = gui.params[2]
	ed = gui.params[3]
	e = gui.params[4]
	q_table = gui.params[5]
	fn = gui.fn
				
print("here")
world = World.loadWorld('world.txt')
gui = Gui.gui(1000, world)
agent = Agent.Agent(world, gui, fn, q_table, e, a, g, l, ed) # alpha, gamma, lambda, Epsilon Decay

t = threading.Thread(target=actionLoop, args=[agent])
t.start()
gui.window.mainloop()

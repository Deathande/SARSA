import Agent
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

if len(sys.argv) == 1:
	gui = Gui.Start()
	fn = gui.fn
	print(fn)
	params = pickle.load(open(fn, "rb"))
	a = params[0]
	g = params[1]
	l = params[2]
	ed = params[3]
	print(a)
	print(g)
	print(l)
	print(ed)

if len(sys.argv) < 6 and len(sys.argv) > 1:
	print("Required arguments: save file, alpha, gamma, lambda, Epsilon decay")
	exit(1)
	fn = sys.argv[1]
	a = float(sys.argv[2])
	g = float(sys.argv[3])
	l = float(sys.argv[4])
	ed = float(sys.argv[5])
world = World.loadWorld('world.txt')
gui = Gui.gui(400, world)
agent = Agent.Agent(world, gui, fn, a, g, l, ed) # alpha, gamma, lambda, Epsilon Decay

t = threading.Thread(target=actionLoop, args=[agent])
t.start()
gui.window.mainloop()

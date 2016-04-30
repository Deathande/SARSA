import Agent
import World
import Gui
import sys

if len(sys.argv) < 5:
	print("Required arguments: save file, alpha, gamma, lambda")
	exit(1)
fn = sys.argv[1]
a = float(sys.argv[2])
g = float(sys.argv[3])
l = float(sys.argv[4])
world = World.loadWorld('world.txt')
gui = Gui.gui(400, world)
agent = Agent.Agent(world, gui, fn, a, g, l) # alpha, gamma, lambda
while True:
	agent.takeAction()

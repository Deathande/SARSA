import numpy as np
import re

def loadWorld(fn):
	f = open(fn, 'r')
	w = []
	for line in f:
		w.append([int(x) for x in re.split("\s*(?=-?\d)", line)])
	return w

if __name__ == '__main__':
	w = loadWorld('world.txt')
	for line in w:
		print(len(line))

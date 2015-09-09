#python3
import enum

class State():
	def __init__(self, value, accept):
		self.value = value
		self.transitions = {}
		self.accept = accept

	def addTransition(self, transition):
		self.transitions[transition.symbol] = transition

	def step(self, symbol):
		try:
			transition = transitions[symbol]
			return transition.nextState, transition.direction
		except KeyError as e:
			raise e

class Transition():
	class Direction(enum.Enum):
		RIGHT = 1
		LEFT  = 2

	def __init__(self, symbol, nextState, direction):
		self.symbol    = symbol
		self.nextState = nextState
		self.direction = direction

class Tape():
	def __init__(self, cells):
		self.cells    = cells
		self.position = 0

	def head(self):
		return cells[position]

	def headPosition(self):
		return position

	def reachEnd(self):
		position == -1 or position == len(cells)
	
	def update(self, direction):
		if reachEnd():
			raise Exception('End of computation.')
		if direction == Transition.Direction.RIGHT:
			position += 1
		else:
			position -= 1


class Automaton():
	pass
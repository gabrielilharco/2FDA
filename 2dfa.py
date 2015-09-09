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
	def __init__(self):
		self.states = None
		self.currentState = None
		self.tape = None
		self.visited = Set([])
		self.simulating = True
		self.initialState = None

	def addNode(self, state):
		states.add(node)

	def addEdge(self, startState, transition):
		startState.addTransition(transition)

	def setInitState (self, state):
		currentState = state
		initialState = state

	def setTape (self, tape):
		tape = tape

	def startOver(self):
		currentState = initialState
		tape.setPosition(0)

	def simulateStep(self):
		if not simulating:
			return "Simulation has stopped."
		currentState, direction = currentState.doStep(tape.head())
		tape.update(direction)
		if (currentState, tape.headPosition()) in visited:
			# infinite loop, end simulation
			simulating = False
			return "Reached a loop. Simulation stopped."
		elif tape.reachedEnd():
			# end of tape, end simulation
			if currentState.accept:
				return "End of simulation. Tape accepted."
			else:
				return "End of simulation. Tape not accepted."
		else:
			visited.add((currentState, tape.headPosition))


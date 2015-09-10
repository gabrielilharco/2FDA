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

	def reset (self):
		position = 0

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
		self.states = {}
		self.currentState = None
		self.tape = None
		self.visited = set()
		self.simulating = True
		self.initialState = None

	def addState(self, state):
		self.states[state.value] = state

	def addTransition(self, sourceState, transition):
		self.states[sourceState].addTransition(transition)

	def setInitState (self, state):
		self.currentState = self.states[state]
		self.initialState = self.states[state]

	def setTape (self, tp):
		self.tape = tp

	def startOver(self):
		self.currentState = self.initialState
		self.tape.reset()
		self.simulating = True

	def getState (self, stateValue):
		return self.states[stateValue]

	def simulateStep(self):
		if not simulating:
			return "Simulation has stopped.\n"
		self.currentState, self.direction = self.currentState.step(self.tape.head())
		self.tape.update(direction)
		if (self.currentState, self.tape.headPosition()) in visited:
			# infinite loop, end simulation
			self.simulating = False
			return "Reached a loop. Simulation stopped.\n"
		elif self.tape.reachEnd():
			# end of tape, end simulation
			self.simulating = False
			if self.currentState.accept:
				return "End of simulation. Tape accepted.\n"
			else:
				return "End of simulation. Tape not accepted.\n"
		else:
			visited.add((self.currentState, self.tape.headPosition))
			return "Position: " + str(self.tape.headPosition()) + ", Direction " + self.direction.name + ", State: " + self.currentState.value + "\n"

	def simulate(self):
		f = open("log.txt", "a")
		f.write("--------------------------------------\n")
		f.write("Beginning simulation\n\n");
		self.startOver()
		while simulating:
			logEntry = simulateStep()
			f.write(logEntry);


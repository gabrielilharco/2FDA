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
			transition = self.transitions[symbol]
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

	def reachEnd(self):
		return self.position < 0 or self.position >= len(self.cells)

	def head(self):
		if self.reachEnd():
			return -1
		return self.cells[self.position]

	def reset (self):
		self.position = 0

	def headPosition(self):
		return self.position
	
	def update(self, direction):
		if self.reachEnd():
			raise Exception('End of computation.')
		if direction == Transition.Direction.RIGHT:
			self.position += 1
		else:
			self.position -= 1



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
		self.visited = {(self.currentState.value, self.tape.headPosition())}
		return self.initialState.value + self.tape.cells + "\n"

	def getState (self, stateValue):
		return self.states[stateValue]

	def simulateStep(self):
		if not self.simulating:
			return "Computation has stopped.\n"
		self.currentState, self.direction = self.currentState.step(self.tape.head())
		self.tape.update(self.direction)
		if (self.currentState.value, self.tape.headPosition()) in self.visited:
			# infinite loop, end computation
			self.simulating = False
			return "\nReached a loop. Computation stopped.\n"
		elif self.tape.reachEnd():
			# end of tape, end computation
			self.simulating = False
			log = self.tape.cells[:self.tape.headPosition()] + self.currentState.value + self.tape.cells[self.tape.headPosition():]+"\n"
			if self.currentState.accept: 
				return log + "\nEnd of computation. Tape accepted.\n"
			else:
				return log + "\nEnd of computation. Tape not accepted.\n"
		else:
			self.visited.add((self.currentState.value, self.tape.headPosition()))
			log = self.tape.cells[:self.tape.headPosition()] + self.currentState.value + self.tape.cells[self.tape.headPosition():]+"\n"
			return log

	def simulate(self):
		f = open("log.txt", "a")
		f.write("Beginning computation\n\n")
		f.write(self.startOver())
		while self.simulating:
			logEntry = self.simulateStep()
			f.write(logEntry);
		f.write("--------------------------------------\n")


#python3

from sets import Set


class State():
	pass

class Transition():
	pass

class Tape():
	pass

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



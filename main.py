from bdfa import *
import sys

def createAutomaton():

	f = open(sys.argv[1], "r")

	nStates, nTransitions = map(int, f.readline().strip().split())
	aut = Automaton()

	#reading states
	for i in range (0, nStates):
		line = f.readline().strip().split()
		value = line[0]
		accepted = bool(int(line[1]))
		state = State(value, accepted)
		aut.addState(state)

	#reading transitions
	for i in range (0, nTransitions):
		line = f.readline().strip().split()
		source = line[0]
		destination = line[1]
		symbol = line[2]
		direction = Transition.Direction.RIGHT if line[3] == 'R' else Transition.Direction.LEFT
		transition = Transition(symbol, aut.getState(destination), direction)
		aut.addTransition(source, transition)

	#read initial state
	initialState = f.readline().strip()
	aut.setInitState(initialState)

	return aut

def readTape():
	f = open(sys.argv[2], "r")

	string = f.readline().strip()
	tape = Tape(string)

	return tape

if __name__ == "__main__":
    #read file and create automaton
    automaton = createAutomaton()
    #read tape
    tape = readTape()
    automaton.setTape(tape)
    #simulate
    automaton.simulate()

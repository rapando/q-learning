from random import randint

class QLearning():
	def __init__ (self, y):
		self.y = y
		self.currentState = 0
		self.possibleActions = self.possibleActionPositions = self.possibleActions2 = self.possibleActionPositions2 = []
		self.selectedAction = 0
		self.rooms = ["A" , "B", "C", "D", "E", "F"]

		self.R = [["-" for x in range (6)] for i in range (6)]
		self.Q = [[0 for x in range(6)] for i in range(6)]
		
		print ("y set to ", self.y)

		# Assign default reward values
		self.R[0][4] = self.R[4][0] = 0
		self.R[1][3] = self.R[3][1] = 0
		self.R[1][5] =  100
		self.R[2][3] = self.R[3][2] = 0
		self.R[3][4] = self.R[4][3] = 0
		self.R[4][5] =  100
		self.R[5][5] = 100
		self.R[5][1] = self.R[5][4] = 0		

	def printR(self):
		print ("\nThe Current Reward Matrix")
		for i in self.R:
			for j in i:
				print (j, end = "\t")
			print ()

	def printQ(self):
		print ("\nThe Current Q Matrix")
		for i in self.Q:
			for j in i:
				print (j, end = "\t")
			print ()

	def episode (self, currentState):
		# first, randomly choose a state
		self.currentState = currentState

		while True:
			print ("\nCurrent State is ", self.rooms[self.currentState])
			# get the possible actions
			self.possibleActions = [action for action in self.R[self.currentState] if action != "-"]
			self.possibleActionPositions = [i for i in range(6) if self.R[self.currentState][i] != "-"]	
			print ("The possible Action States from ", self.rooms[self.currentState], " are ", [self.rooms[i] for i in self.possibleActionPositions])
			#Randomly select an action
			self.selectedAction = self.possibleActionPositions [randint (0, len(self.possibleActions) - 1)]

			print ("The selected Action state is ", self.rooms[self.selectedAction])

			print ("\nTaking the current action as the state")
			self.possibleActions2 = [action for action in self.R[self.selectedAction] if action != "-"]
			self.possibleActionPositions2 = [i for i in range(6) if self.R[self.selectedAction][i] != "-"]
			print ("The possible Action States from ", self.rooms[self.selectedAction], " are ", [self.rooms[i] for i in self.possibleActionPositions2], end = " ")
			# calculate the reward value in Q array
			rewards = [ self.Q[self.selectedAction][x] for x in self.possibleActionPositions2]
			print ("with Q values : ", rewards)
			self.Q[self.currentState][self.selectedAction] = round (self.R[self.currentState][self.selectedAction] + (0.8 * max (rewards)), 0)

			self.printQ()
			if self.selectedAction == 5 : 
				print ("*" * 30, "\nEnd of Episode\n", "*" * 30)
				break
			else : 
				self.currentState = self.selectedAction


	def testPath (self):
		print ("*" * 30, "\nEnd of Episode\n", "*" * 30)
		
		while True:
			room = input ("Enter Room : ").upper()
			if len (room) == 1 and room in self.rooms : break
		path = room + " -> "
		roomPosition = self.rooms.index(room)
		while True:
			self.possibleActions = [action for action in self.Q[roomPosition] if action != "-"]
			bestRoom = self.possibleActions.index (max(self.possibleActions))
			path += self.rooms[bestRoom]
		
			if bestRoom == 5:
				break
			else:
				roomPosition = bestRoom
				path += " -> "

		print ("The best Path is  :: ", path)

while True:
	try:
		y = float(input ("\nEnter the y value 0 <= y <1 : "))
		if y >= 0 and y < 1 : break
	except:
		print ("y must be a valid value between 0 and 1")



ql = QLearning(y);
ql.printR()
ql.printQ()

i = 0
while i < 100:
	state = randint(0,5)
	ql.episode(state)
	i += 1
ql.testPath()
	
import random, os

class Gameboard:
	"""Class to represent the gameboard on which the
		game will be played.

	Attributes:
		length (Optional [int]): The length of the gameboard. 
			Currently length should not be changed.
		visibleGameboard (list): Nested list containing the 
			gameboard that will be displayed to the user.
		invisibleGameboard (list): Nested list containing 
			ships' locations. 
		hits (int): Counter for the number of guesses the
			user have made.
	""" 
	_letters = [
			"A","B","C","D","E",
			"F","G","H","I","J"
            ]
	
	def __init__(self):
		"""Gameboard init method.
			
		"""
		#In the current version of the game the gameboard has a fixed size of 11 squares.
		self.length = 11
		self.visibleGameboard = [ [ "." for x in \
			range(self.length)]for y in range(self.length)]
		self.invisibleGameboard = [ [ " " for x in \
			range(self.length)]	for	y in range(self.length)]
		self.hits = 0

		for col in range(self.length):
			for row in range(self.length):
				if (col==0) and (row==0):
					self.visibleGameboard[row][col] = " "
					self.invisibleGameboard[row][col] = " "
				elif (col==0) and (row!=0):
					self.invisibleGameboard[row][col] = \
						Gameboard._letters[row-1]
					self.visibleGameboard[row][col] = \
						Gameboard._letters[row-1]
				elif (col!=0) and (row==0):
					self.visibleGameboard[row][col] = col
					self.invisibleGameboard[row][col] = col

	@staticmethod
	def refresh_screen():
		"""Method that sets the clear command according to the 
		operation system in use.
		"""
		if os.name=='nt':
			os.system('cls')
		else:
			os.system('clear')

	def print_board(self, type):
		"""Method that displays the visibleGameboard
		or invisibleGameboard depending on the type
		argument.

		Args:
			type (int): 1 for visibleGameboard, 
				2 for invisibleGameboard
		"""
		if type == 1:
			boardToPrint = self.visibleGameboard
		elif type == 2:
			boardToPrint = self.invisibleGameboard

		for row in range(self.length):
			currRow = ""
			for col in range(self.length):
				currRow = currRow + " " \
						+ str(boardToPrint[row][col])
			print(currRow)

	def hit_and_get_result(self, inputStr):
		"""Method that parses the input from the console,
		sets the result on the visibleGameboard property and
		returns the result from the operation.
		
		Args:
			inputStr (str): The input from user to be parsed.
		"""
		y = 0
		if len(inputStr) > 0:
			y = inputStr[0].upper()

		if y in Gameboard._letters:
			y = Gameboard._letters.index(y)+1
		else:
			y = 0

		try:
			x = int(inputStr[1:])
		except:
			x=0

		self.hits+=1
		if (y > len(Gameboard._letters)) or \
           (x >= self.length) or y<1 or x<1:
			message = "Error"
		else:
			if self.visibleGameboard[y][x] != ".":
				message = "Miss"
			else:
				if self.invisibleGameboard[y][x] == "X":
					message = "Hit"
					self.visibleGameboard[y][x] = "X"
				else:
					message = "Miss"
					self.visibleGameboard[y][x] = "-"
		return message

import random

class Ship:
	"""Class to represent a ship that will be present on a gameboard.

	Attributes:
		length (int): The length of the ship.
		alive (bool): Is the ship still allive /not destroyed/?
		AliveShips @static (int): Number of ships that are alive
		_shipCoordinatesY (list int): Y coordinates of ship
		_shipCoordinatesX (list int): X coordinates of ship
	"""
	AliveShips = 0
	ships = []

	def __init__(self, length, Gameboard):
		"""Ship init method.

		Args:
			length (int): The length of the ship.
			gameboard (Gameboard): The gameboard object that the ship will be
				placed on.
		"""
		self.alive = True
		self.length = length
		self._shipCoordinatesY = []
		self._shipCoordinatesX = []
		self._createShip(self.length, Gameboard)
		Ship.ships.append(self)
		Ship.AliveShips += 1

	def _createShip(self, shipLength, Gameboard):
		"""Method that will find possible ship coordinates
		and set them in _shipCoordinatesY and _shipCoordinatesX

		Args:
			length (int): The length of the ship.
			gameboard (Gameboard): The gameboard object for the ship to be
				placed on.
		"""
		tempX = []
		tempY = []
		_shipOrientation = random.randint(0, 1)#0 1=horizontal; 0=vertical
		collision = False

		if _shipOrientation:
			x=random.randint(1, Gameboard.length-shipLength)
			y=random.randint(1, Gameboard.length-1)
			for _ in range(shipLength):
				tempX.append(x)
				tempY.append(y)
				x += 1
		else:
			x=random.randint(1, Gameboard.length-1)
			y=random.randint(1, Gameboard.length-shipLength)
			for _ in range(shipLength):
				tempX.append(x)
				tempY.append(y)
				y += 1

		#check for collision
		for y in tempY:
			for x in tempX:
				if Gameboard._invisibleGameboard[y][x] != " ":
					collision = True
		
		if not collision:
			self._shipCoordinatesY = tempY
			self._shipCoordinatesX = tempX
		else:
			self._createShip(self.length, Gameboard)



	def placeShipOnGameboard(self, Gameboard, objectCoordinatesY,
                             objectCoordinatesX):
		"""Method that will place a ship on the gameboard object,
		according to the Y and X coordinates passed in.

		Args:
			Gameboard (Gameboard): The gameboard object for the 
				ship to be placed on.
			_shipCoordinatesY (list int): Y coordinates of ship.
			_shipCoordinatesX (list int): X coordinates of ship.
		"""
		for col in range(1, Gameboard.length):
			for row in range(1, Gameboard.length):
				if (col in objectCoordinatesX) and (row in objectCoordinatesY):
					Gameboard._invisibleGameboard[row][col] = "X"

	def getCoordinates(self):
		"""
		Get method that returns tuple containing:
			1 - _shipCoordinatesY (list int): Y coordinates of ship
			2 - _shipCoordinatesX (list int): X coordinates of ship
		"""
		return self._shipCoordinatesY, self._shipCoordinatesX

	@staticmethod
	def isDead(Gameboard):
		"""isDead method (static)

		Checks if any instanse of the Ship class that is currently 
		alive has been hit n times equal to its length. If yes returns
		True and sets the alive property to false, else returns False.
		"""

		for ship in Ship.ships:
			hitCounter = 0
			if ship.alive:				
				for i in range(ship.length):
					if Gameboard._visibleGameboard \
					[ship._shipCoordinatesY[i]] \
					[ship._shipCoordinatesX[i]] == "X":
						hitCounter += 1

				if hitCounter == ship.length:
					ship.alive = False
					Ship.AliveShips -= 1
					return True
		return False

class Destroyer(Ship):
	"""Destroyer Class. 

	Inherits Ship Class
	Has preset length of 4. 
	"""
	def __init__(self, Gameboard):
		"""Destroyer init method.

		Args:
			gameboard (Gameboard): The gameboard object that the ship will be
				placed on.
		"""
		Ship.__init__(self, 4, Gameboard)
		
class Battleship(Ship):
	"""Battleship Class. 

	Inherits Ship Class
	Has preset length of 5. 
	"""
	def __init__(self, Gameboard):
		"""Battleship init method.

		Args:
			gameboard (Gameboard): The gameboard object that the ship will be
				placed on.
		"""
		Ship.__init__(self, 5, Gameboard)

from Gameboard import Gameboard
from Ship import Ship, Battleship, Destroyer

if __name__ == "__main__":

	gb = Gameboard()

	ships = [Battleship, Destroyer, Destroyer]

	for ship in ships:
		bs1 = ship(gb)
		bs1.placeShipOnGameboard(gb, *bs1.getCoordinates())

	resultFromHit = ""
	gb.printBoard(1)
	while True:
		inp = input("Enter coordinates (row, col), e.g. A5 = ")
		if inp.lower() == "show":
			gb.refreshScreen()
			print(" \n")
			gb.printBoard(2)
		else:
			resultFromHit = gb.hitAndPrintResult(inp)

			if Ship.isDead(gb):
				resultFromHit = "Sunk"

			gb.refreshScreen()
			if resultFromHit != "":
				print("*** {} *** \n".format(resultFromHit))
			
			gb.printBoard(1)
			if Ship.AliveShips<=0:
				print( \
					"Well done! You completed the game in {} shots" \
					.format(gb.hits))
				break

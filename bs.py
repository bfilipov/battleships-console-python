from Gameboard import Gameboard
from Ship import Ship, Battleship, Destroyer

if __name__ == "__main__":
	gb = Gameboard()
	ships = [Battleship, Destroyer, Destroyer]
	for ship in ships:
		ship(gb).place_ship_on_gameboard()

	resultFromHit = ""
	gb.print_board(1)
	while True:
		inp = input("Enter coordinates (row, col), e.g. A5 = ")
		if inp.lower() == "show":
			gb.refresh_screen()
			print(" \n")
			gb.print_board(2)
		else:
			resultFromHit = gb.hit_and_get_result(inp)

			if Ship.is_any_dead(gb):
				resultFromHit = "Sunk"

			gb.refresh_screen()
			if resultFromHit != "":
				print("*** {} *** \n".format(resultFromHit))
			
			gb.print_board(1)
			if Ship.AliveShips<=0:
				print("Well done! You completed the game in {} shots" \
					.format(gb.hits))
				break

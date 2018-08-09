import unittest
from Ship import Ship
from Gameboard import Gameboard

class TestShip(unittest.TestCase):

	def test_ship(self):
		gb = Gameboard()
		ship1 = Ship(5,gb)
		ship1.place_ship_on_gameboard()

		for i in range(ship1.length):
				self.assertEqual(gb.invisibleGameboard[ship1._shipCoordinatesY[i]][ship1._shipCoordinatesX[i]],"X")


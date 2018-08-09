import unittest
from Ship import Ship, Battleship, Destroyer
from Gameboard import Gameboard

class TestShip(unittest.TestCase):

	def test_ship_length_5(self):
		gb = Gameboard()
		ship1 = Ship(5, gb)
		ship1.place_ship_on_gameboard()

		self.assertTrue(ship1.alive)
		self.assertEqual(ship1.length, 5)
		self.assertEqual(ship1.Gameboard, gb)

		for i in range(ship1.length):
				self.assertEqual(gb.invisibleGameboard \
					[ship1._shipCoordinatesY[i]] \
					[ship1._shipCoordinatesX[i]], "X")

	def test_ship_length_4(self):
		gb = Gameboard()
		ship2 = Ship(4, gb)
		ship2.place_ship_on_gameboard()

		self.assertTrue(ship2.alive)
		self.assertEqual(ship2.length, 4)
		self.assertEqual(ship2.Gameboard, gb)

		for i in range(ship2.length):
				self.assertEqual(gb.invisibleGameboard \
					[ship2._shipCoordinatesY[i]] \
					[ship2._shipCoordinatesX[i]], "X")

	def test_ship_length_3(self):
		gb = Gameboard()
		ship3 = Ship(3, gb)
		ship3.place_ship_on_gameboard()

		self.assertTrue(ship3.alive)
		self.assertEqual(ship3.length, 3)
		self.assertEqual(ship3.Gameboard, gb)

		for i in range(ship3.length):
				self.assertEqual(gb.invisibleGameboard \
					[ship3._shipCoordinatesY[i]] \
					[ship3._shipCoordinatesX[i]], "X")


	def test_Destroyer(self):
		gb = Gameboard()
		destroyer1 = Destroyer(gb)
		destroyer1.place_ship_on_gameboard()

		self.assertTrue(destroyer1.alive)
		self.assertEqual(destroyer1.length, 4)
		self.assertEqual(destroyer1.Gameboard, gb)

		for i in range(destroyer1.length):
				self.assertEqual(gb.invisibleGameboard \
					[destroyer1._shipCoordinatesY[i]] \
					[destroyer1._shipCoordinatesX[i]], "X")

	def test_Battleship(self):
		gb = Gameboard()
		battleship1 = Battleship(gb)
		battleship1.place_ship_on_gameboard()

		self.assertTrue(battleship1.alive)
		self.assertEqual(battleship1.length, 5)
		self.assertEqual(battleship1.Gameboard, gb)

		for i in range(battleship1.length):
				self.assertEqual(gb.invisibleGameboard \
					[battleship1._shipCoordinatesY[i]] \
					[battleship1._shipCoordinatesX[i]], "X")

	def test_is_any_dead(self):
		gb = Gameboard()
		battleship1 = Battleship(gb)
		battleship1.place_ship_on_gameboard()

		destroyer1 = Destroyer(gb)
		destroyer1.place_ship_on_gameboard()

		destroyer2 = Destroyer(gb)
		destroyer2.place_ship_on_gameboard()

		self.assertFalse(Ship.is_any_dead(gb))

		for i in range(battleship1.length):
			gb.visibleGameboard \
				[battleship1._shipCoordinatesY[i]] \
				[battleship1._shipCoordinatesX[i]] = "X"

		self.assertTrue(Ship.is_any_dead(gb))
		self.assertFalse(Ship.is_any_dead(gb))

		for i in range(destroyer1.length):
			gb.visibleGameboard \
				[destroyer1._shipCoordinatesY[i]] \
				[destroyer1._shipCoordinatesX[i]] = "X"

		self.assertTrue(Ship.is_any_dead(gb))
		self.assertFalse(Ship.is_any_dead(gb))

		for i in range(destroyer2.length):
			gb.visibleGameboard \
				[destroyer2._shipCoordinatesY[i]] \
				[destroyer2._shipCoordinatesX[i]] = "X"

		self.assertTrue(Ship.is_any_dead(gb))
		self.assertFalse(Ship.is_any_dead(gb))

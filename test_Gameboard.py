import unittest
from Gameboard import Gameboard

letters = [
			"A","B","C","D","E",
			"F","G","H","I","J"
            ]

class TestGameboard(unittest.TestCase):

	def test_gameboard(self):
		global letters 
		gb = Gameboard()
		self.assertEqual(gb.length, 11)
		self.assertEqual(gb.visibleGameboard[0][0], " ")
		self.assertEqual(gb.invisibleGameboard[0][0], " ")
		for y in range(1,gb.length):
			for x in range(1,gb.length):
				self.assertEqual(gb.visibleGameboard[y][x], ".")
				self.assertEqual(gb.invisibleGameboard[y][x], " ")

		for y in range(1,gb.length):
			self.assertEqual(gb.visibleGameboard[y][0], letters[y-1])
			self.assertEqual(gb.invisibleGameboard[y][0], letters[y-1])

		for x in range(1,gb.length):
			self.assertEqual(gb.visibleGameboard[0][x], x)
			self.assertEqual(gb.invisibleGameboard[0][x], x)

	def test_print_board(self):
		global letters 
		gb = Gameboard()
		for row in range(gb.length):
			currRow = ""
			for col in range(gb.length):
				currRow = currRow + " " + str(gb.visibleGameboard[row][col])
			if row==0:
				self.assertEqual(currRow, "   1 2 3 4 5 6 7 8 9 10")
			else:
				self.assertEqual(currRow, " {} . . . . . . . . . .". \
					format(letters[row-1]))

	def test_hit_and_get_result(self):
		gb1 = Gameboard()
		gb1.invisibleGameboard[1][1] = "X"
		gb1.invisibleGameboard[1][2] = "X"
		gb1.invisibleGameboard[1][3] = "X"

		self.assertEqual(gb1.hit_and_get_result("A1"), "Hit")
		self.assertEqual(gb1.visibleGameboard[1][1], "X")

		self.assertEqual(gb1.hit_and_get_result("A2"), "Hit")
		self.assertEqual(gb1.visibleGameboard[1][2], "X")

		self.assertEqual(gb1.hit_and_get_result("A3"), "Hit")
		self.assertEqual(gb1.visibleGameboard[1][3], "X")

		self.assertEqual(gb1.hit_and_get_result("A4"), "Miss")
		self.assertEqual(gb1.visibleGameboard[1][4], "-")

		self.assertEqual(gb1.hit_and_get_result("F4"), "Miss")
		self.assertEqual(gb1.visibleGameboard[6][4], "-")

		self.assertEqual(gb1.visibleGameboard[1][5], ".")

		self.assertEqual(gb1.visibleGameboard[6][6], ".")

		self.assertEqual(gb1.hit_and_get_result("A11"), "Error")

		self.assertEqual(gb1.hit_and_get_result(""), "Error")

		self.assertEqual(gb1.hit_and_get_result("asdf"), "Error")

		self.assertEqual(gb1.hit_and_get_result("11"), "Error")

		self.assertEqual(gb1.hit_and_get_result("99999999999999999999999999"), "Error")

		self.assertEqual(gb1.hit_and_get_result("A99999999999999999999999999"), "Error")
		
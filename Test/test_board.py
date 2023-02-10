import unittest
import main.player_helpers
import main.battleship_enumerations as enum

class Test(unittest.TestCase):
    def test_upper(self):
        p = main.player_helpers.Board(10, 10)
        c = main.player_helpers.Coordinate("A", 0)
        self.assertEqual(p.get_piece(c), enum.Piece.EMPTY)

if __name__ == '__main__':
    unittest.main()
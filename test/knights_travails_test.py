import unittest

from knights_travails import *


class KnightsMovementTest(unittest.TestCase):
    def test_generate_valid_moves_returns_all_possible_moves(self):
        moves = generate_valid_moves((3, 3))

        self.assertEqual([(4, 5), (4, 1), (2, 5), (2, 1), (5, 4), (1, 4), (5, 2), (1, 2)], moves)

    def test_generate_valid_moves_limits_to_the_board_size(self):
        moves = generate_valid_moves((0, 0))

        self.assertEqual([(1, 2), (2, 1)], moves)


if __name__ == '__main__':
    unittest.main()

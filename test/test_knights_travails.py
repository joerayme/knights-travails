import unittest
from unittest.mock import patch

from knights_travails import *


class KnightsMovementTest(unittest.TestCase):
    def test_generate_valid_moves_returns_all_possible_moves(self):
        moves = generate_valid_moves((3, 3))

        self.assertEqual([(4, 5), (4, 1), (2, 5), (2, 1), (5, 4), (1, 4), (5, 2), (1, 2)], moves)

    def test_generate_valid_moves_limits_to_the_board_size(self):
        moves = generate_valid_moves((0, 0))
        self.assertEqual([(1, 2), (2, 1)], moves)

        moves = generate_valid_moves((7, 7))
        self.assertEqual([(6, 5), (5, 6)], moves)

        moves = generate_valid_moves((1, 1))
        self.assertEqual([(2, 3), (0, 3), (3, 2), (3, 0)], moves)

    def test_get_shortest_path_returns_shortest_distance(self):
        moves = get_shortest_path((0, 7), (1, 6))

        self.assertEqual(4, len(moves))

    def test_get_chess_notation_displays_correct_format(self):
        self.assertEqual(get_chess_notation((0, 0)), 'A1')
        self.assertEqual(get_chess_notation((0, 1)), 'A2')
        self.assertEqual(get_chess_notation((4, 7)), 'E8')

    @patch('knights_travails.get_shortest_path')
    def test_main_parses_input_and_returns_correct_output(self, get_shortest_path_mock):
        get_shortest_path_mock.return_value = [(2, 2), (1, 1)]

        self.assertEqual('C3 B2', main(['A1', 'B2']))

        get_shortest_path_mock.assert_called_once_with((0, 0), (1, 1))

    def test_main_does_not_parse_invalid_chess_position(self):
        try:
            main(['99', 'B2'])
            self.fail('Expected parsing of "99" to fail')
        except ValueError as e:
            self.assertEqual('"99" is not valid chess notation', str(e))

    def test_main_does_not_parse_invalid_chess_notation(self):
        try:
            main(['A1', 'chess'])
            self.fail('Expected parsing of "chess" to fail')
        except ValueError as e:
            self.assertEqual('"chess" is not valid chess notation', str(e))

    def test_main_does_not_parse_chess_notation_that_is_too_long(self):
        try:
            main(['A1', 'A111'])
            self.fail('Expected parsing of "A111" to fail')
        except ValueError as e:
            self.assertEqual('"A111" is not valid chess notation', str(e))

    def test_main_checks_number_of_args(self):
        try:
            main(['A1'])
            self.fail('Expected "A1" input to be too short')
        except ValueError as e:
            self.assertEqual('Did not receive two chess notation positions', str(e))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
import sys

BOARD_SIZE = 8
ASCII_A = 65


def generate_valid_moves(position):
    """
    Generates a list of all valid moves from a given position

    :param position: A position from which to generate all valid moves
    :return: List of all valid moves from the given position
    """
    x, y = position
    moves = []

    moves.append((x + 1, y + 2))
    moves.append((x + 1, y - 2))
    moves.append((x - 1, y + 2))
    moves.append((x - 1, y - 2))
    moves.append((x + 2, y + 1))
    moves.append((x - 2, y + 1))
    moves.append((x + 2, y - 1))
    moves.append((x - 2, y - 1))

    return [pos for pos in moves if is_valid_move(pos)]


def is_valid_move(end_position):
    """
    Determines if the given position is in the board

    :param end_position: The position to evaluate
    :return: Boolean whether the position is on the board or not
    """
    return 0 <= end_position[0] < BOARD_SIZE and 0 <= end_position[1] < BOARD_SIZE


def get_shortest_path(start, target):
    """
    Gets the shortest path between start and target

    :param start:
    :param target:
    :return: A list of positions between start and target
    """
    queue = [(start, [])]

    while queue:
        (current_position, path) = queue.pop(0)

        for next_move in set(generate_valid_moves(current_position)) - set(path):
            if next_move == target:
                return path + [target]
            else:
                queue.append((next_move, path + [next_move]))


def get_chess_notation(position):
    """
    Returns the chess notation of a given position

    :param position:
    :return:
    """
    return f'{chr(position[0] + ASCII_A)}{position[1] + 1}'


def parse_chess_notation(position):
    """
    Parses chess notation into a position and validates it is correct notation

    :param position: A chess board position in notation e.g. A5
    :return: A tuple position
    """
    error = f'"{position}" is not valid chess notation'
    try:
        pos = ord(position[0].upper()) - ASCII_A, int(position[1]) - 1
    except ValueError:
        raise ValueError(error)

    if len(position) != 2 or not is_valid_move(pos):
        raise ValueError(error)

    return pos


def main(positions):
    if len(positions) != 2:
        raise ValueError('Did not receive two chess notation positions')

    start, end = positions

    path = get_shortest_path(parse_chess_notation(start), parse_chess_notation(end))

    return ' '.join([get_chess_notation(pos) for pos in path])


if __name__ == '__main__':
    print(main(sys.argv[1:]))

#!/usr/bin/env python3
import sys
import random

BOARD_SIZE = 8
ASCII_A = 65


def generate_valid_moves(position):
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
    return 0 <= end_position[0] < BOARD_SIZE and 0 <= end_position[1] < BOARD_SIZE


def generate_tree(start_position, prev_position=None):
    for move in generate_valid_moves(start_position):
        if prev_position is None or prev_position != move:
            yield {'pos': move, 'prev': prev_position}


def get_shortest_path(start, target):
    queue = [(start, [])]

    while queue:
        (current_position, path) = queue.pop(0)

        for next_move in set(generate_valid_moves(current_position)) - set(path):
            if next_move == target:
                return path + [target]
            else:
                queue.append((next_move, path + [next_move]))


def get_chess_notation(position):
    return f'{chr(position[0] + ASCII_A)}{position[1] + 1}'


def parse_chess_notation(position):
    error = f'"{position}" is not valid chess notation'
    try:
        pos = ord(position[0]) - ASCII_A, int(position[1]) - 1
    except ValueError:
        raise ValueError(error)

    if len(position) != 2 or not is_valid_move(pos):
        raise ValueError(error)

    return pos


def print_chess_board(moves):
    for y in reversed(range(BOARD_SIZE)):
        yield "\n"
        for x in range(BOARD_SIZE):
            if x == 0:
                yield f"{y + 1} "

            try:
                ch = moves.index((x, y)) + 1
            except ValueError:
                ch = ' '

            color = 104 if (x + y) % 2 == 0 else 100
            yield f"\033[{color}m {ch} \033[0m"

    yield "\n  "

    for x in range(BOARD_SIZE):
        yield f" {chr(x + ASCII_A)} "


def main(positions):
    if len(positions) != 2:
        raise ValueError('Did not receive two chess notation positions')

    start, end = positions

    print(f"\n{get_chess_notation(start)} to {get_chess_notation(end)}")

    path = get_shortest_path(start, end)

    return ''.join(print_chess_board([start] + [pos for pos in path]))


def generate_random_position():
    return random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)


if __name__ == '__main__':
    number = int(sys.argv[1])

    for _ in range(number):
        print(main([generate_random_position(), generate_random_position()]))

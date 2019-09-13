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

    if not is_valid_move(pos):
        raise ValueError(error)

    return pos


def main(input_string):
    start, end = input_string.split(' ')

    path = get_shortest_path(parse_chess_notation(start), parse_chess_notation(end))

    return ' '.join([get_chess_notation(pos) for pos in path])

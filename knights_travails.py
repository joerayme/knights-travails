BOARD_SIZE = 8


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
    return 0 < end_position[0] < BOARD_SIZE and 0 < end_position[1] < BOARD_SIZE


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

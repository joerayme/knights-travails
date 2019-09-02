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

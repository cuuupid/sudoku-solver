import numpy as np
from helper import *
from multiprocessing.dummy import Pool
from time import sleep

tp = Pool(4)
_ = 0
board = np.zeros((9, 9))
makeBoard(board)
assert board.shape == (9, 9)

def solve(board, moves=[]):
    for r in range(9):
        for c in range(9):
            if board[r, c] == _:
                box = np.reshape(board[(r // 3 * 3):(r // 3 * 3)+3,
                            (c // 3 * 3):(c // 3 * 3)+3], -1)
                col = np.reshape(board[:, c], -1)
                row = board[r]
                unknown = intersection(unknowns(row), unknowns(col), unknowns(box))
                if len(unknown) is 1:
                    board[r, c] = unknown[0]
                    moves.append((r, c, unknown[0]))
                elif len(unknown) is 0:
                    return None, None
                else:
                    for choice in unknown:
                        old = board.copy()
                        board[r, c] = choice
                        board, _moves = solve(board, moves + [(r, c, choice)])
                        if board is not None and complete(board):
                            return board, _moves
                        board = old
                    return None, None
    return board, moves

show(board)
original = board.copy()
board, moves = solve(board)
assert valid(board)
for r, c, n in moves:
    original[r, c] = n
    show(original, clear=True)
    sleep(0.2)
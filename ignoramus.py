import numpy as np
from helper import *
from multiprocessing.dummy import Pool
from time import time as t
import tqdm
import random

tp = Pool(4)
_ = 0
board = [
   [6, 8, 4, _, _, _, _, _, _],
   [_, _, 3, _, _, _, 4, _, _],
   [_, 7, _, _, 5, 4, _, _, _],
   [9, 3, _, 5, _, 7, 6, _, 2],
   [_, _, 2, _, 6, _, 7, _, _],
   [7, _, 5, 8, _, 1, _, 4, 3],
   [_, _, _, 4, 9, _, _, 2, _],
   [_, _, 6, _, _, _, 5, _, _],
   [_, _, _, _, _, _, 8, 3, _]
]
board = np.array(board)
assert board.shape == (9, 9)

def _solve(board, guess=9):
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
                elif len(unknown) is 0:
                    return None
                elif guess > 1:
                    choices = []
                    while len(choices) < guess:
                        _choice = random.choice(unknown)
                        unknown.remove(_choice)
                        choices.append(_choice)
                    for choice in choices:
                        old = board.copy()
                        board[r, c] = choice
                        _guess = 1
                        board = _solve(board, guess=_guess)
                        while board is not None and not complete(board):
                            _guess += 1
                            board = _solve(board, guess=_guess)
                        if board is not None and complete(board):
                            return board
                        board = old
                    return None
    return board

def solve(board):
    g = 1
    backup = board.copy()
    board = _solve(board, guess=g)
    while not complete(board):
        g += 1
        last = board.copy()
        board = _solve(board, guess=g)
        if board is None:
            board = last
    return board

show(board)
original = board.copy()
ts = 0
prec = 200
for i in tqdm.tqdm(range(prec)):
    t0 = t()
    board = solve(original.copy())
    assert(valid(board))
    ts += t() - t0
ts /= prec
show(board)
print(ts)
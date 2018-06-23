import numpy as np
import os

unknowns = lambda xs: [_ for _ in range(1, 10) if _ not in xs]
knowns = lambda xs: [_ for _ in range(1, 10) if _ in xs]

def intersection(*args):
    xs = list(range(1, 10))
    for i, arg in enumerate(args):
        _xs = list(xs)
        for x in _xs:
            if x not in arg:
                xs.remove(x)
    return xs

def union(*args):
    xs = []
    for arg in args:
        xs += arg
    return xs

def show(board, clear=False):
    if clear: os.system('clear')
    b = board.copy()
    b[(b < 1) | (b > 9)] = 0
    print(str(b).replace('0', ' '))

def makeBoard(board):
    print("Type in the board, separating cells with spaces and rows with enters.")
    for r in range(9):
        board[r] = [int(i) for i in input().split(' ')]

complete = lambda board: len(board[(board < 1) | (board > 9)]) == 0
def valid(board):
    try:
        for r in range(9):
            assert len(set(board[r])) == 9
        for c in range(9):
            assert len(set(board[:, c])) == 9
        for r in range(3):
            for c in range(3):
                assert len(set(np.reshape(board[(r * 3):(r * 3)+3,
                            (c * 3):(c * 3)+3], -1))) == 9
    except AssertionError as _:
        return False
    return True
from tic_tac_toe import TicTacToe
import numpy as np

def test_victory_condition_rows():
    game = TicTacToe(None)

    assert game.evaluate() is None

    game.board[0] = 1
    assert game.evaluate() == 1

    game.board[0] = -1
    assert game.evaluate() == -1


def test_victory_condition_columns():
    game = TicTacToe(None)

    assert game.evaluate() is None

    game.board[:,0] = 1
    assert game.evaluate() == 1

    game.board[:,0] = -1
    assert game.evaluate() == -1

def test_victory_condition_diags():
    game = TicTacToe(None)

    assert game.evaluate() is None

    rows = [0,1,2]
    columns = [2,1,0]

    game.board[rows, rows] = 1
    assert game.evaluate() == 1

    game.board[rows, columns] = -1
    assert game.evaluate() == -1


def test_draw_detected():
    game = TicTacToe(None)
    game.board = np.array([[ 1, -1, -1],
                           [-1,  1,  1],
                           [ 1, -1, -1],])

    assert game.evaluate() == 0

    game.board = np.array([[ 1, -1, 1],
                           [-1,  0, 1],
                           [ 1, -1,-1], ])

    assert game.evaluate() is None

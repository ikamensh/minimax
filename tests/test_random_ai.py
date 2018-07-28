from tic_tac_toe import TicTacToe
from random_ai import RandomAI


def test_makes_valid_turns():
    game = TicTacToe(RandomAI())

    row, column = game.o_ai.decide_turn(game.board)

    assert 0 <= row <= 2
    assert 0 <= column <= 2
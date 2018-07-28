from tic_tac_toe import TicTacToe
from minimax_ai import MinimaxAI


game = TicTacToe()
ai = MinimaxAI(game, True)

row, column = ai.decide_turn()

print(row, column)
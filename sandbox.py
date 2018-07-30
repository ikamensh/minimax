# from tic_tac_toe import TicTacToe
# from minimax_ai import MinimaxAI
#
#
# game = TicTacToe()
# ai = MinimaxAI(game)
#
# row, column = ai.decide_turn()
#
# print(row, column)

board = ( (1, 0, 1),
          (-1, -1, 1),
          (1, 0, -1))


# @staticmethod
def _evaluate(board):


    sums = []
    sums += [sum(board[row]) for row in range(3)]
    sums += [sum([board[i][column] for i in range(3)]) for column in range(3)]
    sum_main_diag = sum([board[i][i] for i in range(3)])
    sum_opp_diag = sum([board[i][2-i] for i in range(3)])

    sums.append(sum_main_diag)
    sums.append(sum_opp_diag)

    if 3 in sums:
        return 1
    elif -3 in sums:
        return -1
    else:
        n_empty = sum([1 for row in range(3) for cell in board[row] if cell == 0])
        if n_empty == 0:
            return 0
        else:
            return None


print(_evaluate(board))
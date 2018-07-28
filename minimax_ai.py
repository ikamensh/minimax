from math import inf as infinity
from tic_tac_toe import TicTacToe
from random_ai import RandomAI

def game_over(state):
    return TicTacToe.evaluate(state) is not None

def empty_cells(state):
    results = []
    for row in range(3):
        for column in range(3):
            if state[row,column] == 0:
                results.append( (row, column) )

    return results

def minimax(state, depth, X_turn):

    if X_turn:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = TicTacToe.evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x,y] = 1 if X_turn else -1
        score = minimax(state, depth - 1, not X_turn)
        state[x,y] = 0
        score[0], score[1] = x, y

        if X_turn:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


class MinimaxAI:

    def __init__(self, game):
        self.game = game
        self.random_ai = RandomAI(game)

    def decide_turn(self):
        turns_possible = empty_cells(self.game.board)
        if len(turns_possible) == 1:
            row, column = turns_possible[0]
        if len(turns_possible) == 9:
            row, column = self.random_ai.decide_turn()
        else:
            chosen_node = minimax(self.game.board, 10, self.game.x_next)
            row, column, _ = chosen_node
        return row, column










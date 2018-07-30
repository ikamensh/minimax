import numpy as np
import random
from functools import lru_cache
from gym.core import Env
from minimax_ai import MinimaxAI

from gym import spaces



class TicTacToe(Env):

    def __init__(self):
        self.board = np.zeros([3,3], dtype=np.int8)
        self.x_next = True if random.random() > 0.5 else False
        self.o_ai = MinimaxAI(self)
        self.action_space = spaces.Discrete(9)
        self.observation_space = spaces.Box(low=-1, high=1, dtype=np.int8, shape=(3,3))


    def reset(self):
        self.board = np.zeros([3, 3])
        self.x_next = True if random.random() > 0.5 else False
        if not self.x_next:
            row, column = self.o_ai.decide_turn()
            assert self.try_make_turn(row, column)

        return self.board

    def step(self, action):
        """
        :param action: a discrete action from 0 to 8. Cells are enumerated from left to right,
        with columns continuing from top to bottom, like below:

         0 | 1 | 2
        -  + - + -
         3 | 4 | 5
        -  + - + -
         6 | 7 | 8

        :return: observation, reward, done?, None (info)
        """
        assert self.x_next
        row = action // 3
        column = action % 3
        info = {}

        if self.try_make_turn(row,column):
            result = self.evaluate(self.board)
            if result is None:
                row, column = self.o_ai.decide_turn()
                assert self.try_make_turn(row, column)
                result = self.evaluate(self.board)

            if result is None:
                return self.board, 0, False, {}
            else:
                return self.board, result, True, {}

        else:
            return self.board, -0.5, False, {}

    # def render(self, mode="Human"):
    #     shapes = {-1: 'o', 0: ' ', 1: 'x'}
    #     print(f"{shapes[self.board[0,0]]}|{shapes[self.board[0,1]]}|{shapes[self.board[0,2]]}")
    #     print('-+-+-')
    #     print(f"{shapes[self.board[1,0]]}|{shapes[self.board[1,1]]}|{shapes[self.board[1,2]]}")
    #     print('-+-+-')
    #     print(f"{shapes[self.board[2,0]]}|{shapes[self.board[2,1]]}|{shapes[self.board[2,2]]}")


    def try_make_turn(self, row, column):

        if self.board[row,column] == 0:

            self.board[row, column] = 1 if self.x_next else -1
            self.x_next = not self.x_next
            return True

        else:
            return False

    @staticmethod
    def evaluate(board):
        board_as_tuple = tuple(tuple(board[row]) for row in range(3))
        return TicTacToe._evaluate(board_as_tuple)



    def loop(self):
        while self.evaluate(self.board) is None:
            ai = self.x_ai if self.x_next else self.o_ai
            row, column = ai.decide_turn()
            assert self.try_make_turn(row, column)
        return self.evaluate(self.board)


    @property
    def board_as_tuple(self):
        return tuple(tuple(self.board[row]) for row in range(3))


    @staticmethod
    @lru_cache(maxsize=2**16)
    def _evaluate(board):

        sums = []
        # we collect totals of all row, columns and diagonals. Any of those must have a value of
        # either 3 or -3 if there are x x x or o o o in this sequence.
        sums += [sum(board[row]) for row in range(3)]
        sums += [sum([board[i][column] for i in range(3)]) for column in range(3)]
        sum_main_diag = sum([board[i][i] for i in range(3)])
        sum_opp_diag = sum([board[i][2 - i] for i in range(3)])

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














































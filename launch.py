from tic_tac_toe import TicTacToe
from random_ai import RandomAI
from minimax_ai import MinimaxAI
import time


counters = {-1:0, 0:0, 1:0}


n_games = int(1e1)

t = time.time()

for i in range(n_games):
    ttt = TicTacToe()
    x_ai = MinimaxAI(ttt)
    o_ai = RandomAI(ttt)
    ttt.x_ai = o_ai
    ttt.o_ai = x_ai

    result = ttt.loop()
    counters[result] += 1

print(time.time() - t)



print(f"stats: out of {n_games} games, x has won {counters[1]} times, o - {counters[-1]} times, and there were "
      f"{counters[0]} draws.")


from tic_tac_toe import TicTacToe
from random_ai import RandomAI
from minimax_ai import MinimaxAI

counters = {-1:0, 0:0, 1:0}
n_games = int(1e2)

def run_trials():
    for i in range(n_games):
        ttt = TicTacToe()
        x_ai = MinimaxAI(ttt)
        o_ai = RandomAI(ttt)
        ttt.o_ai = o_ai
        ttt.x_ai = x_ai

        result = ttt.loop()
        counters[result] += 1

from cProfile import Profile

profiler = Profile()
profiler.runcall(run_trials)

profiler.print_stats('cumulative')


print(f"stats: out of {n_games} games, x has won {counters[1]} times, o - {counters[-1]} times, and there were "
      f"{counters[0]} draws.")


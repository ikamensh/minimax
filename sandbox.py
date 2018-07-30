from tic_tac_toe import TicTacToe
import random

env = TicTacToe()

print(env.reset())
done = False
while not done:
    obs, rew, done, _ = env.step(env.action_space.sample())
    print("-"*30)
    env.render()




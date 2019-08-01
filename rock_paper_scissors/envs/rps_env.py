import gym
import numpy as np


class RPSEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    result = 'DRAW'
    tags = ["ROCK", "PAPER", "SCISSORS"]
    # looses to map
    loses_to = {
        "0": 1,  # rock loses to paper
        "1": 2,  # paper loses to scissor
        "2": 0  # scissor loses to rock
    }

    def __init__(self):
        self.result = 'DRAW'
        # our states can be either "ROCK, PAPER or SCISSORS"
        self.state_space = 3
        # three actions by our player
        self.action_space = 3

    # returns either a WIN, LOSE or a DRAW to indicate the same.
    def get_result(self, player_move, bot_move):
        if bot_move == player_move:
            result = 'DRAW'
        elif self.loses_to[str(bot_move)] == player_move:
            result = 'LOSE'
        else:
            result = 'WIN'
        return result

    def get_reward(self, state, action):
        self.result = self.get_result(state, action)
        if self.result == 'WIN':
            reward = 5
        elif self.result == 'LOSE':
            reward = -2
        else:
            # Draw case
            reward = 4
        return reward

    """
    Returns isDone and the reward for the taken 'action'
    """
    def step(self, action):
        reward = self.get_reward(self.state, action)
        return True, reward, self.result

    def reset(self):
        self.state = np.random.randint(0, self.action_space)
        return self.state

    def render(self, mode='human'):
        pass

    def close(self):
        pass
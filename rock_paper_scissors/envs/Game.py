import numpy as np
import gym

env = gym.make('rock_paper_scissors:rps-v0')


class Game(object):
    q_table = np.random.uniform(low=0, high=2, size=(env.state_space, env.action_space))
    total_reward, reward = 0, 0
    avg_rewards_list = []
    avg_reward = 0

    def __init__(self, episodes=100, alpha=0.5, gamma=0.5, epsilon=0.2, min_eps=0):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.min_eps = min_eps
        self.episodes = episodes
        # Calculate episodic reduction in epsilon
        self.reduction = (epsilon - min_eps) / episodes

    # either explore or exploit, any which ways return the next action
    def bot_move(self, player_move):
        # Determine next action - epsilon greedy strategy
        if np.random.random() < 1 - self.epsilon:
            action = np.argmax(self.q_table[player_move])
        else:
            action = np.random.randint(0, env.action_space)
        # Decay epsilon
        if self.epsilon > self.min_eps:
            self.epsilon -= self.reduction
        return action

    # update q_table
    def update_experience(self, state, action, reward):
        delta = self.alpha * (reward + self.gamma * np.max(self.q_table[action]) - self.q_table[state, action])
        self.q_table[state, action] += delta

    def get_avg_rewards(self):
        return self.avg_rewards_list

    def play(self):
        for i in range(1, self.episodes + 1):
            player_move = env.reset()
            bot_move = self.bot_move(player_move)
            is_done, reward, result = env.step(bot_move)
            self.total_reward += reward
            self.update_experience(player_move, bot_move, reward)
            print("episode: {0} player: {1}, bot: {2}, reward: {3}, result: {4}".format(i, player_move, bot_move,
                                                                                        self.total_reward, result))


game = Game(episodes=200)
game.play()

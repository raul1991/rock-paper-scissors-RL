from gym.envs.registration import register

register(
    id='rps-v0',
    entry_point='rock_paper_scissors.envs:RPSEnv',
)

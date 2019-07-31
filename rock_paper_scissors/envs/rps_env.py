import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding

class RPSEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
      print("Initialized")


  def step(self, action):
      print("stepping...")


  def reset(self):
      print("resetting env")


  def render(self, mode='human'):
      print("Rendering env")


  def close(self):
      print("Closing env")

import gym
import numpy as np


class Agent(object):
    """Agent that acts randomly."""
    def __init__(self):
        self.action_space = gym.spaces.Box(low=0, high=1, shape=(22,), dtype=np.float32)

    def act(self, observation):
        return self.action_space.sample()
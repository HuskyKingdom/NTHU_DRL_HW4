import gym


class Agent(object):
    """Agent that acts randomly."""
    def __init__(self):
        self.action_space = gym.spaces.Discrete(12)
        pass

    def act(self, observation):
        return self.action_space.sample()

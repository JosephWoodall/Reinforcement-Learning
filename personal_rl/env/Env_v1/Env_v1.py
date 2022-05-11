import gym 
from gym import error, spaces, utils 

class Env_v1(gym.Env):
    
    """
    The state is always kept in the scope of the function that uses it, and it's implied that if the environment takes a step (via the step function), then 
    it moves from state 0 to 1, and then the game immediately ends. So there is no need to track the state within the object in the example below, 
    but generally, you want to have a self.state variable.
    """

    def __init__(self):
        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Discrete(2)

    def step(self, action):
        state = 1

        if action == 2:
            reward = 1
        else:
            reward = -1

        done = True

        info = {}

        return state, reward, done, info 
    
    def reset(self):
        state = 0 

        return state
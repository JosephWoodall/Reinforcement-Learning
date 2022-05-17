from importlib.metadata import entry_points
from gym.envs.registration import register

register(
    id = 'factory-v1',
    entry_points = 'personal_rl.env:Factory-v1',
    max_episode_steps = 100
)
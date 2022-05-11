from importlib.metadata import entry_points
from gym.envs.registration import register

register(
    id = 'env-v1',
    entry_points = 'personal_rl.env:Env_v1',
)
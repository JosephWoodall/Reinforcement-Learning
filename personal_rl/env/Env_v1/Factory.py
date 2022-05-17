import gym 
from gym import error, spaces, utils 
import numpy as np

class Factory(gym.Env):
    metadata = {"render_modes":["human", "rbg_array"], "render_fps": 4}

    """
    The state is always kept in the scope of the function that uses it, and it's implied that if the environment takes a step (via the step function), then 
    it moves from state 0 to 1, and then the game immediately ends. So there is no need to track the state within the object in the example below, 
    but generally, you want to have a self.state variable.
    """

    def __init__(self):

        self.size = 5
        self.window_size = 512

        """
        There are 5 possible cardinal directions any agent can take: 
            Up, Down, Left, Right, Diagonal
        """
        self.action_space = gym.spaces.Discrete(5)

        self.observation_space = spaces.Dict(
            "agent": spaces.Box(0, size - 1, shape = (2,), dtype = int), 
            "target": spaces.Box(0, size - 1, shape = (2,) dtype = int)
        )

        import pygame # Importing here to avoid pygame dependency with no render
        pygame.init()
        pygame.display.init()
        self.window = pygame.display.set_mode((self.window_size, self.window_size))
        self.clock = pygame.time.Clock()
    
    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}
    
    def _get_info(self):
        return {"distance": np.linalg.norm(self._agent_location - self._target_location, ord = 1)}

    def step(self, action):
        direction = self._action_to_direction[action]

        self._agent_location = np.clip(
            self._agent_location + direction, 0, self.size - 1
        )

        done = np.array_equal(self._agent_location, self._target_location)
        reward = 1 if done else 0
        observation = self._get_obs()
        info = self._get_info()

        self.renderer.render_step()

        return observation, reward, done, info 
    
    def reset(self, seed = None, return_info = False, options = None):
        super().reset(seed = seed)

        self._agent_location = self.np_random.integers(0, self.size, size = 2)

        self._target_location = self._agent_location
        while np.array_equal(self._target_location, self._agent_location):
            self._target_location = self.np_random.integers(0, self.size, size = 2)
        
        self.renderer.reset()
        self.renderer.render_step()

        observation = self._get_obs()
        info = self._get_info()

        return (observation, info) if return_info else observation

    def render(self):
        return self.renderer.get_renders()
    
    def _render_frame(self, mode: str):
        import pygame 

        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((255, 255, 255))
        pix_square_size = (
            self.window_size / self.size
        )

        pygame.draw.rect(
            canvas, 
            (255, 0, 0), 
            pygame.Rect( 
                pix_square_size * self._target_location, 
                (pix_square_size, pix_square_size),
            ),
        )
        
        pygame.draw.circle(
            canvas, 
            (0, 0, 255), 
            (self._agent_location + 0.5) * pix_square_size, 
            pix_square_size / 3,
        )

        for x in range(self.size + 1):
            pygame.draw.line(
                canvas, 
                0, 
                (0, pix_square_size * x), 
                (self.window_size, pix_square_size * x), 
                width = 3,
            )
            pygame.draw.line(
                canvas, 
                0, 
                (pix_square_size * x, 0), 
                (pix_square_size * x, self.window_size),
                width = 3
            )
        if mode == "human":
            assert self.window is not None
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()

            self.clock.tick(self.metadata["render_fps"])
        else:
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes = (1, 0, 2)
            )

    def close(self):
        if self.window is not None:
            import pygame 
            pygame.display.quit()
            pygame.quit()
    
    




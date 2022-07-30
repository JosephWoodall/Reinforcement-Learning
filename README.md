# Reinforcement Learning!
Reinforcement Learning is the subfield of machine learning concerned with decision making and motor control. It studies how an agent can learn how to achieve goals in a complex, uncertain environment. It's exciting for many reasons, but here are two: 
- Reinforcement Learning is very general, and is all encompassing to problems that involve making a sequence of decisions. For example, controlling a robot's motors so that it's able to run and jump, making business decisions like pricing and inventory management, or playing video games and board games. It can also be applied to supervised machine learning problems with sequential or structured outputs. 
- Reinforcement Learning algorithms have started to achieve good results in many difficult environments. Reinforcement Learning has a long history, but until recent advances in deep learning, it requred lots of problem-specific engineering. DeepMind's Atari results, BRETT from Pieter Abbeel's group, and AlphaGo all used deep Reinforcement Learning which did not make too many assumptions about their environment, and thus can be applied to other settings; making it great for generalzing about new situations. 

BUT, Reinforcement Learning has two factors that are slowing it down (which have been solved by OpenAI's Gym Library):
- The need for better benchmarks. In supervised learning, progress has been driven by large labeled datasets like ImageNet. In Reinforcement Learning, the closest equivalent would be a large and diverse collection of environments. However, the existing open-source collections of Reinforcement Learning environments dont have enough variety, and they are often difficult to set up and use. 
- Lack of standardization of environments used in publications. Subtle differences in the problem definition, such as the reward function or the set of actions, can drastically alter a task’s difficulty. This issue makes it difficult to reproduce published research and compare results from different papers.

You may find a *very* high level, video explanation of reinforcement learning on my youtube channel: https://www.youtube.com/watch?v=dNoeaEdPEy4


## Environments
There are many environments that are ready to use out of the box, which can be found below: 

#### OpenAI Gym — Atari games, Classic Control, Robotics and more
- This is a wonderful collection of several environments and is heavily used by the community. You can find Atari games, classic control problems (e.g. Cart-Pole), algorithms (e.g. teach the agent how to copy text), MuJoCo for continous control tasks (e.g. teach a spider how to move in a physics environment), robotics (i.e. teach a task to a robot arm) and text games (e.g. blackjack).
License: MIT License

#### Gym Trading — Trading
- If you want give a try to RL for trading Gym Trading is a very good option. This is another environment implemented by OpenAI and provides daily observations based on real market data pulled from Quandl on, by default, the SPY etf.
License: MIT License

#### TensorTrade — Trading
- If you’re looking for something more advanced and highly customizable, TensorTrade has got your back. This framework focuses on being highly composable and extensible, to allow the system to scale from simple trading strategies on a single CPU to complex investment strategies run on a distribution of HPC machines.
License: Apache License 2.0

#### VIZDoom — Games [Doom]
- This brings so many memories. With VIZDoom you can teach a RL agent to play the well-known and beloved Doom. VIZDoom has been used in many research papers, it’s well documented and well maintained.
License: MIT License

#### OpenSpiel — Games
- A collection of environments and algorithms developed by DeepMind, for research in general reinforcement learning and search/planning in games. OpenSpiel also includes tools to analyze learning dynamics and other common evaluation metrics. It includes several games such as Backgammon, Chess and Go.
License: Apache License 2.0

#### ns3-gym — Networking
- The network simulator ns–3 is the de-facto standard for academic and industry studies in the areas of networking protocols and communication technologies. ns3-gym is a framework that integrates both OpenAI Gym and ns-3 and provides multiple networking problems such as traffic control, in which you can test your RL algorithms.
License: GNU General Public License v2.0

#### RecoGym — Recommender Systems
- There have been many works lately that apply RL to recommender systems, usually as multi-armed bandit problem. RecoGym is an RL environment for recommendations for e-commerce advertising.
License: Apache License 2.0

#### OpenSim-RL — Biomechanics
- Design artificial intelligent controllers for the human body to accomplish diverse locomotion tasks. This library has been implemented by Stanford and annual competitions are held, in which RL practitioners can put their skills up to a test against each other. Three environments are currently implemented: a simplified arm movement, learn to run and leg prosthetics.
License: MIT License

#### Textworld — Text-based games
- If you haven’t found the right environment for you yet, you can also easily create a RL environment to match your needs using Textworld. Textworld is not an environment per se, but a generator of environments instead. It’s implemented and maintained by Microsoft and the community, well documented and easy to use.
License: MIT License



### Making a Custom Environment using Gym as a template
- The enviornment class needs to be inherited from gym.env. 
- In the __init__, you'll need to create two variables with fixed names and types. You'll need an action space and observation space (self.action_space, and self.observation_space). These two need to be of Gym's class, space. There are two fundamental types in space: discrete, which is one dimension; and box, which is n-dimension. 
- The reset function from Gym returns a value that's within the self.observation_space. This function is responsible for restarting the environment (at the beginning of a game, for example). The variable that is going to keep track of the current state of the environment is a variable called state. If you use a discrete space, then your state value needs to be an integer; if you use a box space, then you can make your state value a numpy array.
- The step function from Gym takes one parameter, an action value, which is usually called action, that is within the self.action_space. Your action value can be an integer or a numpy array. The step function is the response function, which the agent provides the action they want to take, and the environment returns the state it brought them to. The return value is a 4-tuple, and returns in the following order: 
    - state, the same type of variable as the return of the reset function of self.observation_space
    - reward, a number that informs the agent about the immediate consequences of the action
    - done, a boolean value that is True if the environment reached an endpoint, and should be reset as consequence, or False, if the environment should not be reset as consequence
    - info, a dictionary that can be used during bug fixing, and can be empty. 
- You can have as many helping functions within the environment class as you'd like as long as they don't use the reserved names from above.
- The below functions are not required, but encouraged, when developing a custom environment: 
    - """ metadata = {'render.modes' : ['human']} """, this function defines possible types for the render function
    - render function: this function comes in handy when youre debugging, and is used to convert the state variable to something more human readable.
    - close function: this function comes in handy when additional cleanup is closed. 
    - seed function: this is used when you want to have reproducibility in an environment that uses random number generators
- Stable Baselines is a good template to use as well, and the docs can be found here: https://stable-baselines.readthedocs.io/en/master/guide/custom_env.html

You can find an example of a custom environment I am working on in the personal_rl directory of this repo!

## Interesting Research Articles

#### Assessing Human Interaction in Virtual Reality With Continually Learning Prediction Agents Based on Reinforcement Learning Algorithms: A Pilot Study
https://arxiv.org/pdf/2112.07774.pdf

#### Deep Reinforcement Learning for Automated Stock Trading: An Ensemble Strategy
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690996
https://github.com/AI4Finance-Foundation/Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020
https://github.com/AI4Finance-Foundation/FinRL
https://github.com/AI4Finance-Foundation/ElegantRL


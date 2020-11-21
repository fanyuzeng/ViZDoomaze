# ViZDoomaze
ViZdoomaze includes empty mazes and mazes with obstacles, based on the indoor plans of undecorated departments and build them in ViZDoom, which is a clone of the well-known classic game Doom implemented for research purposes. 


# Vizdoomaze
Vizdoomaze includes empty mazes and mazes with obstacles, based on the indoor plans of undecorated departments and build them in ViZDoom, which is a clone of the well-known classic game Doom implemented for research purposes. These mazes have complicated structures on various scales. In Vizdoomaze, the color of the ceiling and the floor is earth-yellow, while the gray wall resembles brickwork. We set a red tower as a target object, which is randomly positioned in the maze at each training episode. In addition, some green towers representing obstacles randomly are placed in the mazes with obstacles. The agent’s objective in navigation tasks is to find the red tower, and the agent has 3 available actions: turn left, turn right and move forward. If the agent reaches the correct target object, it obtains a positive reward (+1.0), whereas if it does not reach the target object, it obtains a negative living reward (-0.0001). In the mazes with obstacles, the agent obtains a negative reward(-0.01) when it hits an obstacle.

# Installation
Download Vizdoomaze and unzip it, then install it as follows:
cd vizdoomgymmaze pip install -e .

# Test
Run the following code to test whether you successfully install Vizdoomaze.
import gym import vizdoomaze env = gym.make('VizdoomSelfMaze0-v0') episodes=10 for i in range(episodes)： print("Episodes #" + str(i+1)) observation = env.reset() for step in range(100): env.render() action = env.action_space.sample() observation, reward, done, info = env.step(action) if done: print("Episode finished after {} timesteps".format(step+1)) break env.close()

# Environments
VizdoomBasic-v0 VizdoomCorridor-v0 VizdoomDefendCenter-v0 VizdoomDefendLine-v0 VizdoomHealthGathering-v0 VizdoomMyWayHome-v0 VizdoomPredictPosition-v0 VizdoomTakeCover-v0 VizdoomDeathmatch-v0 VizdoomHealthGatheringSupreme-v0 VizdoomSelfMaze0-v0 VizdoomSelfMaze1-v0 VizdoomSelfMaze2-v0 VizdoomSelfMaze3-v0 VizdoomSelfMaze4-v0 VizdoomSelfMaze5-v0 VizdoomSelfMaze5-v0

# Indoor mazes are as follows:
VizdoomMazeOne1-v0 VizdoomMazeTwo5-v0 VizdoomMazeThree8-v0 ...
If you want to use indoor mazes, the environment name should like this: "VizdoomMaze[One/Two/Three/Four][1~20]-v0"
For example,
env = gym.make('VizdoomMazeOne1-v0')
"One" means apartment has one bedroom, while "Two" means apartment has two bedroom.
With the bedrooms increasing, the structure of apartment become more and more complex, but the whole size of four style mazes is the same.


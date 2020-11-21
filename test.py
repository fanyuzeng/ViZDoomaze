import gym
import vizdoomaze
# vizdoomazeOne19m, VizdoomSelfMaze1m
env = gym.make('VizdoomSelfMaze0m-v0')
episodes=10
for i in range(episodes):
    print("Episodes #" + str(i+1))
    observation = env.reset()
    for step in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(step+1))
            break
env.close()


# Vizdoomaze
Vizdoomaze is a series of mazes based on [ViZDoom](https://github.com/mwydmuch/ViZDoom). It includes empty mazes and mazes with obstacles, based on the indoor plans of undecorated departments. These mazes have complicated structures on various scales. In Vizdoomaze, the color of the ceiling and the floor is earth-yellow, while the gray wall resembles brickwork. We set a red tower as a target object, which is randomly positioned in the maze at each training episode. In addition, some green towers representing obstacles randomly are placed in the mazes with obstacles. 

The agent’s objective in navigation tasks is to find the red tower, and the agent has 3 available actions: turn left, turn right and move forward. If the agent reaches the correct target object, it obtains a positive reward (+1.0), whereas if it does not reach the target object, it obtains a negative living reward (-0.0001). In the mazes with obstacles, the agent obtains a negative reward(-0.01) when it hits an obstacle.

Requirements:
- [ViZDoom](https://github.com/mwydmuch/ViZDoom)


# Installation
    git clone https://github.com/fanyuzeng/ViZDoomaze.git  
    cd ViZDoomaze   
    pip install -e .    


# Example Usage
```python
import gym        
import vizdoomaze         
env = gym.make('vizdoomazeOne1-v0')      
episodes=10     
for i in range(episodes)：     
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
```


# Mazes


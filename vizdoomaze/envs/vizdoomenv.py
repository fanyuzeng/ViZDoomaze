import gym
from gym import spaces
from vizdoom import *
import numpy as np
import os
from gym.envs.classic_control import rendering
import cv2

CONFIGS = [['basic.cfg', 3],                # 0
           ['deadly_corridor.cfg', 7],      # 1
           ['defend_the_center.cfg', 3],    # 2
           ['defend_the_line.cfg', 3],      # 3
           ['health_gathering.cfg', 3],     # 4
           ['my_way_home.cfg', 5],          # 5
           ['predict_position.cfg', 3],     # 6
           ['take_cover.cfg', 2],           # 7
           ['deathmatch.cfg', 20],          # 8
           ['health_gathering_supreme.cfg', 3], # 9
           ['selfmaze0.wad', 3],            # 10
           ['selfmaze1.wad', 3],            # 11
           ['selfmaze2.wad', 3],            # 12
           ['selfmaze3.wad', 3],            # 13
           ['one/one_1.wad', 3],            # 14
           ['one/one_2.wad', 3],            # 15
           ['one/one_3.wad', 3],            # 16
           ['one/one_4.wad', 3],            # 17
           ['one/one_5.wad', 3],            # 18
           ['one/one_6.wad', 3],            # 19
           ['one/one_7.wad', 3],            # 20
           ['one/one_8.wad', 3],            # 21
           ['one/one_9.wad', 3],            # 22
           ['one/one_10.wad', 3],           # 23
           ['one/one_11.wad', 3],           # 24
           ['one/one_12.wad', 3],           # 25
           ['one/one_13.wad', 3],           # 26
           ['one/one_14.wad', 3],           # 27
           ['one/one_15.wad', 3],           # 28
           ['one/one_16.wad', 3],           # 29
           ['one/one_17.wad', 3],           # 30
           ['one/one_18.wad', 3],           # 31
           ['one/one_19.wad', 3],           # 32
           ['one/one_20.wad', 3],           # 33
           ['two/two_1.wad', 3],            # 34
           ['two/two_2.wad', 3],            # 35
           ['two/two_3.wad', 3],            # 36
           ['two/two_4.wad', 3],            # 37
           ['two/two_5.wad', 3],            # 38
           ['two/two_6.wad', 3],            # 39
           ['two/two_7.wad', 3],            # 40
           ['two/two_8.wad', 3],            # 41
           ['two/two_9.wad', 3],            # 42
           ['two/two_10.wad', 3],           # 43
           ['two/two_11.wad', 3],           # 44
           ['two/two_12.wad', 3],           # 45
           ['two/two_13.wad', 3],           # 46
           ['two/two_14.wad', 3],           # 47
           ['two/two_15.wad', 3],           # 48
           ['two/two_16.wad', 3],           # 49
           ['two/two_17.wad', 3],           # 50
           ['two/two_18.wad', 3],           # 51
           ['two/two_19.wad', 3],           # 52
           ['two/two_20.wad', 3],           # 53
           ['three/three_1.wad', 3],        # 54
           ['three/three_2.wad', 3],        # 55
           ['three/three_3.wad', 3],        # 56
           ['three/three_4.wad', 3],        # 57
           ['three/three_5.wad', 3],        # 58
           ['three/three_6.wad', 3],        # 59
           ['three/three_7.wad', 3],        # 60
           ['three/three_8.wad', 3],        # 61
           ['three/three_9.wad', 3],        # 62
           ['three/three_10.wad', 3],       # 63
           ['three/three_11.wad', 3],       # 64
           ['three/three_12.wad', 3],       # 65
           ['three/three_13.wad', 3],       # 66
           ['three/three_14.wad', 3],       # 67
           ['three/three_15.wad', 3],       # 68
           ['three/three_16.wad', 3],       # 69
           ['three/three_17.wad', 3],       # 70
           ['three/three_18.wad', 3],       # 71
           ['three/three_19.wad', 3],       # 72
           ['three/three_20.wad', 3],       # 73
           ['four/four_1.wad', 3],          # 74
           ['four/four_2.wad', 3],          # 75
           ['four/four_3.wad', 3],          # 76
           ['four/four_4.wad', 3],          # 77
           ['four/four_5.wad', 3],          # 78
           ['four/four_6.wad', 3],          # 79
           ['four/four_7.wad', 3],          # 80
           ['four/four_8.wad', 3],          # 81
           ['four/four_9.wad', 3],          # 82
           ['four/four_10.wad', 3],         # 83
           ['four/four_11.wad', 3],         # 84
           ['four/four_12.wad', 3],         # 85
           ['four/four_13.wad', 3],         # 86
           ['four/four_14.wad', 3],         # 87
           ['four/four_15.wad', 3],         # 88
           ['four/four_16.wad', 3],         # 89
           ['four/four_17.wad', 3],         # 90
           ['four/four_18.wad', 3],         # 91
           ['four/four_19.wad', 3],         # 92
           ['four/four_20.wad', 3],         # 93

           ['one/one_10m.wad', 3],          # 94
           ['selfmaze1m.wad', 3],            # 95
           ['selfmaze2m.wad', 3],            # 96

           ['one/one_19m.wad', 3],           # 97
           ['selfmaze0m.wad', 3],            # 98
           ['selfmaze3m.wad', 3],            # 99



          ]

class VizdoomEnv(gym.Env):

    def __init__(self, level):

        # init game
        self.game = DoomGame()
        self.game.set_screen_resolution(ScreenResolution.RES_640X480)
        scenarios_dir = os.path.join(os.path.dirname(__file__), 'scenarios')
        self.game.load_config(os.path.join(scenarios_dir, "default.cfg"))
        self.game.set_doom_map("map00")
        self.game.set_doom_scenario_path(os.path.join(scenarios_dir, CONFIGS[level][0]))
        self.game.set_window_visible(True)
        self.game.init()
        self.state = None

        self.action_space = spaces.Discrete(CONFIGS[level][1])
        self.observation_space = spaces.Box(0, 23, (self.game.get_screen_height(),
                                                     self.game.get_screen_width(),
                                                     self.game.get_screen_channels()),
                                            dtype=np.uint8)
        self.viewer = None

    def step(self, action):
        # convert action to vizdoom action space (one hot)
        act = np.zeros(self.action_space.n)
        act[action] = 1
        act = np.uint8(act)
        act = act.tolist()

        reward = self.game.make_action(act)
        state = self.game.get_state()
        if state.automap_buffer is not None:
            map = np.transpose(state.automap_buffer, (1, 2, 0))
            print(map.shape)
            cv2.imshow('ViZDoom Automap Buffer', map)
        cv2.waitKey(28)
        done = self.game.is_episode_finished()
        if not done:
            observation = np.transpose(state.screen_buffer, (1, 2, 0))
        else:
            observation = np.uint8(np.zeros(self.observation_space.shape))

        info = {'dummy': 0}

        return observation, reward, done, info

    def reset(self):
        self.game.new_episode()
        self.state = self.game.get_state()
        img = self.state.screen_buffer
        return np.transpose(img, (1, 2, 0))

    def render(self, mode='human'):
        try:
            img = self.game.get_state().screen_buffer
            img = np.transpose(img, [1, 2, 0])

            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
        except AttributeError:
            pass

    @staticmethod
    def get_keys_to_action():
        # you can press only one key at a time!
        keys = {(): 2,
                (ord('a'),): 0,
                (ord('d'),): 1,
                (ord('w'),): 3,
                (ord('s'),): 4,
                (ord('q'),): 5,
                (ord('e'),): 6}
        return keys

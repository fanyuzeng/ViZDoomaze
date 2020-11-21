from vizdoomaze.envs.vizdoomenv import VizdoomEnv


class VizdoomSelfMaze1m(VizdoomEnv):

    def __init__(self):
        super(VizdoomSelfMaze1m, self).__init__(95)

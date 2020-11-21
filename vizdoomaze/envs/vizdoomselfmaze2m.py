from vizdoomaze.envs.vizdoomenv import VizdoomEnv


class VizdoomSelfMaze2m(VizdoomEnv):

    def __init__(self):
        super(VizdoomSelfMaze2m, self).__init__(96)

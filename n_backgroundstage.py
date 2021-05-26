from n_staractor import *

class BackgroundStage(MyStage):
    def __init__(self):
        super().__init__()
        for i in range(10):
            self.add_actor(StarActor())
from n_mygameworld import *
from n_menu_menustage import *
import random

class GameStage(MyStage):

    grid_x_count = 20
    grid_y_count = 15
    food_position = {
        'x': random.randint(0, grid_x_count - 1),
        'y': random.randint(0, grid_y_count - 1),
    }

    lastkey = None

    def back(self, pos, btn):
        self.menu.menu_Main()

    def keyuplistener(self, key, mod):
        print("UP")
        self.lastkey = None

    def keydownlistener(self, key, mod, unicode):
        print("DOWN")
        self.lastkey = key

    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.b: MyActor = MyActor("ama.png", pos=(200, 200), anchor=(16, 16))
        self.add_actor(self.b)
        self.set_on_key_down_listener(self.keydownlistener)
        self.set_on_key_up_listener(self.keyuplistener)
        self.m: MyActor = MyActor("kocka.png", pos=(300, 300), anchor=(16, 16))
        self.add_actor(self.m)

    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        if self.lastkey != None:
            if self.lastkey == keys.UP:
                animate(self.m, pos=(self.m.pos[0], self.m.pos[1] - 1000), duration=4)
                self.m.set_rotation(360)
            if self.lastkey == keys.DOWN:
                animate(self.m, pos=(self.m.pos[0], self.m.pos[1] + 1000), duration=4)
                self.m.set_rotation(180)
            if self.lastkey == keys.LEFT:
                animate(self.m, pos=(self.m.pos[0] - 1000, self.m.pos[1]), duration=4)
                self.m.set_rotation(90)
            if self.lastkey == keys.RIGHT:
                animate(self.m, pos=(self.m.pos[0] + 1000, self.m.pos[1]), duration=4)
                self.m.set_rotation(270)
        global food_position






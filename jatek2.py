from n_mygameworld import *
from n_menu_menustage import *

class GameStage(MyStage):

    lastkey = None

    def back(self, pos, btn):
        self.menu.menu_Main()

    def jerrymove(self, pos, btn):
        animate(self.m, pos=pos)

    def keyuplistener(self, key, mod):
        print("UP")
        self.lastkey = None

    def keydownlistener(self, key, mod, unicode):
        print("DOWN")
        self.lastkey = key

    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.m: MyActor = MyActor("kocka.png", pos=(300, 300), anchor=(0, 0))
        self.add_actor(self.m)
        self.set_on_key_down_listener(self.keydownlistener)
        self.set_on_key_up_listener(self.keyuplistener)

    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        if self.lastkey != None:
            if self.lastkey == keys.UP:
                animate(self.m, pos=(self.m.pos[0], self.m.pos[1] - 1000), duration=4)
            if self.lastkey == keys.DOWN:
                animate(self.m, pos=(self.m.pos[0], self.m.pos[1] + 1000), duration=4)
            if self.lastkey == keys.LEFT:
                animate(self.m, pos=(self.m.pos[0] - 1000, self.m.pos[1]), duration=4)
            if self.lastkey == keys.RIGHT:
                animate(self.m, pos=(self.m.pos[0] + 1000, self.m.pos[1]), duration=4)





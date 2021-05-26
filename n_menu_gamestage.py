from n_mygameworld import *
from n_menu_menustage import *

class GameStage(MyStage):

    def back(self, pos, btn):
        self.menu.menu_Main()

    def jerrymove(self, pos, btn):
        animate(self.m, pos=pos)

    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.m: MyActor = MyActor("m_jerry.png", pos=(300, 300), anchor=(0, 0))
        self.m.set_on_mouse_down_listener(self.back)
        self.add_actor(self.m)
        self.menu: Menustage = menu
        self.set_on_mouse_down_listener(self.jerrymove)



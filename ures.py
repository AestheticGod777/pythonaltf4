from n_mygameworld import *
from n_menu_menustage import *

class BlankStage(MyStage):

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()


    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.bruh: MyActor = MyActor("bruhu.png", pos=(200, 100), anchor=(1, 1))
        self.add_actor(self.bruh)
        self.menu = menu
        self.set_on_key_down_listener(self.keydown)

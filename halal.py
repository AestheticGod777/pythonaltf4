from n_mygameworld import *
from n_menu_menustage import *

class BlankStage(MyStage):

    def menu_Main(self, pos=0, btn=0):
        self.onscreenstage = self

    def menu_Game(self, pos=0, btn=0):
        self.onscreenstage = GameStage(self)

    def menu_Blank(self, pos=0, btn=0):
        self.onscreenstage = BlankStage(self)

    def menu_Exit(self, pos=0, btn=0):
        exit()

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()


    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.menu = menu

        menuitem1: MyActor = MyActor("restart.png", pos=(100, 100), anchor=(0, 0))
        self.add_actor(menuitem1)
        menuitem1.set_on_mouse_down_listener(self.menu.menu_Game)

        menuitem2: MyActor = MyActor("menu.png", pos=(100, 250), anchor=(0, 0))
        self.add_actor(menuitem2)
        menuitem2.set_on_mouse_down_listener(self.menu.menu_Main)



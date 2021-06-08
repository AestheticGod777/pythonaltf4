from n_mygameworld import *
import pygame
from halal import *
from jatek2 import *
#from n_menu_main import scr

HEIGHT = 800
WIDTH = 1000

class Menustage(MyStage):

    def menu_Main(self, pos=0, btn=0):
        self.onscreenstage = self
        sounds.menu_sound.play(loops=100)
        sounds.death_sound.stop()
        sounds.game_sound.stop()

    def menu_Game(self, pos=0, btn=0):
        self.onscreenstage = GameStage(self)
        sounds.game_sound.play(loops=100)
        sounds.menu_sound.stop()
        sounds.death_sound.stop()

    def menu_Blank(self, pos=0, btn=0):
        self.onscreenstage = BlankStage(self)
        sounds.death_sound.play(loops=100)
        sounds.menu_sound.stop()
        sounds.game_sound.stop()

    def menu_Exit(self, pos=0, btn=0):
        sounds.death_sound.stop()
        sounds.menu_sound.stop()
        sounds.game_sound.stop()
        sounds.exit_sound.play()
        exit()

    def __init__(self):
        super().__init__()
        sounds.menu_sound.play()
        self.background: MyActor = MyActor(("menubackground.png"), pos=(0, 0), anchor=(0, 0))
        self.add_actor(self.background)
        self.background.set_size(WIDTH, HEIGHT)

        menuitem1: MyActor = MyActor("start.png", pos=(300, 50), anchor=(0, 0))
        self.add_actor(menuitem1)
        menuitem1.set_on_mouse_down_listener(self.menu_Game)

        menuitem2: MyActor = MyActor("exit.png", pos=(325, 200), anchor=(0, 0))
        self.add_actor(menuitem2)
        menuitem2.set_on_mouse_down_listener(self.menu_Exit)

        menuitem3: MyActor = MyActor("ama.png", pos=(900, 700), anchor=(0, 0))
        self.add_actor(menuitem3)
        menuitem3.set_on_mouse_down_listener(self.menu_Blank)

        self.onscreenstage : MyStage = self


    def draw(self):
        if self == self.onscreenstage:
            super(Menustage, self).draw()
        else:
            self.onscreenstage.draw()

    def update(self, deltaTime: float = 0.0166666666666666666666):
        if self == self.onscreenstage:
            super(Menustage, self).update(deltaTime)
        else:
            self.onscreenstage.update(deltaTime)

    def on_mouse_down(self, pos, button):
        sounds.click_sound.play()
        if self == self.onscreenstage:
            super(Menustage, self).on_mouse_down(pos, button)
        else:
            self.onscreenstage.on_mouse_down(pos, button)

    def on_key_down(self, key, mod, unicode):
        if self == self.onscreenstage:
            super().on_key_down(key, mod, unicode)
        else:
            self.onscreenstage.on_key_down(key, mod, unicode)

    def on_key_up(self, key, mod):
        if self == self.onscreenstage:
            super().on_key_up(key, mod)
        else:
            self.onscreenstage.on_key_up(key, mod)



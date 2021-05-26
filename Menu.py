from n_mygameworld import *
from n_menu_menustage import *
from jatek2 import *


def on_key_down(key, mod, unicode):
    menu.on_key_down(key, mod, unicode)


def on_key_up(key, mod):
    menu.on_key_up(key, mod)



def on_mouse_down(pos, button):
    menu.on_mouse_down(pos, button)


def update(dt):
    menu.update(dt)


def draw():
    screen.clear()
    menu.draw()



menu: Menustage = Menustage()


pgzrun.go()
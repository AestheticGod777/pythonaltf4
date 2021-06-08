import pgzrun
from typing import List
import pygame
from pgzero import game
from pgzero.builtins import *
from pgzero import loaders
from pgzero import rect
from pgzero.screen import *
from pgzero.game import PGZeroGame, DISPLAY_FLAGS


class MyBaseActor:
    elapsed_time: float = 0
    _stage: 'MyStage' = 0
    timers: List['MyBaseTimer']

    def __init__(self) -> None:
        self.timers = []

    def add_timer(self, timer: 'MyBaseTimer'):
        if isinstance(timer, MyBaseTimer):
            self.timers.append(timer)
            if timer.base_actor != 0:
                timer.remove()
            timer.base_actor = self
        else:
            print("ERROR: Az objektum példány nem adható hozzá a staghez, mert nem a MyBaseTimer leszármazottja.")

    def remove_timer(self, timer: 'MyBaseTimer'):
        try:
            self.timers.remove(timer)
            timer.base_actor = 0
        except ValueError:
            print("A következő objektum már el lett távolítva korábban: " + str(id(self)))

    def update(self, delta_time: float = 0.0166666666666666666666):
        self.elapsed_time += delta_time
        for obj in self.timers:
            obj.update(delta_time)

    def draw(self):
        pass

    def remove_from_stage(self):
        try:
            self._stage.remove_actor(actor=self)
        except ValueError:
            print("A következő objektum már el lett távolítva korábban: " + str(id(self)))

    def set_stage(self, stage: 'MyStage'):
        self._stage = stage


class MyBaseListeners:
    _on_mouse_down_listener = 0
    _on_mouse_up_listener = 0
    _on_mouse_move_listener = 0
    _on_key_up_listener = 0
    _on_key_down_listener = 0

    def remove_on_mouse_down_listener(self):
        self._on_mouse_down_listener = 0

    def remove_on_mouse_up_listener(self):
        self._on_mouse_up_listener = 0

    def remove_on_mouse_move_listener(self):
        self._on_mouse_move_listener = 0

    def remove_on_key_down_listener(self):
        self._on_key_down_listener = 0

    def remove_on_key_up_listener(self):
        self._on_key_up_listener = 0

    def set_on_key_down_listener(self, func):
        self._on_key_down_listener = func

    def set_on_key_up_listener(self, func):
        self._on_key_up_listener = func

    def set_on_mouse_move_listener(self, func):
        self._on_mouse_move_listener = func

    def set_on_mouse_up_listener(self, func):
        self._on_mouse_up_listener = func

    def set_on_mouse_down_listener(self, func) -> object:
        self._on_mouse_down_listener = func


class MyActor(Actor, MyBaseActor, MyBaseListeners):

    _w: int = -1
    _h: int = -1

    def __init__(self, image, pos=(0, 0), anchor=(0,0), **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        MyBaseActor.__init__(self)
        MyBaseListeners.__init__(self)

    def is_on_stage(self) -> bool:
        return self._stage != 0

    def overlaps_with(self, otheractor: 'MyActor') -> bool:
        return self.colliderect(otheractor)

    def overlaps_point(self, pos) -> bool:
        return self.collidepoint(pos)

    def on_mouse_down(self, pos, button):
        if self.overlaps_point(pos):
            if self._on_mouse_down_listener != 0:
                self._on_mouse_down_listener(pos, button)

    def on_mouse_up(self, pos, button):
        if self.overlaps_point(pos):
            if self._on_mouse_up_listener != 0:
                self._on_mouse_up_listener(pos, button)

    def on_mouse_move(self, pos):
        if self.overlaps_point(pos):
            if self._on_mouse_move_listener != 0:
                self._on_mouse_move_listener(pos)

    def on_key_down(self, key, mod, unicode):
        if self._on_key_down_listener != 0:
            self._on_key_down_listener(key, mod, unicode)

    def on_key_up(self, key, mod):
        if self._on_key_up_listener != 0:
            self._on_key_up_listener(key, mod)

    def set_image(self, image_url:str):
        self.image = image_url

    def set_size(self, width: int, height: int):
        if width == -1 and height == -1:
            if self._w == -1 and self._h == -1:
                self._surf = pygame.transform.scale(self._surf, (self.width, self.height))
            else:
                self._surf = pygame.transform.scale(self._surf, (self._w, self._h))
        else:
            self._surf = pygame.transform.scale(self._surf, (width, height))
            self._w = width
            self._h = height
        self._update_pos()

    def set_rotation(self, degree: int):
        self.angle = degree
        self.set_size(-1, -1)

    def rotate_with(self, degree: int):
        self.set_rotation(self.angle + degree)

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_width(self, width: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(width, int(float(self._h) * (float(width) / float(self._w))))
        else:
            self.set_size(width, self._h)

    def set_height(self, height: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(int(float(self._w) * (float(height) / float(self._h))), height)
        else:
            self.set_size(self._w, height)

    def get_width(self)->int:
        return self._w

    def get_height(self)->int:
        return self._h


class MyText(MyBaseActor):
    text: str = "Kigyoú"
    color = (255, 255, 255)
    alpha: float = 1
    background = None
    fontname = None
    fontsize = 64

    def set_color(self, r: int, g: int, b: int, a: float = 1):
        self.color = (r, g, b)
        self.alpha = a

    def set_background(self, r: int, g: int, b: int):
        self.color = (r, g, b)

    def set_text(self, text: str):
        self.text = text

    def set_alpha(self, a: float):
        self.alpha = a

    def set_fontname(self, fontname: str):
        self.fontname = fontname

    def set_fontsize(self, size: float):
        self.fontsize = size


class MyButton(MyActor, MyText):

    def __init__(self, image="blank.png", pos=(0, 0), anchor=(0, 0), width:int=256, height:int=64, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        MyText.__init__(self)
        self.set_size(width, height)
        self.set_x(20)
        self.set_y(80)

    def draw(self):
        super().draw()
        Screen(pygame.display.get_surface()).draw.text(self.text, (self.x, self.y), angle=self.angle, color=self.color, background=self.background, fontname=self.fontname, fontsize=self.fontsize, alpha=self.alpha)


class MyLabel(MyText, MyBaseActor):

    def __init__(self, pos=(0, 0), angle=0):
        MyText.__init__(self)
        MyBaseActor.__init__(self)
        self.x: int = pos[0]
        self.y: int = pos[1]
        self.angle: int = angle

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def draw(self):
        Screen(pygame.display.get_surface()).draw.text(self.text, (self.x, self.y), angle=self.angle, color=self.color, background=self.background, fontname=self.fontname, fontsize=self.fontsize, alpha=self.alpha)

    def set_rotation(self, angle: int):
        self.angle = angle


class MyStage(MyBaseActor, MyBaseListeners):
    actors: List[MyBaseActor]

    def __init__(self):
        MyBaseActor.__init__(self)
        MyBaseListeners.__init__(self)
        self.actors = []

    def update(self, delta_time: float = 0.0166666666666666666666):
        super(MyStage, self).update(delta_time)
        for obj in self.actors:
            obj.update(delta_time)

    def draw(self):
        for obj in self.actors:
            obj.draw()

    def add_actor(self, actor: MyBaseActor):
        if isinstance(actor, MyBaseActor):
            self.actors.append(actor)
            if actor._stage != 0:
                print("A következő actor át lett helyezve a " + str(id(actor._stage)) + " stageből a " + str(id(self)) + " stagebe.")
                actor.remove_from_stage()
            actor.set_stage(self)
        else:
            print("ERROR: Az objektum példány nem adható hozzá a staghez, mert nem a MyBaseActor leszármazottja.")

    def remove_actor(self, actor: MyBaseActor):
        self.actors.remove(actor)
        actor.set_stage(0)

    def on_mouse_down(self, pos, button):
        if self._on_mouse_down_listener != 0:
            self._on_mouse_down_listener(pos, button)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_down(pos, button)

    def on_mouse_up(self, pos, button):
        if self._on_mouse_up_listener != 0:
            self._on_mouse_up_listener(pos, button)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_up(pos, button)

    def on_mouse_move(self, pos):
        if self._on_mouse_move_listener != 0:
            self._on_mouse_move_listener(pos)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_move(pos)

    def on_key_down(self, key, mod, unicode):
        if self._on_key_down_listener != 0:
            self._on_key_down_listener(key, mod, unicode)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_key_down(key, mod, unicode)

    def on_key_up(self, key, mod):
        if self._on_key_up_listener != 0:
            self._on_key_up_listener(key, mod)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_key_up(key, mod)


#Minden időzítőt a stagehez vagy actorhoz lehet hozzáadni. A lényeg, hogy oda lehet beilleszteni, ahol megjelent az .add_timer(...) metódus.
# pl.: text2.add_timer(MyTickTimer(self.tikk))
#  ahol a text2 egy Button típus.
#
#   Vagy referenciát csinálva:
#   self.timer: MyIntervalTimer = MyIntervalTimer(csinaldeztfuggveny, 3, 7)
#   stage.add_timer(self.timer)
#   ...
#   Máshol meghívható, akár egy kattintáskor:
#   self.timer.stop()
#
#   Minden időzítő megállítható, elindítható a start() és a stop() metódusokkal.
#   Az időzítő eltávolítható a remove() függvénnyel.
#
#   Az időzítő eseményéhez illesztett függvénynek egy paraméterének kell lenni, ami az időzítőt adja eredményül. Innen lehet lekérdezni például, hogy hányszor futott le, vagy mióta megy éppen.
#   pl:
#   text2.add_timer(MyTickTimer(self.tikk))

#     def tikk(self, timer: MyMultiTickTimer):
#         print("TIKK " + str(timer.count))
# TIKK 1
# TIKK 2
# TIKK 3
#
# Ez az osztály minden időzítő őse. Ezeket a funkciókat, amik benne vannak, minden időzítő tudja.
class MyBaseTimer:

    _listener = 0
    _enabled: bool = True
    correction: float = 0
    base_actor: MyBaseActor = 0
    elapsed_time:float = 0

    def __init__(self, func = 0):
        self._listener = func

    def set_timer_listener(self, func):
        self._listener = func

    def remove_timer_listener(self, func):
        self._listener = 0

    def start(self):
        self._enabled = True

    def stop(self):
        self._enabled = False

    def update(self, deltaTime: float = 0.0166666666666666666666):
        if self._enabled:
            self.elapsed_time += deltaTime
            self._do_timer()

    def _do_timer(self):
        pass

    def remove(self):
        if self.base_actor == 0:
            return
        self.base_actor.remove_timer(self)
        self.base_actor = 0


#Folyamatosan fut, ki és be lehet kapcsolni.
class MyPermanentTimer(MyBaseTimer):

    def _do_timer(self):
        if self._listener != 0:
            self._listener(self)


# Folyamatosan fut, de csak meghatározott időközönként futtatja le a kódot.
class MyTickTimer(MyBaseTimer):

    # interval: ennyi időközönként
    # start_delay: A hozzáadás után ennyivel később fut le először
    # repeat: ismétli, többször fut
    def __init__(self, func=0, interval: float = 1, start_delay: float = 0, repeat: bool = True):
        super().__init__(func)
        self.interval: float = interval
        self.elapsed_time = -start_delay
        self.repeat: bool = repeat

    def _do_timer(self):
        if not self._enabled:
            return
        if self.elapsed_time >= self.interval:
            self.correction = self.elapsed_time-self.interval
            if self._listener != 0:
                self._listener(self)
            if not self.repeat:
                self.stop()
            else:
                self.elapsed_time = self.correction


# folyamatosan, minden száításkor lefut egy intervallumon belül.
class MyIntervalTimer(MyBaseTimer):

    #start_time: futás kezdete
    #stop_time: futás vége
    def __init__(self, func=0, start_time: float = 1, stop_time: float = 4):
        super().__init__(func)
        self.start_time = start_time
        self.stop_time = stop_time

    def _do_timer(self):
        if not self._enabled:
            return
        if (self.elapsed_time >= self.start_time) and (self.elapsed_time <= self.stop_time):
            if self._listener != 0:
                self._listener(self)


# Egyszer fut le a hozzáadást követően. Ezután eltávolítja megát a birtokló objektum példányból.
class MyOneTickTimer(MyBaseTimer):

    def __init__(self, func=0, interval: float = 1):
        self.interval = interval
        super().__init__(func)

    def _do_timer(self):
        if not self._enabled:
            return
        if self.elapsed_time >= self.interval:
            self.correction = self.elapsed_time - self.interval
            if self._listener != 0:
                self._listener(self)
            self.remove()


# Meg lehet adni, hogy hányszor fusson le, és ez milyen időközönként legyen. Ezután eltávolítja megát a birtokló objektum példányból.
class MyMultiTickTimer(MyBaseTimer):

    def __init__(self, func=0, interval: float = 1, startdelay: float = 0, count = 5):
        super().__init__(func)
        self.interval: float = interval
        self.elapsed_time = -startdelay
        self.count: int = 0
        self.target_count: int = count

    def _do_timer(self):
        if not self._enabled:
            return
        if self.elapsed_time >= self.interval:
            self.correction = self.elapsed_time-self.interval
            self.count += 1
            if self._listener != 0:
                self._listener(self)
            if self.count >= self.target_count:
                self.remove()
            self.elapsed_time = self.correction

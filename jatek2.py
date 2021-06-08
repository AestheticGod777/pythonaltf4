from n_mygameworld import *
from n_menu_menustage import *
import random


class GameStage(MyStage):

    screen_width = 1000
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pontszam = 0
    lastkey = None
    sebesseg = 4
    teszt = 5


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
        self.borderbal: MyActor = MyActor("border1.png", pos=(0, 0), anchor=(16, 16))
        self.add_actor(self.borderbal)
        self.borderjobb: MyActor = MyActor("border1.png", pos=(1020, 0), anchor=(16, 16))
        self.add_actor(self.borderjobb)
        self.borderfent: MyActor = MyActor("border2.png", pos=(0, 0), anchor=(16, 16))
        self.add_actor(self.borderfent)
        self.borderlent: MyActor = MyActor("border2.png", pos=(0, 850), anchor=(16, 16))
        self.add_actor(self.borderlent)
        self.food: MyActor = MyActor("ama.png", pos=(self.screen_width / 2, (self.screen_height / 2) - 200), anchor=(16, 16))
        self.add_actor(self.food)
        self.set_on_key_down_listener(self.keydownlistener)
        self.set_on_key_up_listener(self.keyuplistener)
        self.snake: MyActor = MyActor("kocka.png", pos=(self.screen_width / 2, self.screen_height / 2), anchor=(16, 16))
        self.add_actor(self.snake)
        self.menu=menu
        self.score: MyLabel = MyLabel()
        self.score.set_x(self.screen_height - self.screen_height + 10)
        self.score.set_y(self.screen_width - self.screen_width + 10)
        self.add_actor(self.score)

    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        if self.lastkey != None:
            if self.lastkey == keys.UP:
                animate(self.snake, pos=(self.snake.pos[0], self.snake.pos[1] - 1000), duration=self.sebesseg)
                self.snake.set_rotation(360)
            if self.lastkey == keys.DOWN:
                animate(self.snake, pos=(self.snake.pos[0], self.snake.pos[1] + 1000), duration=self.sebesseg)
                self.snake.set_rotation(180)
            if self.lastkey == keys.LEFT:
                animate(self.snake, pos=(self.snake.pos[0] - 1000, self.snake.pos[1]), duration=self.sebesseg)
                self.snake.set_rotation(90)
            if self.lastkey == keys.RIGHT:
                animate(self.snake, pos=(self.snake.pos[0] + 1000, self.snake.pos[1]), duration=self.sebesseg)
                self.snake.set_rotation(270)

        if self.food.is_on_stage() and self.food.overlaps_with(self.snake):
            self.pontszam += 1
            print(self.pontszam)
            self.food.set_x(x=random.randint(64, self.screen_width))
            self.food.set_y(y=random.randint(64, self.screen_height))
        self.score.set_text("Score: " + str(self.pontszam))

        if self.pontszam >= 5:
            self.sebesseg = 3
        elif self.pontszam >= 10:
            self.sebesseg = 2.5
        elif self.pontszam >= 20:
            self.sebesseg = 2
        elif self.pontszam >= 50:
            self.sebesseg = 1.5
        elif self.pontszam >= 100:
            self.sebesseg = 1
        elif self.pontszam >= 250:
            self.sebesseg = 0.5
        elif self.pontszam >= 500:
            self.sebesseg = 0.3
        elif self.pontszam >= 1000:
            self.sebesseg = 0.1

        if self.snake.is_on_stage() and self.snake.overlaps_with(self.borderbal):
            self.menu.menu_Blank()

        if self.snake.is_on_stage() and self.snake.overlaps_with(self.borderjobb):
            self.menu.menu_Blank()

        if self.snake.is_on_stage() and self.snake.overlaps_with(self.borderfent):
            self.menu.menu_Blank()

        if self.snake.is_on_stage() and self.snake.overlaps_with(self.borderlent):
            self.menu.menu_Blank()




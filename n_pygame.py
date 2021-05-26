# https://pygame-zero.readthedocs.io/en/stable/index.html
# Pygame Zero telepítése:
# - Fel kell tenni egy python interpretert, célszerű minden felhasználónak telepíteni, én a c:\python mappába raktam, és a path-beállításokat engedélyeztem, hogy bárhonnan el lehessen érni.
# - Utána parancssorban ki kell adni: pip install pgzero
# - A PyCharm-ban az előbb feltelepített interpretert kell beállítani.
# - És már szalad is!
import pgzrun
# Ebben vannak a saját fejlesztésú osztályok, a MyStage és a MyActor
from numpy.distutils.conv_template import unique_key
from n_mygameworld import *
from n_staractor import StarActor

# Globális eseménykezelő, csak egy ilyen lehet a programban. A kattintás eseményt kezeli, a pos változó a kattintás helye, a button pedig a gomb értéke, amelyikkel kattinttunk
# Fontos, hogy ez a függvény ezzel a névvel és paraméterlistával jöjjön létre.
def on_mouse_down(pos, button):
    # Az esemény értékeit elküldi a Stage számára, az mejd továbbküldi az Actoroknak
    gamestage.on_mouse_down(pos, button)


# Globális eseménykezelő, csak egy ilyen lehet a programban. A kattintás eseményt kezeli, a pos változó a kattintás helye, a button pedig a gomb értéke
# Fontos, hogy ez a függvény ezzel a névvel és paraméterlistával jöjjön létre.
def on_mouse_move(pos):
    # Az esemény értékeit elküldi a Stage számára, az mejd továbbküldi az Actoroknak
    gamestage.on_mouse_move(pos)


# Globális eseménykezelő, csak egy ilyen lehet a programban. A kattintás eseményt kezeli, a pos változó a kattintás helye, a button pedig a gomb értéke, amelyikkel kattinttunk
# Fontos, hogy ez a függvény ezzel a névvel és paraméterlistával jöjjön létre.
def on_mouse_up(pos, button):
    # Az esemény értékeit elküldi a Stage számára, az mejd továbbküldi az Actoroknak
    gamestage.on_mouse_up(pos, button)


def on_key_down(key, mod, unicode):
    print("DOWN: " + str(key) + " " + str(mod) + " " + str(unicode))
    gamestage.on_key_down(key, mod, unicode)


def on_key_up(key, mod):
    print("UP: " + str(key) + " " + str(mod))
    gamestage.on_key_up(key, mod)


# Ez egy Actorhoz illesztett eseménykezelő lesz majd, később kerül hozzáadásra.
def m2onclick(pos, button):
    # animáltan pozíciót változtat.
    animate(m1, pos=(100, 100))


# Ez egy Actorhoz illesztett eseménykezelő lesz majd, később kerül hozzáadásra.
def m3onclick(pos, button):
    # animáltan pozíciót változtat. Az új pozíció a kattintás helye
    animate(m3, pos=pos)


def keydownlistener(key, mod, unicode):
    if key == keys.UP:
        animate(m1, pos=(m1.pos[0], m1.pos[1] - 10), duration=0.1)
    if key == keys.DOWN:
        animate(m1, pos=(m1.pos[0], m1.pos[1] + 10), duration=0.1)
    if key == keys.LEFT:
        animate(m1, pos=(m1.pos[0] - 10, m1.pos[1]), duration=0.1)
    if key == keys.RIGHT:
        animate(m1, pos=(m1.pos[0] + 10, m1.pos[1]), duration=0.1)


# A játékmenet (szimuláció) itt lép egyet előre. A dt paraméter a két képkocka közt eltelt idő. 60 fps esetén 0.016666 mp az értéke.
def update(dt):
    # A Stage szereplőit előre kell léptetni az időben, ezért kell ennek is az update metódusát meghívni.
    gamestage.update(dt)
    # Egy egyszerű átfedés vizsgálat m1 és m2 közt. Ha átfednek, akkor az m2 eltűnik a stageről
    if m2.overlaps_with(m1):
        m2.remove_from_stage()


# Minden képkockánál teljesen újra kell rajzolni a képernyőt. Ez a metódus a Staget rajzolja ki a képernyőre. Nem lesz villogás a dupla pufferelés miatt.
def draw():
    # Törlés, vagy színezés, hogy az előző rajz eltűnjön.
    #screen.clear()
    screen.fill("#113333")
    # A Stage kirajzolása
    gamestage.draw()


# Létre kell hozni egy játékteret, ahol a szereplők majd megjelennek. Az egy térhez tartozó szereplőket a MyStage gyűjti össze.
# Akár több stage is létrehozható, de akkor azokat mind a feljebb lévő eljárásokban is kezelni kell
# Ha pedig egyszer az egyiket, egyszer pedig a másikat (pl játék menü és játék közt váltás) szeretnénk látni, akkor el kell ott ágazni annak megfelelően, amit látni akarunk. (Vagy létre kell hozni egy magasabb szervezettségi szintet, pl Screen névvel, ami Stage-ket gyűjt.)
gamestage = MyStage()

# Egy Actor létrehozása. A képnek az ./images mappában kell lenni!!! Pos kezdőpozíció, anchor pedig a forgatási pont, és a kép ezen pontja kerül a pos értékre.
# Itt mindig a MyActorból vagy annak a leszármazottjából legyenek a példányok, mert az kiokosítottam:)
m1 = MyActor(image="m_jerry.png", pos=(0, 0), anchor=(0, 0))
m1.set_width(30, 30)

# Másik példány, ugyan azzal a képpel.
m2 = MyActor(image="m_jerry.png", pos=(220, 220), anchor=(0, 0))

# Méretarányos méretezés. Használjuk mindig az általam készített metódusokat, ha lehet. Pl a méret változtatás Pygame Zero szintjén nem támogatott funkció.


# Esemény hozzáadása az m2 példányhoz, azaz ha rákattintunk, akkor a fent definiált m2onclick hajtódik végre.
m2.set_on_mouse_down_listener(m2onclick)
m2.set_width(30)
m2.set_rotation(90)


# Ez egy kicsivel bonyolultabb létrehozása az Actornak, azaz a StarActor örökli a MyActort, és ott már mindent előkészít. Így itt csak létre kell paraméter nélkül hozni, és csinálja a dolgát önállóan.
m3 = StarActor()
m3.set_size(500, 500)


for i in range(100):
    gamestage.add_actor(StarActor())

# A Stagere való kattintást kezeli, azaz ha rákattintunk a képernyőre, akkor a fent definiált m3onclick hajtódik végre.
gamestage.set_on_mouse_down_listener(m3onclick)
gamestage.set_on_key_down_listener(keydownlistener)

# Hozzá kell adni őket a stagehez, mivel a stage jelenik meg a képernyőn, ezen keresztül jelennek meg majd az Actorok is.
gamestage.add_actor(m1)
gamestage.add_actor(m2)
gamestage.add_actor(m3)

# Ezzel indul a játék. Összeszedi a fent fix névvel definiált eseménykezelőket, létrehozza az ablakot, stb...
pgzrun.go()

# ZKOUSKA PYGLETU
# import pyglet
# window = pyglet.window.Window()
# pyglet.app.run()
# print('Hotovo!')


import pyglet
import math
window = pyglet.window.Window()

def tik(t):
    had.x = had.x + t * 20
    had.y = 20 + 20 * math.sin(had.x / 5)
    had.rotation = 20 + 20 * math.sin(had.x / 5)

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    had.x = 150

obrazek = pyglet.image.load('snake-icon.png')
had = pyglet.sprite.Sprite(obrazek)

def vykresli():
    window.clear()
    had.draw()

window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
)

pyglet.app.run()
import pyglet
from pyglet import gl

# KONSTANTY
# Velikost okna (v pixelech)
SIRKA = 900
VYSKA = 600

VELIKOST_MICE = 20
TLOUSTKA_PALKY = 10
DELKA_PALKY = 100
RYCHLOST = 200  # v pixelech za sekundu
RYCHLOST_PALKY = RYCHLOST * 1.5  # taky v pixelech za sekundu

DELKA_PULICI_CARKY = 20
VELIKOST_FONTU = 42
ODSAZENI_TEXTU = 30

# GLOBALNí PROMĚNNÉ
pozice_palek = [VYSKA // 2, VYSKA // 2]  # vertikalni pozice dvou palek
pozice_mice = [0, 0]  # x, y souradnice micku -- nastavene v reset()
rychlost_mice = [0, 0]  # x, y slozky rychlosti micku -- nastavene v reset()
stisknute_klavesy = set()  # sada stisknutych klaves
skore = [0, 0]  # skore dvou hracu




def nakresli_obdelnik(x1, y1, x2, y2):
    """Nakresli obdelnik na dane souradnice

    Nazorny diagram::

         y2 - +-----+
              |/////|
         y1 - +-----+
              :     :
             x1    x2
    """
    # Tady pouzijeme volani OpenGL, ktere je pro nas zatim asi nejjednodussi
    # na pouziti
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # ukonci kresleni trojuhelniku

def nakresli_text(text, x, y, pozice_x):
    """Nakresli dany text na danou pozici

    Argument ``pozice_x`` muze byt "left" nebo "right", udava na kterou stranu
    bude text zarovnany
    """
    napis = pyglet.text.Label(
        text,
        font_size=VELIKOST_FONTU,
        x=x, y=y, anchor_x=pozice_x
    )
    napis.draw()

def vykresli():
    """Vykresli stav hry"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # smaz obsah okna (vybarvi na cerno)
    gl.glColor3f(1, 1, 1)  # nastav barvu kresleni na bilou

    # nakresli micek
    nakresli_obdelnik(
        pozice_mice[0] - VELIKOST_MICE // 2,
        pozice_mice[1] - VELIKOST_MICE // 2,
        pozice_mice[0] + VELIKOST_MICE // 2,
        pozice_mice[1] + VELIKOST_MICE // 2,
    )

    # nakresli obe palky
    for x, y in [(0, pozice_palek[0]), (SIRKA, pozice_palek[1])]:
        nakresli_obdelnik(
            x - TLOUSTKA_PALKY,
            y - DELKA_PALKY // 2,
            x + TLOUSTKA_PALKY,
            y + DELKA_PALKY // 2,
        )

    # nakresli delici caru
    for y in range(DELKA_PULICI_CARKY // 2, VYSKA, DELKA_PULICI_CARKY * 2):
        nakresli_obdelnik(
            SIRKA // 2 - 1,
            y,
            SIRKA // 2 + 1,
            y + DELKA_PULICI_CARKY,
            )

    # nakresli_text(
    #     "{}:{}".format(skore[0], skore[1]),
    #     SIRKA - 20,
    #     VYSKA - 80,
    #     "right")

    nakresli_text(
        str(skore[0]),
        x=ODSAZENI_TEXTU,
        y=VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
        pozice_x='left',
    )

    nakresli_text(
        str(skore[1]),
        x=SIRKA - ODSAZENI_TEXTU,
        y=VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
        pozice_x='right',
    )

window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw=vykresli,  # na vykresleni okna pouzij funkci `vykresli`
)
pyglet.app.run()  # vse je nastaveno, at zacne hra
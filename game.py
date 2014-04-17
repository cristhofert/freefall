#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

import gtk
import gobject
import random

import glucosa

WIGTH = 620
HEITH = 480

class Game(glucosa.GameArea):

    def __init__(self):
        glucosa.GameArea.__init__(self)

        self.set_update_loop(60)
        self.set_background(glucosa.Image('images/space.png'))
        self.add_sprite(Cloud(self))
        self.add_sprite(Cloud(self))
        self.add_sprite(Cloud(self))
        self.add_sprite(Cloud(self))
        self.jumper = Jumper(self)
        self.coin = Coin(self)
class Jumper(glucosa.Sprite):

    def __init__(self, game):
        self.game = game
        self.speed = 6
        self.image = glucosa.Image('images/jumper.png')
        self.control = glucosa.Control(self.game)

        glucosa.Sprite.__init__(self, self.image, 0, 0)
        self.game.add_sprite(self)

    def update(self):
        if self.control.left:
            self.x -= self.speed
        elif self.control.right:
            self.x += self.speed

        self._set_bounds()

    def _set_bounds(self):
        """Se asegura de que el sprite no pueda salir de la pantalla"""

        # Bordes horizontales
        if self.x < 0:
            self.x = 0
        elif self.x + 100 > 640:
            self.x = 640 -100

        # Bordes verticales
        if self.y < 0:
            self.y = 0
        elif self.y + 70 > 480:
            self.y = 480 -70

class Coin(glucosa.Sprite):

    def __init__(self, game):
        image = glucosa.Image('images/coin.png')
        glucosa.Sprite.__init__(self, image, 0, -10)
        self.speed = 3
        game.add_sprite(self)

    def update(self):
        self. y -= self.speed

        if self.y < 0:
            self.x = random.randint(0, WIGTH)
            self.y = HEITH + random.randint(20, 300)

class Cloud(glucosa.Sprite):

    def __init__(self, game):
        image = glucosa.Image('images/cloud.png')
        glucosa.Sprite.__init__(self, image, 0, -10)
        self.speed = 1
        game.add_sprite(self)

    def update(self):
        self. y -= self.speed

        if self.y < 0:
            self.x = random.randint(0, WIGTH)
            self.y = HEITH + random.randint(20, 300)

class CloudP(glucosa.Sprite):

    def __init__(self):
        image = glucosa.Image('images/cloud.png')
        x = random.randint(0, WIGTH)
        y = random.randint(0, HEITH)
        glucosa.Sprite.__init__(self, image, x, y)
        self.speed = random.randint(1, 3)

    def update(self):
        self.y -= self.speed

        if self.y < 0:
            self.y = -20
            self.x = random.randint(0, WIGTH)

class Window(gtk.Window):

    def __init__(self):
        super(gtk.Window, self).__init__()

        self.connect('destroy', gtk.main_quit)

        self.set_title('Freefall')
        self.resize(WIGTH, HEITH)

        self.add(Game())

        self.show_all()


if __name__ == '__main__':
    Window()
    gtk.main()

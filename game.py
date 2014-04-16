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
        self.jumper = Jumper(self)

class Jumper(glucosa.Sprite):

    def __init__(self, game):
        self.game = game
        self.image = glucosa.Image('images/jumper.png')
        self.control = glucosa.Control(self.game.canvas)

        glucosa.Sprite.__init__(self, self.images, 0, 0)
        self.game.add_sprite(self)

    def update(self):
        if self.control.left:
            self.x -= self.speed
        elif self.control.right:
            self.x += self.speed

        if self.control.down:
            self.y += self.speed
        elif self.control.up:
            self.y -= self.speed

        if self.can_fire_counter > 0:
            if self.control.fire:
                self.fire()
        else:
            self.can_fire_counter += 1

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

class Cloud(glucosa.Sprite):

    def __init__(self):
        image = glucosa.Image('images/cloud.png')
        x = random.randint(0, WIGHT)
        y = random.randint(0, HEITH)
        glucosa.Sprite.__init__(self, image, x, y)
        self.speed = random.randint(1, 3)

    def update(self):
        self.y -= self.speed

        if self.y > 480:
            self.y = -20
            self.x = random.randint(0, WIGTH)

class Window(gtk.Window):

    def __init__(self):
        super(gtk.Window, self).__init__()

        self.connect('destroy', gtk.main_quit)

        self.set_title('Freefall')

        self.add(Game())


if __name__ == '__main__':
    Window()
    gtk.main()

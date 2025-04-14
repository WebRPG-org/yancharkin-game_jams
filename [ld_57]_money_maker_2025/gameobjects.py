from random import randint
import pyxel

class GameObject:

    def __init__(self, x, y, img_n, img_x, img_y, size=16,
            aframes_n=1, trcol=0, speed=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size

        self.frame = 0
        self.frame_max = aframes_n
        self.images = [
                (img_n, img_x+(self.size*j), img_y, self.size, self.size, trcol)
                        for j in range(0, self.frame_max)
        ]
        self.alive = True

    def animate(self):
        if pyxel.frame_count % 15 == 0:
            self.frame += 1
            if self.frame == self.frame_max:
                self.frame = 0

    def is_on_screen(self):
        return self.y > 16

    def move_up(self):
        self.y -= self.speed

    def update(self):
        self.animate()
        self.move_up()

    def draw(self):
        if self.is_on_screen():
            pyxel.blt(self.x, self.y, *(self.images[self.frame]))

class Ash(GameObject):

    def __init__(self, x=0, y=0, speed=4):
        super().__init__(x=0, y=0, img_n=None, img_x=None, img_y=None,
                size=None, aframes_n=0, trcol=None, speed=None)
        self.x = randint(16, pyxel.width-16)
        #self.x = randint(0, pyxel.width)
        self.y = randint(pyxel.height, pyxel.height+48)
        #colors = [0, 7, 9, 10, 13]
        colors = [0, 0, 0, 0, 0, 0, 0, 0, 0, 9]
        self.color = colors[randint(0, 9)]
        self.speed = randint(1, 2)
    
    def is_on_screen(self):
        return self.y > 16

    def draw(self):
        if self.is_on_screen():
            pyxel.rect(self.x, self.y, 1, 1, self.color)

    def move_up(self):
        self.y -= self.speed
        if self.is_on_screen():
            #self.y = self.y + pyxel.cos(pyxel.frame_count * randint(-16, 16))
            self.x = self.x + pyxel.sin(pyxel.frame_count * randint(-16, 16))

class Flag(GameObject):

    def __init__(self, x, y, img_n=0, img_x=48, img_y=88, size=16,
            aframes_n=1, trcol=0, speed=0.1):
        super().__init__(x, y, img_n=img_n, img_x=img_x, img_y=img_y,
                size=size, aframes_n=aframes_n, trcol=trcol, speed=speed)

class Coin(GameObject):

    def __init__(self, x, y, img_n=0, img_x=0, img_y=16, size=4,
            aframes_n=2, trcol=0, speed=1):
        super().__init__(x, y, img_n=img_n, img_x=img_x, img_y=img_y,
                size=size, aframes_n=aframes_n, trcol=trcol, speed=speed)

class Bag(GameObject):

    def __init__(self, x, y, img_n=0, img_x=0, img_y=24, size=8,
            aframes_n=2, trcol=0, speed=1):
        super().__init__(x, y, img_n=img_n, img_x=img_x, img_y=img_y,
                size=size, aframes_n=aframes_n, trcol=trcol, speed=speed)

class Bomb(GameObject):

    def __init__(self, x, y, img_n=0, img_x=16, img_y=24, size=8,
            aframes_n=2, trcol=0, speed=1):
        super().__init__(x, y, img_n=img_n, img_x=img_x, img_y=img_y,
                size=size, aframes_n=aframes_n, trcol=trcol, speed=speed)

class Lava(GameObject):
    def __init__(self, x, y, img_n=1, img_x=48, img_y=0, size=16,
            aframes_n=2, trcol=0):
        super().__init__(x, y, img_n=img_n, img_x=img_x, img_y=img_y,
                size=size, aframes_n=aframes_n, trcol=trcol, speed=0)

    def update(self):
        self.animate()

class LavaPool:

    def __init__(self):
        self.pool = []
        for i in range(13):
            self.pool.append(Lava(16+(i*16), pyxel.height))
        #for i in range(15):
        #    self.pool.append(Lava(0+(i*16), pyxel.height))

    def reset(self):
        for lava in self.pool:
            lava.y = pyxel.height

    def set_y(self, y):
        for lava in self.pool:
            lava.y = y

    def update(self):
        for lava in self.pool:
            lava.update()

    def draw(self):
        for lava in self.pool:
            lava.draw()

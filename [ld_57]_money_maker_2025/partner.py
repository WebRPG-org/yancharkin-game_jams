from random import randint
import pyxel

class Partner:

    def __init__(self, x, y, speed, size=16):
        self.x = x
        self.y = y
        self.speed = speed
        self.cur_speed = self.speed
        self.size = size
        self.alive = True
        self.frame = 0
        self.frame_max = 2
        self.partner_type = randint(0, 1)
        # img_bank, bank_pos_x, bank_pos_y, w, h, transparent_color
        images = [
                [(0, 56+(self.size*j), 8, -self.size, self.size, 0)
                        for j in range(0, self.frame_max)],
                [(0, 88+(self.size*j), 8, -self.size, self.size, 0)
                        for j in range(0, self.frame_max)]
        ]
        self.image = images[self.partner_type]

    def animate(self):
        if pyxel.frame_count % 15 == 0:
            self.frame += 1
            if self.frame == self.frame_max:
                self.frame = 0

    def move_up(self):
        self.y = self.y - self.cur_speed

    # TODO Add fall action
    #def fall(self)
    #    self.y = self.y + 10

    #def move_down(self):
    #    self.y = min(self.y + self.cur_speed, pyxel.height - self.size)

    #def move_left(self):
    #    self.x = max(self.x - self.cur_speed, 24)

    #def move_right(self):
    #    self.x = min(self.x + self.cur_speed, pyxel.width - 16 - self.size)

    def is_on_screen(self):
        return self.y > 0

    def update(self):
        # TODO Act more smart
        self.animate()
        self.move_up()
        if self.is_on_screen():
            self.y = self.y + pyxel.cos(pyxel.frame_count * 16)

    def draw(self):
        if self.is_on_screen():
            if self.partner_type == 0:
                pyxel.blt(self.x+8, self.y-8, 0, 64, 0, 16, 8, 0)
            else:
                pyxel.blt(self.x+8, self.y-8, 0, 96, 0, 16, 8, 0)
            pyxel.blt(self.x, self.y, *(self.image[self.frame]))

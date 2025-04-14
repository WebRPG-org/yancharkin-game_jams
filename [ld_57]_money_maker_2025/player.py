import pyxel

class Player:

    def __init__(self, x, y, speed, size=16):
        self.x = x
        self.y = y
        self.speed = speed
        self.cur_speed = self.speed
        self.size = size
        self.in_control = True
        self.alive = True
        self.lives = 2
        self.fall_time = 0

        self.frame = 0
        self.frame_max = 2
        # img_bank, bank_pos_x, bank_pos_y, w, h, transparent_color
        self.images = [
                #(0, 56+(self.size*j), 8, self.size, self.size, 0)
                (0, 24+(self.size*j), 8, self.size, self.size, 0)
                        for j in range(0, self.frame_max)
        ]

    def animate(self):
        if pyxel.frame_count % 15 == 0:
            self.frame += 1
            if self.frame == self.frame_max:
                self.frame = 0

    def move_left(self):
        self.x = max(self.x - self.cur_speed, 24)

    def move_right(self):
        self.x = min(self.x + self.cur_speed, pyxel.width - 16 - self.size)

    def move_up(self):
        self.y = max(self.y - self.cur_speed, 24)

    def move_down(self):
        self.y = min(self.y + self.cur_speed, pyxel.height - self.size)

    def is_on_screen(self):
        return self.y < pyxel.height+8

    def update(self):
        self.animate()
        if self.in_control:
            if (pyxel.btn(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_LEFT)) or \
                (pyxel.btn(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_RIGHT)) or \
                (pyxel.btn(pyxel.KEY_DOWN) and pyxel.btn(pyxel.KEY_LEFT)) or \
                (pyxel.btn(pyxel.KEY_DOWN) and pyxel.btn(pyxel.KEY_RIGHT)):
                    self.cur_speed = self.speed * pyxel.sqrt(2) / 2
            else:
                self.cur_speed = self.speed
            if pyxel.btn(pyxel.KEY_LEFT):
                self.move_left()
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.move_right()
            if pyxel.btn(pyxel.KEY_UP):
                self.move_up()
            if pyxel.btn(pyxel.KEY_DOWN):
                self.move_down()
        else:
            self.y = self.y + 10
        if self.is_on_screen():
            self.y = self.y + pyxel.cos(pyxel.frame_count * 16)
            #self.x = self.x + pyxel.sin(pyxel.frame_count * 16)

    def draw(self):
        if self.is_on_screen():
            if self.lives == 2:
                #pyxel.blt(self.x-8, self.y-8, 0, 48, 0, 16, 8, 0)
                pyxel.blt(self.x-8, self.y-8, 0, 16, 0, 16, 8, 0)
            elif self.lives == 1:
                #pyxel.blt(self.x-8, self.y-8, 0, 64, 0, 16, 8, 0)
                pyxel.blt(self.x-8, self.y-8, 0, 32, 0, 16, 8, 0)
            pyxel.blt(
                    self.x, self.y, *(self.images[self.frame])
            )

import pyxel
from game import Game
from gameobjects import Flag
from player import Player
from audio import Audio

class App:

    def __init__(self):
        pyxel.init(240, 176, display_scale=2, capture_sec=0, fps=30)
        pyxel.load("res.pyxres")
        self.audio = Audio()
        self.flag = Flag(pyxel.width-38, pyxel.height-48)
        self.player = Player(38, pyxel.height-32, 1)
        self.audio.play_music(1)
        pyxel.run(self.update, self.draw)

    def draw_ground(self):
        for i in range(15):
            if (pyxel.frame_count >= 8*30) and (i in (1, 2, 3, 4)):
                pass
            else:
                pyxel.blt(16*i, pyxel.height-16, 0, 24, 112, 16, 16, 0)

    def draw_flag(self):
        if (pyxel.frame_count < 10*30):
            pyxel.rect(pyxel.width-38, pyxel.height-96, 1, 80, 13)
            self.flag.draw()

    def draw_player(self):
        if (pyxel.frame_count < 8*30):
            pyxel.blt(30, pyxel.height-40, 0, 0, 104, 24, 24, 0)
        else:
            self.player.draw()

    def update(self):
        self.flag.move_up()
        if pyxel.frame_count == 8*30:
            self.player.in_control = False
            self.audio.play_fall_snd()
        elif pyxel.frame_count >= 8*30:
            self.player.update()
        if pyxel.frame_count == 10*30:
            Game(pyxel.frame_count)

    def draw(self):
        pyxel.cls(0)
        #pyxel.cls(12)
        pyxel.rect(29, 16, 182, 55, 7)
        pyxel.rect(30, 17, 180, 53, 9)
        pyxel.blt(36, 24, 0, 0, 32, 80, 16, 1)
        pyxel.blt(124, 24, 0, 0, 48, 80, 16, 1)
        pyxel.blt(88, 48, 0, 0, 64, 64, 16, 1)
        self.draw_ground()
        self.draw_flag()
        self.draw_player()
        #pyxel.text(pyxel.width/2 - 1, pyxel.height/2 - 3,
        #           str(int(pyxel.frame_count/30)+1), 7)

App()

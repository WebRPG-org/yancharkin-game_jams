import pyxel

class Audio:

    def __init__(self):
        self.__music_off = True

    def play_money_snd(self):
        pyxel.play(0, 63, resume=True)

    def play_fall_snd(self):
        #pyxel.play(0, [61, 62], resume=True)
        pyxel.play(0, 61, resume=True)
    
    def play_hit_snd(self):
        pyxel.play(0, 60, resume=False)
    
    def play_money_hit_snd(self):
        pyxel.play(0, 58, resume=True)
    
    def play_impact_snd(self):
        pyxel.play(0, 59, resume=True)

    def play_music(self, track_n, loop=False):
        pyxel.playm(track_n, loop=loop)

    #def toggle_music(self):
    #    if self.__music_off:
    #        pyxel.playm(0, loop=True)
    #        self.__music_off = False
    #    else:
    #        #pyxel.stop(1)
    #        #pyxel.stop(2)
    #        #pyxel.stop(3)
    #        pyxel.stop()
    #        self.__music_off = True


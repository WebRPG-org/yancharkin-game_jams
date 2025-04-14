from random import randint
import pyxel
from level import Level
from player import Player
from hud import HUD
from timer import Timer
from audio import Audio
from gameobjects import Coin, Bag, Bomb, Ash
from partner import Partner

class Game:

    TIMEOUT = 66
    SCORE = 0

    def __init__(self, intro_time):
        self.intro_time = intro_time
        self.level = Level(pyxel.tilemaps[0], 30, 22)
        #self.player = Player(112, 32, 1)
        self.player = Player(38, 32, 1)
        self.hud = HUD()
        self.timer = Timer()
        self.timer.start()
        self.audio = Audio()
        #self.__music_off = True
        self.__time_is_out = False
        self.__player_is_dead = False

        self.deposits = []
        self.money = []
        self.friends = []
        self.enemies = []
        self.money_maker()
        self.enemy_maker()
        self.ash = []
        self.audio.play_music(2, loop=True)

        pyxel.run(self.update, self.draw)

    def restart(self):
        if self.hud.game_over:
            self.player.alive = True
            self.player.lives = 2
            #self.player.x = 112
            self.player.x = 38
            self.player.y = 32
            self.player.in_control = True
            self.player.fall_time = 0
            self.hud.game_over = False
            self.timer.reset()
            self.intro_time = pyxel.frame_count
            self.level.lava_timer = False
            self.level.lava_time = 0
            self.level.lava_pool.reset()
            self.deposits = []
            self.money = []
            self.money_maker()
            self.friends = []
            self.enemies = []
            self.enemy_maker()
            self.SCORE = 0
            self.__time_is_out = False
            self.__player_is_dead = False
            self.timer.start()
            self.audio.play_music(2, loop=True)

    def money_maker(self):
        def make_a_bit(spawn_time, mtype):
            x = randint(24, pyxel.width-24)
            y = pyxel.height
            speed = randint(1, 2)
            if mtype == Bag:
                speed = randint(2, 3)
            self.deposits.append([spawn_time, mtype, x, y, speed])

        intervals = [0, 20, 42, 64]
        for i in range(1, len(intervals)):
            for j in range(0, 10):
                spawn_time = randint(intervals[i-1], intervals[i])
                mtype = randint(0, 3)
                if mtype == 3:
                    make_a_bit(spawn_time, Bag)
                else:
                    make_a_bit(spawn_time, Coin)

    def spawn_ash(self):
        for i in range(1):
            a = Ash()
            self.ash.append(a)

    def move_ash(self):
        for a in self.ash:
            a.move_up()
    
    def cleanup_ash(self):
        for i, entity in enumerate(self.ash):
            if not entity.is_on_screen():
                del self.ash[i]
    
    def draw_ash(self):
        for a in self.ash:
            a.draw()

    def money_spawner(self):
        for i, s in enumerate(self.deposits):
            if s[0] == self.timer.time:
                income = s[1](s[2], s[3], speed=s[4])
                self.money.append(income)
                del self.deposits[i]
    
    def update_cleanup_money(self):
        for i, entity in enumerate(self.money):
            entity.update()
            if (abs(self.player.x+3 - entity.x) < 5 \
                    and abs(self.player.y - entity.y) < 16) \
                    or not entity.is_on_screen():
                if entity.is_on_screen():
                    self.audio.play_money_snd()
                    if type(entity) == Coin:
                        self.SCORE += 1
                    elif type(entity) == Bag:
                        self.SCORE += 10
                entity.alive = False
                del self.money[i]

    def draw_money(self):
        for i, entity in enumerate(self.money):
            entity.draw()

    def enemy_maker(self):
        def make_a_bit(spawn_time, mtype):
            x = randint(24, pyxel.width-24)
            y = pyxel.height
            speed = 1
            if mtype == Bomb:
                speed = randint(2, 3)
            self.friends.append([spawn_time, mtype, x, y, speed])

        intervals = [20, 42, 64]
        for i in range(1, len(intervals)):
            for j in range(0, 10):
                spawn_time = randint(intervals[i-1], intervals[i])
                mtype = randint(0, 3)
                if mtype == 3:
                    make_a_bit(spawn_time, Partner)
                else:
                    make_a_bit(spawn_time, Bomb)

    def enemy_spawner(self):
        for i, s in enumerate(self.friends):
            if s[0] == self.timer.time:
                friend = s[1](s[2], s[3], speed=s[4])
                self.enemies.append(friend)
                del self.friends[i]

    def update_cleanup_enemies(self):
        for i, entity in enumerate(self.enemies):
            entity.update()
            if (abs(self.player.x+3 - entity.x) < 5 \
                    and abs(self.player.y - entity.y) < 16) \
                    or not entity.is_on_screen():
                if entity.is_on_screen():
                    if type(entity) == Bomb:
                        self.audio.play_hit_snd()
                        self.player.lives -= 1
                    elif type(entity) == Partner:
                        self.audio.play_money_hit_snd()
                        self.SCORE += 100
                        self.player.lives -= 1
                entity.alive = False
                del self.enemies[i]

    def draw_enemies(self):
        for i, entity in enumerate(self.enemies):
            entity.draw()

    def is_player_dead(self):
        if (self.player.lives <= 0) and not self.__player_is_dead:
            self.__player_is_dead = True
            return True
        else:
            return False

    def is_timeout(self):
        if (pyxel.frame_count-self.intro_time == 30*self.TIMEOUT) and not self.__time_is_out:
            self.__time_is_out = True
            return True
        else:
            return False

    def check_gameover(self):
        if self.player.fall_time != 0:
            if pyxel.frame_count == self.player.fall_time + 2*30:
                self.audio.play_music(0)
                self.hud.game_over = True
                self.timer.pause()

    def update(self):
        self.spawn_ash()
        self.move_ash()
        self.cleanup_ash()
        self.timer.update()
        if self.is_timeout() or self.is_player_dead():
            self.player.in_control = False
            self.level.lava_timer = True
            if self.player.fall_time == 0:
                self.audio.play_fall_snd()
                pyxel.stop()
        self.level.lava_timer_update()
        if not self.player.is_on_screen() and self.player.alive:
            if self.player.fall_time == 0:
                self.player.fall_time = pyxel.frame_count
                self.audio.play_impact_snd()
            self.player.alive = False
        self.check_gameover()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #if pyxel.btnp(pyxel.KEY_M):
        #    self.audio.toggle_music()
        if pyxel.btnp(pyxel.KEY_R):
           pyxel.stop()
           self.restart()
        self.money_spawner()
        self.enemy_spawner()
        self.player.update()
        self.update_cleanup_money()
        self.update_cleanup_enemies()
        if self.player.in_control:
            self.level.animate()
        else:
            self.level.move_lava()
            self.level.lava_pool.update()

    def draw(self):
        pyxel.cls(0)
        self.level.draw()
        self.draw_money()
        self.draw_enemies()
        self.player.draw()
        self.draw_ash()
        if self.timer.time < self.TIMEOUT:
            self.hud.draw(self.timer.time, self.SCORE)
        else:
            self.hud.draw(self.TIMEOUT, self.SCORE)
        self.level.lava_pool.draw()

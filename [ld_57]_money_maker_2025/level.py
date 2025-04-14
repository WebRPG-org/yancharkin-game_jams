import pyxel
from timer import Timer
from gameobjects import LavaPool

class LevelTile:
    # 8x8
    wall = (1, 0)
    # 16x16
    walls = [
        [
            (2, 0),
            (3, 0),
            (2, 1),
            (3, 1)
        ],
        [
            (4, 0),
            (5, 0),
            (4, 1),
            (5, 1)
        ]
    ]

    empty = (0, 0)

class Level:

    def __init__(self, tilemap, w, h):
        self.w = w
        self.h = h
        self.tilemap = tilemap
        self.level_map = []
        self.frame = 0
        self.speed = 8
        self.lava_timer = False
        self.lava_time = 0
        self.lava_pool = LavaPool()

        for y in range(self.h):
            self.level_map.append([])
            for x in range(self.w):
                # 8x8
                if self.tilemap.pget(x, y) == LevelTile.wall:
                    self.level_map[y].append(LevelTile.wall)
                # 16x16
                elif self.tilemap.pget(x, y) == LevelTile.walls[0][0]:
                    self.level_map[y].append(LevelTile.walls[0][0])
                elif self.tilemap.pget(x, y) == LevelTile.walls[0][1]:
                    self.level_map[y].append(LevelTile.walls[0][1])
                elif self.tilemap.pget(x, y) == LevelTile.walls[0][2]:
                    self.level_map[y].append(LevelTile.walls[0][2])
                elif self.tilemap.pget(x, y) == LevelTile.walls[0][3]:
                    self.level_map[y].append(LevelTile.walls[0][3])
                elif self.tilemap.pget(x, y) == LevelTile.walls[1][0]:
                    self.level_map[y].append(LevelTile.walls[1][0])
                elif self.tilemap.pget(x, y) == LevelTile.walls[1][1]:
                    self.level_map[y].append(LevelTile.walls[1][1])
                elif self.tilemap.pget(x, y) == LevelTile.walls[1][2]:
                    self.level_map[y].append(LevelTile.walls[1][2])
                elif self.tilemap.pget(x, y) == LevelTile.walls[1][3]:
                    self.level_map[y].append(LevelTile.walls[1][3])
                else:
                    self.level_map[y].append(LevelTile.empty)

    def animate(self):
        if pyxel.frame_count % self.speed == 0:
            self.frame += 1
            if self.frame == 2:
                self.frame = 0

    def lava_timer_update(self):
        if self.lava_timer:
            if pyxel.frame_count % 2 == 0:
                self.lava_time += 1

    #pyxel.blt(16, 32, 1, 48, 0, 16, 16, 0)
    def move_lava(self):
        if self.lava_time > 3:
            #pyxel.rect(0, pyxel.height-16, pyxel.width, 16, 9)
            self.lava_pool.set_y(pyxel.height-16)
        elif self.lava_time > 2:
            #pyxel.rect(0, pyxel.height-12, pyxel.width, 16, 9)
            self.lava_pool.set_y(pyxel.height-12)
        elif self.lava_time > 1:
            #pyxel.rect(0, pyxel.height-8, pyxel.width, 16, 9)
            self.lava_pool.set_y(pyxel.height-18)
        elif self.lava_time > 0:
            #pyxel.rect(0, pyxel.height-4, pyxel.width, 16, 9)
            self.lava_pool.set_y(pyxel.height-4)

    def draw(self):
        for y in range(self.h):
             for x in range(self.w):
                tile = self.level_map[y][x]
                for j in range(4):
                    if tile == LevelTile.walls[0][j]:
                        tile = LevelTile.walls[self.frame][j]
                    elif tile == LevelTile.walls[1][j]:
                        tile = LevelTile.walls[abs(self.frame-1)][j]
                    pyxel.blt(x * 8, y * 8, 1, tile[0] * 8, tile[1] * 8, 8,8)


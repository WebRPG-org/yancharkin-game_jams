import pyxel

class Timer:

    def __init__(self):
        self.time = -1
        self.running = False

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def reset(self):
        self.time = 0

    def update(self):
        if self.running:
            if pyxel.frame_count % 30 == 0:
                self.time += 1

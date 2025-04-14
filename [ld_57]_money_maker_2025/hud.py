import pyxel

class HUD:

    def __init__(self):
        #self.__font_h = 5
        self.__font_w = 3
        self.__padding = 32
        self.game_over = False

    def _get_string_len(self, s):
        return (len(s) * self.__font_w) + (len(s) - 1)

    def draw(self, time, score):
        if self.game_over and (pyxel.frame_count % 30 != 0):
            game_over_str = "GAME OVER"
            game_over_str_len = self._get_string_len(game_over_str)
            pyxel.text(
                    pyxel.width/2 - game_over_str_len/2,
                    pyxel.height/2 - 9,
                    game_over_str, 7
            )
            restart_str = "PRESS 'R' TO RESTART"
            restart_str_len = self._get_string_len(restart_str)
            pyxel.text(
                    pyxel.width/2 - restart_str_len/2,
                    pyxel.height/2 + 3,
                    restart_str, 7
            )
        pyxel.rect(0, 0, pyxel.width, 16, 7)
        pyxel.rect(1, 1, pyxel.width-2, 14, 0)

        time_str = f'TIME: {time:02}'
        time_str_len = self._get_string_len(time_str)
        pyxel.text(self.__padding, 5, time_str, 7)

        score_str = f'SCORE: {score:03}'
        score_str_len = self._get_string_len(score_str)
        pyxel.text(pyxel.width-self.__padding-score_str_len, 5, score_str, 7)

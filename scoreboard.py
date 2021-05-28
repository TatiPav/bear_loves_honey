import pygame.font
from pygame.sprite import Group
from vinni import Vinni

class Scoreboard:
    """Табло для вывода информации"""
    def __init__(self, bh_game):
        self.bh_game = bh_game
        self.screen = bh_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = bh_game.settings
        self.stats = bh_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_vinni_s

    def prep_score(self):
        # Пребразование в графическое изображение
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                                            self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_vinni_s(self):
        # Информация об оставшихся медвежонках
        self.vinni_s = Group
        for vinni_number in range(self.stats.vinni_s_left):
            vinni = Vinni(self.bh_game)
            vinni.rect.x = 10 + vinni_number * vinni.rect.width
            vinni.rect.y = 10
            self.vinni_s.add(vinni)

    def check_high_score(self):
        # Проверка наличия нового рекорда
        if self.stats.score > self.stats.high_score:
            self.stats.high_score =self.stats.score
            self.prep_high_score()

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.vinni_s.draw(self.screen)

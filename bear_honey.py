import sys
import pygame

from settings import Settings
from vinni import Vinni


class BearHoney:
    """Класс для управления игрой"""

    def __init__(self):
        """Создаётся игра"""
        pygame.init()
        self.settings = Settings()

        """Создаём окно для прорисовки графических элементов - кортеж для размера экрана"""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Мишки любят мёд")

        self.vinni = Vinni(self)

    def run_game(self):
        """Запускаем основной цикл игры, управляем обновленем экрана"""
        while True:
            self._check_events()
            self.vinni.update()
            self._update_screen()


    def _check_events(self):
            # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.vinni.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.vinni.moving_left = True
                elif event.key == pygame.K_UP:
                    self.vinni.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.vinni.moving_down = True



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.vinni.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.vinni.moving_left = False
                elif event.key == pygame.K_UP:
                    self.vinni.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.vinni.moving_down = False

    def _update_screen(self):
        # При каждом проходе цикла прорисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.vinni.blitme()
        # Отображается последнее окно
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    bh = BearHoney()
    bh.run_game()

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

        # self.vinni = Vinni(screen)
        self.vinni = Vinni(self)

    def run_game(self):
        """Запускаем основной цикл игры, управляем обновленем экрана"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.vinni.blitme()
            # Отображается последнее окно
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    bh = BearHoney()
    bh.run_game()

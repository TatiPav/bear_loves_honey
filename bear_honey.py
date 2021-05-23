import sys
import pygame

from settings import Settings
from vinni import Vinni
from bee import Bee


class BearHoney:
    """Класс для управления игрой"""

    def __init__(self):
        """Создаётся игра"""
        pygame.init()
        self.settings = Settings()

        """Вычисление размера экрана"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Мишки любят мёд")

        self.vinni = Vinni(self)
        # Создаём группу
        self.bees = pygame.sprite.Group()

    def run_game(self):
        """Запускаем основной цикл игры, управляем обновленем экрана"""
        while True:
            self._check_events()
            self.vinni.update()
            self.bees.update()
            self._update_screen()


    def _check_events(self):
            # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.vinni.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.vinni.moving_left = True
        elif event.key == pygame.K_UP:
            self.vinni.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.vinni.moving_down = True
            """Выход клавишей q"""
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bee()


    def _check_keyup_events(self, event):
        """Отпущены клавиши"""
        if event.key == pygame.K_RIGHT:
            self.vinni.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.vinni.moving_left = False
        elif event.key == pygame.K_UP:
            self.vinni.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.vinni.moving_down = False

    def _fire_bee(self):
        """Создание новой пчелы и включение её в группу bees"""
        new_bee = Bee(self)
        self.bees.add(new_bee)


    def _update_screen(self):
        # При каждом проходе цикла прорисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.vinni.blitme()
        for bee in self.bees.sprites():
            bee.draw_bee()
        # Отображается последнее окно
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    bh = BearHoney()
    bh.run_game()

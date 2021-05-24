import sys
import pygame

from settings import Settings
from vinni import Vinni
from bee import Bee
from honey import Honey


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
        self.honeyes = pygame.sprite.Group()

        self._create_shelf()

    def run_game(self):
        """Запускаем основной цикл игры, управляем обновленем экрана"""
        while True:
            self._check_events()
            self.vinni.update()
            self._update_bees()
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
        if len(self.bees) < self.settings.bee_allowed:
            new_bee = Bee(self)
            self.bees.add(new_bee)

    def _create_shelf(self):
        # Создание полок для мёда
        honey = Honey(self)
        honey_width, honey_height = honey.rect.size
        available_space_x = self.settings.screen_width - (2 * honey_width)
        number_honeyes_x = available_space_x // (2 * honey_width)
        # Расчитываем возможное к-во полок на экране
        vinni_height = self.vinni.rect.height
        available_space_y = (self.settings.screen_height - (3 * honey_height) - vinni_height)
        number_rows = available_space_y // (2 * honey_height)

        for row_number in range(number_rows):
            # Создание первой полки банок с мёдом
            for honey_number in range(number_honeyes_x):
                self._create_honey(honey_number, row_number)

    def _create_honey(self, honey_number, row_number):
        # Создание банки с мёдом и размещение её в ряду
        honey = Honey(self)
        honey_width, honey_height = honey.rect.size
        honey.x = honey_width + 2 * honey_width * honey_number
        honey.rect.x = honey.x
        honey.rect.y = honey.rect.height + 2 * honey.rect.height * row_number
        self.honeyes.add(honey)

    def _update_bees(self):
        """Обновляет позиции и убирает старые позиции"""
        self.bees.update()
        # Удаление улетевших пчёл
        for bee in self.bees.copy():
            if bee.rect.bottom <= 0:
                self.bees.remove(bee)
        # print(len(self.bees))

    def _update_screen(self):
        # При каждом проходе цикла прорисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.vinni.blitme()
        for bee in self.bees.sprites():
            bee.draw_bee()

        self.honeyes.draw(self.screen)
        # Отображается последнее окно
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    bh = BearHoney()
    bh.run_game()

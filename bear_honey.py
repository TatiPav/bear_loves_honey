import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        # Для подсчёта результатов
        self.stats = GameStats
        self.sb = Scoreboard(self)

        self.vinni = Vinni(self)
        # Создаём группу
        self.bees = pygame.sprite.Group()
        self.honey_s = pygame.sprite.Group()

        self._create_shelf()

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Запускаем основной цикл игры, управляем обновленем экрана"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.vinni.update()
                self._update_bees()
                self._update_honey_s()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_botton(mouse_pos)

    def _check_play_botton(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Сброс игровых настроек при новой игре
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_vinni_s()

            self.honey_s.empty()
            self.bees.empty()

            self._create_shelf()
            self.vinni.center_vinni()

            pygame.mouse.set_visible(False)

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
        if len(self.bees) < self.settings.bees_allowed:
            new_bee = Bee(self)
            self.bees.add(new_bee)

    def _update_bees(self):
        """Обновляет позиции и убирает старые позиции"""
        self.bees.update()
        # Удаление улетевших пчёл
        for bee in self.bees.copy():
            if bee.rect.bottom <= 0:
                self.bees.remove(bee)

        self._check_bee_honey_collisions()

    def _check_bee_honey_collisions(self):
        # Проверяем попадание и удаляем пчелу и банку
        collisions = pygame.sprite.groupcollide(self.bees, self.honey_s, True, True)

        if collisions:
            for honey_s in collisions.values():
                self.stats.score += self.settings.honey_points * len(honey_s)
            self.sb.prep_score()
            self.check_high_score()

        if not self.honey_s:
            # Удаление существующих банок и создание новых
            self.bees.empty()
            self._create_shelf()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _update_honey_s(self):
        self._check_shelf_edges()
        self.honey_s.update()

        # Проверка столкновений между медвежонком и банкой
        if pygame.sprite.spritecollideany(self.vinni, self.honey_s):
            self._vinni_hit()

        self._check_honey_s_botton()

    def _check_honey_s_botton(self):
        """Проверка - появились ли медовые банки внизу"""
        screen_rect = self.screen.get_rect()
        for honey in self.honey_s.sprites():
            if honey.rect.bottom >= screen_rect.bottom:
                self._vinni_hit()
                break

    def _vinni_hit(self):
        """Обработка столкновения"""
        if self.stats.vinni_s_left > 0:
            self.stats.vinni_s_left -= 1
            self.sb.prep_vinni_s()

            # Очищаем список банок и мёда
            self.honey_s.empty()
            self.bees.empty()

            self._create_shelf()
            self.vinni.center_vinni()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_shelf(self):
        # Создание полок для мёда
        honey = Honey(self)
        honey_width, honey_height = honey.rect.size
        available_space_x = self.settings.screen_width - (2 * honey_width)
        number_honey_s_x = available_space_x // (2 * honey_width)

        # Расчитываем возможное к-во полок на экране
        vinni_height = self.vinni.rect.height
        available_space_y = (self.settings.screen_height - (3 * honey_height) - vinni_height)
        number_rows = available_space_y // (2 * honey_height)

        for row_number in range(number_rows):
            # Создание первой полки банок с мёдом
            for honey_number in range(number_honey_s_x):
                self._create_honey(honey_number, row_number)

    def _create_honey(self, honey_number, row_number):
        # Создание банки с мёдом и размещение её в ряду
        honey = Honey(self)
        honey_width, honey_height = honey.rect.size
        honey.x = honey_width + 2 * honey_width * honey_number
        honey.rect.x = honey.x
        honey.rect.y = honey.rect.height + 2 * honey.rect.height * row_number
        self.honey_s.add(honey)

    def _check_shelf_edges(self):
        """Реагирует при достижении края экрана"""
        for honey in self.honey_s.sprites():
            if honey.check_edges():
                self._change_shelf_direction()
                break

    def _change_shelf_direction(self):
        """Опускает все банки и меняет направление"""
        for honey in self.honey_s.sprites():
            honey.rect.y += self.settings.shelf_drop_speed
        self.settings.shelf_direction *= -1

    def _update_screen(self):
        # При каждом проходе цикла прорисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.vinni.blitme()
        for bee in self.bees.sprites():
            bee.draw_bee()
        self.honey_s.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # Отображается последнее окно
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    bh = BearHoney()
    bh.run_game()

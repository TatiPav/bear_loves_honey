import pygame
from pygame.sprite import Sprite

class Bee(Sprite):
    """Этот класс управляет пчёлами, выпускаемыми медвежонком"""
    def __init__(self, bh_game):
        """Создаёт пчёл в текущем местонахождении медвежонка"""
        super().__init__()
        self.screen = bh_game.screen
        self.settings = bh_game.settings

        self.image = pygame.image.load('images/bee.bmp')
        self.rect = self.image.get_rect()

        # Создание пчелы в начальной позиции (0, 0) и назначение правильной позиции
        # (она зависит от позиции медвежонка)

        self.rect.midtop = bh_game.vinni.rect.midtop

        # Позиция пчелы сохраняется в вещественном формате
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает пчелу вверх по экрану"""
        # Обновление позиции пчелы
        self.y -= self.settings.bee_speed
        # Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bee(self):
        """Вывод пчелы на экран"""

        # self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, self.rect)


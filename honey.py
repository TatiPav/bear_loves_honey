import pygame
from pygame.sprite import Sprite

class Honey(Sprite):
    """Единица мёда"""
    def __init__(self, bh_game):
        """Задаёт начальную позицию продукту"""
        super().__init__()
        self.screen = bh_game.screen
        self.settings = bh_game.settings

        # Загрузка изображениея и задание назначение атрибута rect
        self.image = pygame.image.load('images/honey.bmp')
        self.rect = self.image.get_rect()

        # Новые банки с мёдом появляются в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохраняем точную горизонтальную позицию
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если банка у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # Перемещение влево или вправо
        self.x += (self.settings.honey_speed * self.settings.shelf_direction)
        self.rect.x = self.x

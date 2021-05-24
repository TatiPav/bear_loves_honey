import pygame
from pygame.sprite import Sprite

class Honey(Sprite):
    """Единица мёда"""
    def __init__(self, bh_game):
        """Задаёт начальную позицию продукту"""
        super().__init__()
        self.screen = bh_game.screen

        # Загрузка изображениея и задание назначение атрибута rect
        self.image = pygame.image.load('images/honey.bmp')
        self.rect = self.image.get_rect()

        # Новые банки с мёдом появляются в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохраняем точную горизонтальную позицию
        self.x = float(self.rect.x)
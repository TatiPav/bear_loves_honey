import pygame

class Vinni:
    """Этот класс управляет медвежонком"""

    def __init__(self, bh_game):
        """Инициализирует медвежонка и задаёт ему начальную позицию"""
        self.screen = bh_game.screen
        self.screen_rect = bh_game.screen.get_rect()

        # Загружает изображение медвежонка и получает прямоугольник
        self.image = pygame.image.load('images/vi.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый медвежонок появляется в центре нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует медвежонка в текущей позиции"""
        self.screen.blit(self.image, self.rect)

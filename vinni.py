import pygame

class Vinni:
    """Этот класс управляет медвежонком"""

    def __init__(self, bh_game):
        """Инициализирует медвежонка и задаёт ему начальную позицию"""
        self.screen = bh_game.screen
        self.settings = bh_game.settings
        self.screen_rect = bh_game.screen.get_rect()

        # Загружает изображение медвежонка и получает прямоугольник
        self.image = pygame.image.load('images/vi.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый медвежонок появляется в центре нижнего края экрана
        # self.rect.midbottom = self.screen_rect.midbottom
        # Каждый новый медвежонок появляется в центре экрана
        self.rect.center = self.screen_rect.center
        # Сохранение вещественной координаты цента медвежонка
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Определяем перемещение Флаг
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """С учётом флага происходит обновление позиции"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.vinni_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.vinni_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.vinni_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.vinni_speed

        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """Рисует медвежонка в текущей позиции"""
        self.screen.blit(self.image, self.rect)

import sys
import pygame

class BearHoney:
    """Класс для управления игрой"""
    def __init__(self):
        """Создаётся игра"""
        pygame.init()
        """Создаём окно для прорисовки графических элементов - кортеж для размера экрана"""
        self.screen = pygame.display.set_mode((500, 300))
        pygame.display.set_caption("Мишки любят мёд")
        # Настраиваем цвет экрана
        self.bg_color = (230, 210, 210)

    def run_game(self):
        """Запускаем основной цикл игры, управляем обновленем экрана"""
        while True:
           # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            # Отображается последнее окно
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    bh = BearHoney()
    bh.run_game()
class Settings:
    """В этом классе хранятся все настройки игры Мишки любят мёд"""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.vinni_speed = 1.5

        # Параметры пчелы
        self.bee_speed = 2
        self.bee_allowed = 3

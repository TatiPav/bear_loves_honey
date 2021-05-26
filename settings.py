class Settings:
    """В этом классе хранятся все настройки игры Мишки любят мёд"""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.vinni_speed = 10
        self.vinni_limit = 3

        # Параметры пчелы
        self.bee_speed = 1.5
        self.bees_allowed = 3

        # Настройка банок с мёдом
        self.honey_speed = 1.0
        self.shelf_drop_speed = 10
        # Ниже движение 1 вправо, -1 влево
        self.shelf_direction = 1

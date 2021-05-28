class Settings:
    """В этом классе хранятся все настройки игры Мишки любят мёд"""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.vinni_limit = 3

        # Параметры пчелы
        self.bees_allowed = 3

        # Настройка банок с мёдом
        self.shelf_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.vinni_speed_factor = 1.5
        self.bee_speed_factor = 1.5
        self.honey_speed_factor = 1.0
        # Ниже движение 1 вправо, -1 влево
        self.shelf_direction = 1
        # Подсчёт очков
        self.honey_points = 50
        """Для увеличения скорости"""
    def increase_speed(self):
        self.vinni_speed_factor *= self.speedup_scale
        self.bee_speed_factor *= self.speedup_scale
        self.honey_speed_factor *= self.speedup_scale
        self.honey_points = int(self.honey_points * self.score_scale)
        # print(self.honey_points)
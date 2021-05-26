class GameResult:
    def __init__(self, bh_game):
        """Подсчёт результатов"""
        self.settings = bh_game.settings
        self.reset_result()

        # Игра в активном состоянии

        self.game_active = True

    def reset_result(self):
        """Создаёт изменение результатов"""
        self.vinnis_left = self.settings.vinni_limit


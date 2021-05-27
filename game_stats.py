class GameStats:
    def __init__(self, bh_game):
        """Подсчёт результатов"""
        self.settings = bh_game.settings
        self.reset_stats()

        # Игра в неактивном состоянии

        self.game_active = False

    def reset_stats(self):
        """Создаёт изменение результатов"""
        self.vinni_s_left = self.settings.vinni_limit

class Score():
    """Отслеживание статистики игры"""

    def __init__(self):
        """Инициализация статистики"""
        self.reset_score()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_score(self):
        """Статистика, изменяющаяся во время игры"""
        self.guns_left = 3
        self.score = 0

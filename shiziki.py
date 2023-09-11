import pygame


class Shizik(pygame.sprite.Sprite):
    """Класс одного Шизика"""

    def __init__(self, screen):
        """Инициализация и задание начальной позиции"""
        super(Shizik, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('photo/Ino_2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Вывод Шизика на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self, score):
        """Перемещение Шизиков"""
        """Ускорение Шизиков +1000"""
        self.y += 0.5
        self.rect.y = self.y


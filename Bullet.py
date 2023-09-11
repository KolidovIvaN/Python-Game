"""Класс для создания пуль"""

import pygame

class Bullet1(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Создание пули в позиции пушки"""
        super(Bullet1, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 5, 5, 15)
        self.color = (150, 150, 150)
        self.speed = 10
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем пули на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)

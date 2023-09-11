"""Класс для создания пушки"""
import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):
        """Инициалищация пушки"""
        super(Gun, self).__init__()
        self.display = screen
        self.image = pygame.image.load('Photo/Guns/Spaceship_1.png')
        self.rect = self.image.get_rect()
        self.x_rect = self.rect.centerx
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """Рисование пушки"""
        self.display.blit(self.image, self.rect)

    def update_gun(self):
        """Обновление позиции пушки"""
        with open('speed.txt', 'r') as f:
            self.speed = float(f.readline())
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.mleft and self.rect.left > 0:
            self.center -= self.speed
        self.rect.centerx = self.center

    def create_gun(self):
        """Размещение пушки по центру экрана"""
        self.center = self.screen_rect.centerx

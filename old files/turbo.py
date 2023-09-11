import pygame


class Turbo(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Turbo, self).__init__()
        """Инициализация бонуса турбо"""
        self.screen = screen
        self.image = pygame.image.load('Photo/Bonuses/turbo_2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

    def draw(self):
        """Рисование бонуса на экран"""
        self.screen.blit(self.image, self.rect)

    def update_turbo(self):
        """Перемещение бонуса"""
        self.y += 2
        self.rect.y = self.y
        self.rect.centerx = self.center




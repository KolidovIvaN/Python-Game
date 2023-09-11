import pygame


class Rocket(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Rocket, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Photo/Guns/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def draw_rocket(self):
        self.screen.blit(self.image, self.rect)

    def update_rocket(self):
        self.y -= 2



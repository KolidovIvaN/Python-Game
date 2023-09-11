import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():
    """вывод игровой информации"""

    def __init__(self, screen_all, score):
        """инициализация подсчета очков"""
        self.screen = screen_all
        self.screen_rect = screen_all.get_rect()
        self.score = score
        self.text_color = (217, 128, 138)  # (171, 38, 54)  #(235, 120, 154)
        self.font = pygame.font.Font('./Fonts/Baron Neue.otf', 50)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        """преобразование текста счета в граф. изображ."""
        self.score_img = self.font.render(str(self.score.score), True, self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 290
        self.score_rect.top = 475

    def image_high_score(self):
        """Рекорд на экран"""
        self.high_score_image = self.font.render(str(self.score.high_score), True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 290
        self.high_score_rect.top = 615

    def image_guns(self):
        """Количество жизней"""
        self.guns = Group()
        for gun_number in range(self.score.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 910 + gun_number * gun.rect.width * 1.3
            gun.rect.y = 690
            self.guns.add(gun)

    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)

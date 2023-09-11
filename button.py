"""Класс для создания кнопок в игровом меню"""
import pygame

pygame.init()

button_sound = pygame.mixer.Sound('Sounds/sound_button.wav')
pygame.mixer.Sound.set_volume(button_sound, 1)


class Button():

    def __init__(self, width, height, screen, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color #(255, 255, 255)
        self.active_color = active_color #(230, 230, 0)
        self.screen = screen

    def draw(self, x, y, message, size, color_text, x0, y0, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button_font = pygame.font.Font('./Fonts/Baron Neue.otf', size)
        button_text = button_font.render(message, True, pygame.Color(color_text))
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))
            if click[0] == 1:
                button_sound.play()
                pygame.time.delay(400)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()

        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))

        self.screen.blit(button_text, (x + x0, y - y0))

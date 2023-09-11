# Главный файл игры. Здесь описывается главное меню игры, описание правил и тд.
import pygame
import pygame, sys, time
from button import Button
from controls import run


RES_BG = (1366, 800)
font = pygame.font.Font('./Fonts/Rules.ttf', 30)
color_inactive = (254, 230, 170)  # (13, 36, 69)
color_active = (183, 73, 38)
shot = pygame.mixer.Sound('Sounds/Shot.wav')
pygame.mixer.Sound.set_volume(shot, 0.2)


def game_menu():
    pygame.font.init()
    pygame.mixer.music.load('Sounds/Background_sound.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0)  # Громкость музыки
    screen_menu = pygame.display.set_mode(RES_BG)
    icon_game = pygame.image.load('Photo/Icon_2.png')
    background_game = pygame.image.load('Photo/Background/background mein menu.jpg').convert()
    pygame.display.set_caption('Skywalker\'s War')
    pygame.display.set_icon(icon_game)
    menu_name_font = pygame.font.Font('./Fonts/Baron Neue.otf', 70)
    mein_menu = menu_name_font.render('MEIN MENU', True, (255, 255, 255))
    beta_font = pygame.font.Font('./Fonts/Baron Neue.otf', 15)
    beta = beta_font.render('Beta 3.2.5', True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen_menu.blit(background_game, (0, 0))
        screen_menu.blit(mein_menu, (850, 100))
        screen_menu.blit(beta, (10, 8))

        size = 60
        # Создание кнопки
        # Start Game
        button_start_game = Button(475, 80, screen_menu, color_inactive, color_active)
        button_start_game.draw(820, 210, 'START GAME', size, 'black', 70, -12, run)

        # Создание кнопки
        # Options
        button_options = Button(475, 80, screen_menu, color_inactive, color_active)
        button_options.draw(820, 320, 'OPTIONS', size, 'black', 130, -12, options)

        # Создание кнопки
        # Tutorials
        button_tutorials = Button(475, 80, screen_menu, color_inactive, color_active)
        button_tutorials.draw(820, 430, 'TUTORIALS', size, 'black', 92, -12, tutorials)

        # Создание кнопки
        # Creator
        button_creator = Button(475, 80, screen_menu, color_inactive, color_active)
        button_creator.draw(820, 540, 'CREATOR', size, 'black', 115, -12, creator)

        # Создание кнопки
        # Quit
        button_quit = Button(475, 80, screen_menu, color_inactive, color_active)
        button_quit.draw(820, 650, 'EXIT GAME', size, 'black', 90, -12, quit)

        # Создание кнопки
        # Music
        # button_options = Button(100, 55, screen_menu, color_inactive, color_active)
        # button_options.draw(1150, 30, 'Music', 35, 'black', music)

        pygame.display.flip()


def options():
    pygame.font.init()
    screen_menu = pygame.display.set_mode(RES_BG)
    icon_game = pygame.image.load('Photo/Icon_2.png')
    background_game = pygame.image.load('Photo/Background/Options_background.jpg').convert()
    pygame.display.set_caption('Skywalker\'s War')
    pygame.display.set_icon(icon_game)
    beta_font = pygame.font.Font('./Fonts/Baron Neue.otf', 15)
    beta = beta_font.render('Beta 3.2.5', True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen_menu.blit(background_game, (0, 0))
        screen_menu.blit(beta, (10, 8))

        # Создание кнопки
        # Main menu
        button_options = Button(160, 50, screen_menu, color_inactive, color_active)
        button_options.draw(1180, 700, 'Main Menu', 25, 'black', 5, -13, game_menu)

        pygame.display.flip()


def creator():
    pygame.font.init()
    screen_menu = pygame.display.set_mode(RES_BG)
    icon_game = pygame.image.load('Photo/Icon_2.png')
    background_game = pygame.image.load('Photo/Background/background creator.jpg').convert()
    pygame.display.set_caption('Skywalker\'s War')
    pygame.display.set_icon(icon_game)
    beta_font = pygame.font.Font('./Fonts/Baron Neue.otf', 15)
    beta = beta_font.render('Beta 3.2.5', True, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen_menu.blit(background_game, (0, 0))
        screen_menu.blit(beta, (10, 8))

        # Создание кнопки
        # Main menu
        button_options = Button(160, 50, screen_menu, color_inactive, color_active)
        button_options.draw(1150, 700, 'Main Menu', 25, 'black', 5, -13, game_menu)

        pygame.display.flip()


def tutorials():
    pygame.font.init()
    screen_menu = pygame.display.set_mode(RES_BG)
    icon_game = pygame.image.load('Photo/Icon_2.png')
    background_game = pygame.image.load('Photo/Background/background tutorials.jpg').convert()
    pygame.display.set_caption('Skywalker\'s War')
    pygame.display.set_icon(icon_game)
    beta_font = pygame.font.Font('./Fonts/Baron Neue.otf', 15)
    beta = beta_font.render('Beta 3.2.5', True, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen_menu.blit(background_game, (0, 0))
        screen_menu.blit(beta, (10, 8))

        # Создание кнопки
        # Main menu
        button_options = Button(160, 50, screen_menu, color_inactive, color_active)
        button_options.draw(1150, 700, 'Main Menu', 25, 'black', 5, -13, game_menu)

        pygame.display.flip()


def music():
    pygame.mixer.music.stop()


game_menu()

import pygame, sys, time
from button import Button
from Bullet import Bullet1
from shiziki import Shizik
from gun import Gun
from pygame.sprite import Group
from score import Score
from score_2 import Scores

"""
from bonus import Bonuses
from random import randint
"""

pygame.init()
RES_BG = (1400, 800)
font = pygame.font.Font('./Fonts/Rules.ttf', 30)
color_inactive = (254, 230, 170)
color_active = (183, 73, 38)
# shot = pygame.mixer.Sound('Sounds/Shot.wav')
# pygame.mixer.Sound.set_volume(shot, 0.1)
# pygame.time.set_timer(pygame.USEREVENT, 2000)
shot = pygame.mixer.Sound('Sounds/Shot.wav')
pygame.mixer.Sound.set_volume(shot, 0.05)
crash = pygame.mixer.Sound('Sounds/crash.wav')
pygame.mixer.Sound.set_volume(crash, 0.2)
game_over_sound = pygame.mixer.Sound('Sounds/Game_over.wav')
pygame.mixer.Sound.set_volume(game_over_sound, 0.3)


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
        screen_menu.blit(mein_menu, (877, 95))
        screen_menu.blit(beta, (10, 8))

        size = 60
        # Создание кнопки
        # Start Game
        button_start_game = Button(475, 80, screen_menu, color_inactive, color_active)
        button_start_game.draw(848, 210, 'START GAME', size, 'black', 70, -12, run)

        # Создание кнопки
        # Options
        button_options = Button(475, 80, screen_menu, color_inactive, color_active)
        button_options.draw(848, 320, 'OPTIONS', size, 'black', 130, -12, options)

        # Создание кнопки
        # Tutorials
        button_tutorials = Button(475, 80, screen_menu, color_inactive, color_active)
        button_tutorials.draw(848, 430, 'TUTORIALS', size, 'black', 92, -12, tutorials)

        # Создание кнопки
        # Creator
        button_creator = Button(475, 80, screen_menu, color_inactive, color_active)
        button_creator.draw(848, 540, 'CREATOR', size, 'black', 115, -12, creator)

        # Создание кнопки
        # Quit
        button_quit = Button(475, 80, screen_menu, color_inactive, color_active)
        button_quit.draw(848, 650, 'EXIT GAME', size, 'black', 90, -12, quit)

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
    photo_spaceship = pygame.image.load('Photo/Guns/Spaceship_1.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen_menu.blit(background_game, (0, 0))
        screen_menu.blit(beta, (10, 8))
        screen_menu.blit(photo_spaceship, (660, 640))

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


def run():
    FPS = 160
    pygame.font.init()
    pygame.init()  # инитиализируем
    pygame.mixer.music.load('sounds/Variant_2.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0)
    screen_all = pygame.display.set_mode((1400, 800))
    screen = pygame.Surface((700, 770))  # создаем экран
    pygame.display.set_caption('Skywalker\'s War')  # название приложения
    image_icon = pygame.image.load('photo/Icon_2.png')  # импорт фото иконки приложения
    pygame.display.set_icon(image_icon)  # создание иконки приложения
    bg_screen = pygame.image.load('Photo/Background/GameBackground_2.jpg').convert()
    bg_all = pygame.image.load('Photo/Background/GameBackground.jpg').convert()
    main_font = pygame.font.Font('./Fonts/Baron Neue.otf', 70)
    main_font_score = pygame.font.Font('./Fonts/Baron Neue.otf', 45)
    title_game = main_font.render('Skywalker\'s War', True, pygame.Color(203, 198, 176))
    game_score = main_font_score.render('SCORE:', True, pygame.Color(233, 161, 90))
    game_record = main_font_score.render('RECORD:', True, pygame.Color(233, 161, 90))
    gun = Gun(screen)  # вызов пушки из файла Gun на экран
    bullets = Group()
    shiziki = Group()
    army_shiziki(screen, shiziki)
    score = Score()
    sc = Scores(screen_all, score)
    clock = pygame.time.Clock()

    """""
    bonuses_images = ['Turbo.png', 'Shield.png', 'Bullets.png']
    bonuses_surface = [pygame.image.load('Photo/Bonuses/' + path).convert_alpha() for path in bonuses_images]
    bonuses = pygame.sprite.Group()

    def createBonuses(group):
        x = randint(35, 700)
        speed = randint(1, 4)
        return Bonuses(x, bonuses_surface[indx], speed, group)

    def collideBonuses():
        for bonus in bonuses:
            if gun.rect.collidepoint(bonus.rect.center):
                bonus.kill()
                if indx == 0:
                    with open('speed.txt', 'w') as f:
                        f.write(str(float(5.0)))
    """

    # Основной цикл программы:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # выход из приложения
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:  # передвижение пушки вправо
                    gun.mright = True
                elif event.key == pygame.K_a:  # передвижение пушки влево
                    gun.mleft = True
                elif event.key == pygame.K_SPACE:  # стрельба из пушки
                    new_bullet = Bullet1(screen, gun)
                    bullets.add(new_bullet)
                    shot.play()
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    pause(screen_all)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    gun.mright = False
                elif event.key == pygame.K_a:
                    gun.mleft = False
            """""        
            if event.type == pygame.USEREVENT:
                indx = randint(0, len(bonuses_surface) - 1)
                createBonuses(bonuses)
            """

        # collideBonuses()
        screen_all.blit(bg_all, (0, 0))
        screen_all.blit(screen, (40, 10))
        screen.blit(bg_screen, (0, 0))
        screen_all.blit(title_game, (760, 50))
        screen_all.blit(game_score, (965, 415))
        screen_all.blit(game_record, (965, 545))
        # bonuses.draw(screen_all)

        if score.run_game:
            gun.update_gun()
            bullets.update()
            update(bg_screen, screen, gun, sc, shiziki, bullets)
            update_bullets(screen, shiziki, score, sc, bullets)
            update_shiziki(screen_all, score, screen, sc, gun, shiziki, bullets, bg_all)
            # bonuses.update(800)
            pygame.display.update()
            clock.tick(FPS)

        pygame.display.update()
        clock.tick(FPS)


def pause(screen):
    pygame.font.init()
    pause_font = pygame.font.Font('./Fonts/Baron Neue.otf', 75)
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # выход из приложения
                sys.exit()

        pygame.mixer.music.stop()
        pause_text = pause_font.render('Paused. Press Enter To Continue', True, pygame.Color('red'), (200, 149, 99))
        screen.blit(pause_text, (50, 330))

        button_options = Button(475, 80, screen, color_inactive, color_active)
        button_options.draw(480, 500, 'MEIN MENU', 65, 'black', 50, -12, game_menu)

        button_options = Button(475, 80, screen, color_inactive, color_active)
        button_options.draw(480, 620, 'EXIT GAME', 65, 'black', 70, -12, quit)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            pygame.mixer.music.load('sounds/Variant_2.mp3')
            pygame.mixer.music.play(-1)
            paused = False

        pygame.display.update()


def update(bg_screen, screen, gun, sc, shiziki, bullets):
    """Обновление экрана"""
    screen.blit(bg_screen, (0, 0))  # закрашиваение экрана в нужный цвет
    sc.show_score()
    for bullet in bullets.sprites():  # отрисовка пуль
        bullet.draw_bullet()
    gun.output()  # отображение пушки на экране
    shiziki.draw(screen)
    pygame.display.flip()


def update_bullets(screen, shiziki, score, sc, bullets):
    """Обновление позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, shiziki, True, True)  # словарь
    if collisions:
        for shiziki in collisions.values():
            score.score += 10 * len(shiziki)
        sc.image_score()
        check_high_score(score, sc)
        sc.image_guns()
    if len(shiziki) == 0:
        bullets.empty()
        army_shiziki(screen, shiziki)


def gun_kill(screen_all, score, screen, sc, gun, shiziki, bullets, bg_all):
    """Столкновение пушки с армией Шизиков"""
    pygame.font.init()
    game_over_font = pygame.font.Font('./Fonts/Baron Neue.otf', 150)
    game_over = game_over_font.render('GAME OVER', True, pygame.Color('red'))
    if score.guns_left > 1:
        score.guns_left -= 1
        crash.play()
        sc.image_guns()
        shiziki.empty()
        bullets.empty()
        army_shiziki(screen, shiziki)
        gun.create_gun()
        time.sleep(2)
    else:
        score.run_game = False
        game_over_sound.play()
        pygame.mixer.music.stop()
        game_over_sound.play()
        screen_game_over(screen_all, bg_all, game_over)


def update_shiziki(screen_all, score, screen, sc, gun, shiziki, bullets, bg_all):
    """Обновление позиции Шизиков"""
    shiziki.update(score)
    if pygame.sprite.spritecollideany(gun, shiziki):
        gun_kill(screen_all, score, screen, sc, gun, shiziki, bullets, bg_all)
    shiziki_check(score, screen, sc, gun, shiziki, bullets, screen_all, bg_all)


def shiziki_check(score, screen, sc, gun, shiziki, bullets, screen_all, bg_all):
    """Проверка армии до конца экрана"""
    screen_rect = screen.get_rect()
    for shizik in shiziki.sprites():
        if shizik.rect.bottom >= screen_rect.bottom:
            gun_kill(screen_all, score, screen, sc, gun, shiziki, bullets, bg_all)


def army_shiziki(screen, shiziki):
    """Создание армии Шизиков"""
    shizik = Shizik(screen)
    shizik_width = shizik.rect.width
    numder_shizik_x = int((700 - 2 * shizik_width) / shizik_width)
    shizik_height = shizik.rect.height + 5
    number_shizik_y = int((680 - 250 - 2 * shizik_height) / shizik_height)

    for row_number in range(number_shizik_y):
        for shizik_numder in range(numder_shizik_x):
            shizik = Shizik(screen)
            shizik.x = shizik_width + shizik_width * shizik_numder
            shizik.y = shizik_height + shizik_height * row_number
            shizik.rect.x = shizik.x
            shizik.rect.y = shizik.rect.height + shizik.rect.height * row_number
            shiziki.add(shizik)


def check_high_score(score, sc):
    """проверка рекорда"""
    if score.score > score.high_score:
        score.high_score = score.score
        sc.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(score.high_score))


def screen_game_over(screen_all, bg_all, game_over):
    """Создание экрана "Game Over" после истечения всех жизней"""
    restart_menu = True
    while restart_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen_all.blit(bg_all, (0, 0))
        screen_all.blit(game_over, (275, 200))
        pygame.mixer.music.stop()

        # Создание кнопки для перезапуска игры
        button_options = Button(475, 80, screen_all, color_inactive, color_active)
        button_options.draw(445.5, 380, 'RESTART GAME', 65, 'black', 12, -12, run)
        # Создание кнопки для выхода из игры
        button_options = Button(475, 80, screen_all, color_inactive, color_active)
        button_options.draw(445.5, 500, 'MEIN MENU', 65, 'black', 50, -12, game_menu)

        button_options = Button(475, 80, screen_all, color_inactive, color_active)
        button_options.draw(445.5, 620, 'EXIT GAME', 65, 'black', 70, -12, quit)

        pygame.display.flip()


game_menu()

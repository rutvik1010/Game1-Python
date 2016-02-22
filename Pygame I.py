import pygame
import random
import time

pygame.init()
display_width = 1080
display_height = 720
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0,255,0)
crash_sound = pygame.mixer.Sound("Smashing-Yuri_Santana-1233262689.wav")
pygame.mixer.music.load("Piano_Desire.wav")
g_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hungry Jack")
clock = pygame.time.Clock()
manimg = pygame.image.load("character-color.png")


def text_object(text, font,color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def credits_object(text,font):
    cre_surf = font.render(text, True, white)
    return cre_surf, cre_surf.get_rect()

def game_credits(text):
    credits_font = pygame.font.SysFont("comicsansms", 15)
    credits_surf, credits_rect = credits_object(text, credits_font)
    credits_rect.center = (80, 10)
    g_display.blit(credits_surf, credits_rect)


def buttons(boxcolor,textcolor, x, y, w, h, text):
        pygame.draw.rect(g_display, white, (x, y, w, h))
        smalltext = pygame.font.SysFont("comicsansms", 20)
        smalltext_surf, smalltext_rect = text_object(text, smalltext, textcolor)
        smalltext_rect.center = ((x + (w/2)), y + (h/2))
        g_display.blit(smalltext_surf, smalltext_rect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        titlefont = pygame.font.SysFont("comicsansms", 100)
        titlesurface, titlerectangle = text_object("Space Ball 3D", titlefont, red)
        titlerectangle.center = ((display_width/2), (display_height/2))
        g_display.blit(titlesurface, titlerectangle)
        game_credits("Created by: Rutvik")
        buttons(white,red, 200, 600, 100, 50, "Play!")
        buttons(white,red, 880, 600, 100, 50, "Quit")
        mousepos = pygame.mouse.get_pos()
        mouseclick = pygame.mouse.get_pressed()
        if 200 < mousepos[0] < 300 and 600 < mousepos[1] < 650:
            if mouseclick[0] ==1:
                g_loop()
        elif 880 < mousepos[0] < 980 and 600 < mousepos[1] < 650:
            if mouseclick[0] ==1:
                pygame.quit()
                quit()
        pygame.display.update()


def message_box(text):
    textfont = pygame.font.SysFont("comicsansms", 60)
    textsurf, textrect = text_object(text, textfont, white)
    textrect.center = ((display_width/2), (display_height/2))
    g_display.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    g_display.fill(black)
    pygame.display.flip()


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_box("You Crashed!")

def screen_limit_message():
    message = pygame.font.SysFont(None, 30)
    display_message = message.render("You reached the screen limit", True, white)
    g_display.blit(display_message, (420, 0))

def display_score(count):
    font_size = pygame.font.SysFont("comicsansms", 30)
    text = font_size.render("Score: " + str(count), True, red)
    g_display.blit(text, (20, 20))


def things(thingx, thingy, thingwidth, thingheight,thingcolor):
    pygame.draw.rect(g_display, thingcolor, [thingx, thingy, thingwidth, thingheight])


def createman(x, y):
    g_display.blit(manimg, (x, y))




def g_loop():
    pygame.mixer.music.play(-1)
    x = (display_width * 0.4)
    y = (display_height * 0.4)
    x_change = 0
    y_change = 0
    thing_starty = random.randrange(0, display_height)
    thing_startx = 1280
    thing_speed = -7
    thing_width = 50
    thing_height = 50
    score_count = 0
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_LEFT:
                    x_change = - 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x += x_change
        y += y_change
        g_display.fill(black)

# GENERATING OBJECTS ON THE SCREEN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        things(thing_startx, thing_starty, thing_width, thing_height, white)
        thing_startx += thing_speed
        createman(x, y)
        display_score(score_count)

# SCREEN BOUNDARIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if (x + 340) > display_width or x < -200:
                screen_limit_message()
        if (y + 195) > display_height or y + 35 < 0:
                screen_limit_message()

# GENERATING N NUMBER OF BLOCKS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if thing_startx + thing_width < 0:
            thing_startx = 1280
            thing_starty = random.randrange(0,display_height)
            score_count += 1
            thing_speed -= 1

# DETECTING COLLISION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if  (x+200) < thing_startx and (x+340) >= thing_startx: # stops printing when the object passes the man
            if thing_starty > y and thing_starty < y + 195:
                crash()
                game_intro()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    game_intro()

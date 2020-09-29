# -*- coding: UTF-8 -*-
# Pygame-Modul importieren.

import pygame

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

def main():

    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    imgBack = pygame.image.load ("/home/saiboto/saiboto_data/Bilder/space2.jpg")
    imgSurf = pygame.image.load ("/home/saiboto/saiboto_data/Bilder/Astro2.png")

    #pygame.transform.flip(imgSurf, True, True)

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
    pygame.display.set_caption("Lost in Space")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()

    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    running = True
    x = 0
    y = 0
    speedX = 2
    speedY = 2

    angle_deg = 0

    #forward = True
    #down = True

    while running:

        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(60)

        # screen-Surface mit Schwarz (RGB = 0, 0, 0) füllen.
        screen.fill((0, 0, 0))
        screen.blit (imgBack, (0, 0))
        image_rotated = pygame.transform.rotate(imgSurf, angle_deg)
        width_rotated = image_rotated.get_width()
        height_rotated = image_rotated.get_height()
        angle_deg += 0.4
        screen.blit (image_rotated, (x, y))
        x += speedX
        y += speedY
        if x > width - width_rotated:
            speedX = -2
        if x < 0:
            speedX = 2
        if y > height - height_rotated:
            speedY = -2
        if y < 0:
            speedY = 2
        '''
        if forward == True:
            x += 1
        else:
            x -= 1
        if x < 0:
            forward = True

        if x > 300:
            forward = False

        if down == True:
            y +=1
        else:
            y -=1
        if y < 0:
            down = True

        if y > 200:
            down = False
            #y += 2
        '''

        # Alle aufgelaufenen Events holen und abarbeiten.
        #################### BEGIN Event processing loop #################
        for event in pygame.event.get():

            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                print("X gedrückt!")
                running = False

            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:

                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:

                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        #################### END Event processing loop #################
        # Inhalt von screen anzeigen.
        pygame.display.flip()

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':

    # Unsere Main-Funktion aufrufen.
    main()

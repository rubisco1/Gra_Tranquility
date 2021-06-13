while True:
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

OKNOGRY.fill((0, 0, 0))
rysuj_plansze()
rysuj_pole_gry()
if WYGRANA:
    drukuj_wynik(WYGRANY)
elif WYGRANA is False:
    print ("Przegrałeś")

pygame.display.update()



while True:
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if WYGRANA is False:
            if RUCH == 1:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # jeżeli naciśnięto 1. przycisk
                        mouseX, mouseY = event.pos 
                        # wylicz indeks klikniętego pola
                        pole = (int(mouseY / 50) * 3) + int(mouseX / 50)
                        RUCH = postaw_znak(pole, RUCH)
            elif RUCH == 2:
                RUCH = ai_ruch(RUCH)

            WYGRANY = kto_wygral()
            if WYGRANY is not None:
                WYGRANA = True

    OKNOGRY.fill((0, 0, 0))
    rysuj_plansze()
    rysuj_pole_gry()
    if WYGRANA:
        drukuj_wynik(WYGRANY)
    pygame.display.update()

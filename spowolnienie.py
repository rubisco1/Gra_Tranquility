from datetime import datetime, timedelta

#ta funkcja będzie uruchamiana po "zjedzeniu owocka"
def spowolnienie():
    #nwm jeszcze czy dołączymy do klasy gracz, czy owoc, czy osobna funkcja
    koniec = datetime.now() + timedelta(seconds = 30)
    while datetime.now() < koniec:#pętla będzie działać ok. 30 sekund
        for obiekt in przeciwnicy:
            #grupę wszytskich spritów nawazłam przeciwnicy, będzie ją trzeba stworzyć gdy już będzie klasa przeciwnik
            obiekt.zmiana_szybkosci()
            #trzeba będzie dododać funkcje zmiana szybkości w klasie przeciwnicy

#generalnie to zobaczymy czy ta funkcja zadziała kiedy bedą już przeciwnicy i główna pętla gry, na razie wiem, że czasowe ramy działają
 

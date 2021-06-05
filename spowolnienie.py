from datetime import datetime, timedelta

def spowolnienie():#nwm jeszcze czy dołączymy do klasy gracz, czy owoc, czy osobna funkcja
    koniec = datetime.now() + timedelta(seconds=1)
    while datetime.now() < koniec:#pętla będzie działać 30 sekund
        print("1")

spowolnienie()

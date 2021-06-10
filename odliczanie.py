#na początku dodałam jeszcze import time
# odliczanie

pygame.init()

while True:
    for event in pygame.event.get():
        # przechwyć otwarcie okna
        if event.type == START:
            pygame.start()
            sys.start()
            
def countdown(time):
    count.color('white')
    count.penup()
    count.goto(-10, 10)

for x in range(3):
    count.write(3-x, font=("Arial", 30, 'bold'))
    time.sleep(1)
    count.clear
    count.write("Start!", font=("Arial", 30, 'bold'))

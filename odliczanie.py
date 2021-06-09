#na początku dodałam jeszcze import time
# odliczanie
count.color('white')
count.penup()
count.goto(-200, 200)

for x in range(3):
    count.write(3-x, font=("Arial", 30, 'bold'))
    time.sleep(1)
    count.clear
    count.write("Start!", font=("Arial", 30, 'bold'))

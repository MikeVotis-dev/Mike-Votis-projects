#--------------------------If you want to PLAY it ,press the DOWNLOAD BUTTON---------------------------------
#--------------------------You need also to have downloaded the Python from https://www.python.org 
# For further information ASK CHAT GPT OR GEMINI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



from turtle import *
from time import sleep
from random import randint

w = 200
h = 150

t = Turtle()
t.color("red")
t.shape("turtle")
t.penup()
t.speed(0)
t.points = 0


def rand_move():
    t.goto(randint(-w, w), randint(-h, h))

def catch(x, y):
    t.points = t.points + 1
    t.clear()
    t.write('A!', font=("Arial", 14, "normal"))
    rand_move()

t.onclick(catch)

rand_move()

while t.points < 5:
    sleep(3)
    rand_move()

t.write("WOW!", font=("Arial", 16, "bold"))
t.hideturtle()

done()

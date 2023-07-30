from random import randint
from turtle import Turtle, Screen

health = 50
damage = 10
fight = randint(10, 20)
step = 0

def up():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(90)
    turtle.forward(10)

def down():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(-90)
    turtle.forward(10)

def left():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(180)
    turtle.forward(10)

def right():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(0)
    turtle.forward(10)

def combat():
    enemy = Turtle()
    enemy.up()
    eHealth = randint(20, 100)
    eDamage = randint(10, 20)

screen = Screen()
screen.setup(500, 350)  # visible portion of screen area
screen.screensize(600, 600)  # scrollable extent of screen area
turtle = Turtle()
turtle.up()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

screen.mainloop()
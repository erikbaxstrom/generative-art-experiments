from random import randint
import tkinter
from turtle import RawTurtle, TurtleScreen

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


root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.pack(side=tkinter.LEFT)
screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.up()

button = tkinter.Button(root, text="click me!", command=up)
button.pack()



# screen.onkey(up, "Up")
# screen.listen()
screen.mainloop()
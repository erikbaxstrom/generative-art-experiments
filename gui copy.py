from random import randint
import tkinter
from turtle import RawTurtle, TurtleScreen
import Plot

step = 0

def generate_preview(turtle):
    # global step
    # step += 1
    # turtle.seth(randint(0,360))
    # turtle.forward(15)
    coords = Plot.draw(turtle)
    # screen.setworldcoordinates(coords[0], coords[1], coords[2], coords[3])
    screen.setworldcoordinates(0,0,150,150)
    


window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
screen = TurtleScreen(canvas)
turtle = RawTurtle(screen)
turtle.up()
screen.tracer(0)

button = tkinter.Button(window, text="Generate Preview", command=lambda: generate_preview(turtle))
button.pack()



# screen.onkey(up, "Up")
# screen.listen()
screen.mainloop()
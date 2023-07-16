from turtle import *
import random
from math import sin, cos, pi, sqrt

setup(800, 800)
speed(0)


def drawBranch(x, y, angle, cumulative_angle, length, level, wacky):
    level -= 1
    if level == 0:
        return
    else:
        # Draw Stuff
        new_x = x + length * sin(cumulative_angle)
        new_y = y + length * cos(cumulative_angle)
        width(level/10)
        penup()
        goto(x,y)
        pendown()
        goto(new_x, new_y)

        # Update Stuff and Recurse
        # angle /= 1.4
        wacky *= .8 + random.betavariate(3,6)
        # wacky = wacky**2
        if wacky > 1: #lets get wacky
            print('lets get it wacky in here', wacky)
            length *= wacky**2
            drawBranch(new_x, new_y, angle, cumulative_angle + angle, length, level, wacky)
            drawBranch(new_x, new_y, angle, cumulative_angle - angle, length, level, wacky)

        else:
            print('not wack')
            length *= wacky / 1.3
            # length /= 2
            drawBranch(new_x, new_y, angle, cumulative_angle - angle, length, level, wacky)
            drawBranch(new_x, new_y, angle, cumulative_angle + angle, length, level, wacky)




# start at the bottom center
penup()
# goto(0,-400)
# pendown()
# goto(0,-300)
hideturtle()
tracer(False)
drawBranch(0, -200, pi/1.5, 0, 60, 6, .7)
tracer(True)
exitonclick()
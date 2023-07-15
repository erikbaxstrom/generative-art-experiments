from turtle import *
import random
from math import sin, cos, pi

setup(800, 800)
speed(0)


def drawBranch(x, y, angle, cumulative_angle, length, level):
    # new_x = sqrt(length^2-y^2)
    # new_y = sqrt(length^2-x^2)
    new_x = x + length * sin(cumulative_angle)
    new_y = y + length * cos(cumulative_angle)


    if level == 0:
        return
    else:
        # width(length/20)
        penup()
        goto(x,y)
        pendown()
        goto(new_x, new_y)
        level -= 1
        # length /= 1 + random.uniform(0,1)
        # angle /= 1.4
        length /= .8 + random.betavariate(3,8)
        if random.random()<1:
            drawBranch(new_x, new_y, angle, cumulative_angle + angle, length, level)
            drawBranch(new_x, new_y, angle, cumulative_angle - angle, length, level)




# start at the bottom center
penup()
# goto(0,-400)
# pendown()
# goto(0,-300)
hideturtle()
tracer(False)
drawBranch(0, -200, pi/3, 0, 60, 9)
tracer(True)
exitonclick()
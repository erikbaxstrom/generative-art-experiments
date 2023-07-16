import turtle
import random

class Canvas:
    """A model of brush strokes"""

    def __init__(self) -> None:
        self.moves = []
    
    def move_brush(self, x, y, z, s):
        """Move the drawing implement"""
        self.moves.append([x,y,z,s])
        print(f"painted {x, y, z, s}")
    
    # def paint(self, x, y, z, s)

    def to_gcode():
        """Export the drawing as gcode"""
        print("export gcode")

    def to_turtle(self):
        """Draw using Turtle Graphics"""
        print("draw in turtle")
        turtle.setup(1000, 1000)
        turtle.exitonclick()




def main():
    painting = Canvas()
    painting.move_brush(0,0,0,0) # go to origin fast without drawing (s=0) and leave pen up (z=0)
    painting.move_brush(2,2,5,0) # s=0, so lift pen, move fast to 2,2, then move pen to half pressure
    painting.move_brush(4,4,10,1) # starting from 2,2 with pen at half pressure, move to 4,4 while increasing brush pressure to full. do it slowly
    painting.move_brush(5,5,0,10) # move to 5,5 while decreasing brush pressure to 'off'. do it quickly
    painting.move_brush(0,0,0,0) #go back to origin without drawing
    print(f"brush strokes recorded: {painting.moves}")

    painting.to_turtle()

if __name__ == '__main__':
    main()
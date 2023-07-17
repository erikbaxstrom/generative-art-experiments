import turtle
import random

class Canvas:
    """A model of brush strokes"""

    def __init__(self) -> None:
        self.moves = []
        print("Created Canvas")
    
    def move_brush(self, x, y, z, s):
        """Move the drawing implement"""
        self.moves.append([x,y,z,s])
        print(f"recorded move {x, y, z, s}")
    
    # def paint(self, x, y, z, s)

    def to_gcode():
        """Export the drawing as gcode"""
        print("export gcode")

    def to_turtle(self):
        """Draw using Turtle Graphics"""
        print("Draw In Turtle")
        turtle.setup(1000,1000)
        for previous_move, current_move in zip(self.moves, self.moves[1:]):
            print(f"from:{previous_move} to: {current_move}")
            start_x = previous_move[0]
            start_y = previous_move[1]
            start_pressure = previous_move[2]
            end_x = current_move[0]
            end_y = current_move[1]
            end_pressure = current_move[2]
            speed = current_move[3]
            if(speed==0): # don't draw, just move
                print(f'moving to {end_x, end_y}')
                turtle.penup()
                turtle.goto(end_x,end_y)
            else: # let's draw!
                print(f'drawing to {end_x, end_y}')
                turtle.pendown()
                pressure_change = end_pressure - start_pressure
                print(f"pressure: start{start_pressure} end{end_pressure} change{pressure_change}")
                # Interpolate x, y, and pressure smoothly along the change in pressure
                for step in range(1, abs(pressure_change)+1):
                    incr_x = start_x + step * (end_x - start_x) / (abs(pressure_change))
                    incr_y = start_y + step * (end_y - start_y) / (abs(pressure_change))
                    line_width = start_pressure + step * (end_pressure - start_pressure) / (abs(pressure_change)) # to do: take some kind of mean of the pressure and speed to get the line width
                    print(f"incrementing to x{incr_x} y{incr_y} width{line_width}")
                    turtle.width(line_width)
                    turtle.goto(incr_x, incr_y)
                    
        turtle.exitonclick()




def main():
    painting = Canvas()
    painting.move_brush(0,0,0,0) # go to origin fast without drawing (s=0) and leave pen up (z=0)
    painting.move_brush(100,200,5,0) # s=0, so lift pen, move fast to 20,20, then move pen to half pressure
    painting.move_brush(400,300,10,1) # starting from 20,20 with pen at half pressure, move to 40,40 while increasing brush pressure to full. do it slowly
    painting.move_brush(50,50,0,10) # move to 50,50 while decreasing brush pressure to 'off'. do it quickly
    painting.move_brush(0,0,10,0) #go back to origin without drawing
    painting.move_brush(20,400,3, 1) # draw another line from the origin
    print(f"brush strokes recorded: {painting.moves}")

    painting.to_turtle()

if __name__ == '__main__':
    main()
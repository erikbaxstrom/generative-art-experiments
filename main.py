import turtle
import random

class Canvas:
    """A model of brush strokes on a canvas"""

    def __init__(self) -> None:
        self.moves = []
        print("Created Canvas")
    
    def move_brush(self, x, y, pressure, speed):
        """Paint on the Canvas by moving the brush. Speed = 0 lifts brush before moving."""
        self.moves.append([x,y,pressure, speed])
        print(f"recorded move {x, y, pressure, speed}")

    def to_gcode(self):
        """Export the Canvas as gcode"""
        print("Export gcode")
        gcode = ''
        with open('start_gcode.txt') as file: # use .txt b/c .gcode is more likely to be accientally deleted
            gcode += file.read()
        
        gcode += 'here is some gcode that I added \n'
        
        with open('end_gcode.txt') as file:
            gcode += file.read()
        print('the final gcode \n', gcode)



    def to_turtle(self):
        """Simulate the Canvas using Turtle Graphics"""
        print("Draw In Turtle")
        # Find the extreme coordinates and set up the drawing area
        max_x = max_y = min_x = min_y = 0
        padding = 100
        for move in self.moves: 
            max_x = max(max_x, move[0])
            min_x = min(min_x, move[0])
            max_y = max(max_y, move[1])
            min_y = min(min_y, move[1])
        print(f"minx{min_x} maxx{max_x} miny{min_y} maxy{max_y}")
        turtle.setup(max_x - min_x + padding, max_y - min_y + padding)
        turtle.setworldcoordinates(min_x - padding/2, min_y - padding/2, max_x + padding/2, max_y + padding/2)
        turtle.tracer(False)
        turtle.hideturtle()
        # Draw the Brush Strokes
        # Move to the starting location w/o drawing
        print(f'moving to {self.moves[0][0], self.moves[0][1]}')
        turtle.penup()
        turtle.goto(self.moves[0][0], self.moves[0][1])
        # Draw everything else
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
            else: # Let's draw!
                print(f'drawing to {end_x, end_y}')
                turtle.pendown()
                pressure_change = end_pressure - start_pressure
                print(f"pressure: start{start_pressure} end{end_pressure} change{pressure_change}")
                # Interpolate x, y, and pressure smoothly along the change in pressure
                if pressure_change == 0:
                    turtle.width(end_pressure)
                    turtle.goto(end_x, end_y)
                else:
                    for step in range(1, abs(pressure_change)+1):
                        incr_x = start_x + step * (end_x - start_x) / (abs(pressure_change))
                        incr_y = start_y + step * (end_y - start_y) / (abs(pressure_change))
                        line_width = start_pressure + step * (end_pressure - start_pressure) / (abs(pressure_change)) 
                        print(f"incrementing to x{incr_x} y{incr_y} width{line_width}")
                        turtle.width(line_width)
                        turtle.goto(incr_x, incr_y)
                        
        print("done drawing")
        turtle.tracer(True)
        turtle.exitonclick()




def main():
    canvas = Canvas()

    # Basic Test Code
    canvas.move_brush(0,0,0,0) # go to origin fast without drawing (s=0) and leave pen up (z=0)
    canvas.move_brush(100,-200,5,0) # s=0, so lift pen, move fast to 20,20, then move pen to half pressure
    canvas.move_brush(400,300,10,1) # starting from 20,20 with pen at half pressure, move to 40,40 while increasing brush pressure to full. do it slowly
    canvas.move_brush(50,50,0,10) # move to 50,50 while decreasing brush pressure to 'off'. do it quickly
    canvas.move_brush(0,0,10,0) #go back to origin without drawing and drop brush to 10
    canvas.move_brush(20,400,3, 1) # draw another line from the origin
    print(f"brush strokes recorded: {canvas.moves}")
    # canvas.move_brush(1, 300, 5, 0)
    # for x in range(1,300):
    #     canvas.move_brush(x,300-x,3, 5)
    canvas.to_gcode()

    # # Classic 10print
    # iterations = 20
    # tile_size = 20
    # for i in range(0,iterations):
    #     for j in range(0,iterations):
    #         if random.random() > (i+j)/(iterations * 2):
    #             canvas.move_brush(tile_size * i, tile_size * (j + 1), random.randint(1,10), 0)
    #             canvas.move_brush(tile_size * (i + 1), tile_size * (j), random.randint(1,10), 5)
    #         else:
    #             canvas.move_brush(tile_size * (i + 1), tile_size * (j+1), random.randint(1,10), 0)
    #             canvas.move_brush(tile_size * (i), tile_size * (j), random.randint(1,10), 5)
    # canvas.to_turtle()





if __name__ == '__main__':
    main()
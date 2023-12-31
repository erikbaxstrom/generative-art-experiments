import turtle
import random

class Canvas:
    """A model of brush strokes on a canvas"""


    def __init__(self) -> None:
        self.moves = []
        # Some physical parameters of the printer and the brush
        self.decimal_rounding = 2 # number of decimal places to round coordinates
        self.bed_x_max = 110.0
        self.bed_y_max = 85.0
        self.bed_padding = 10
        self.brush_z_min = -4.6 # relative coordinate!!! most pressure & lowest z coord
        self.brush_z_max = -3.2 # relative coordinate!!! least pressure & highest z coord
        self.brush_z_off = -2.25 # relative coordinate!!! brush lifted completely off the paper
        self.brush_z_range = self.brush_z_max - self.brush_z_min
        self.brush_speed_max = 4300
        self.brush_speed_min = 300
        self.brush_g0_xy_speed = 4300 # G0 code is for fast movements without interpolation
        self.brush_g0_z_speed = 90
        self.f_range = self.brush_speed_max - self.brush_speed_min
        self.scale = 0
    
    def move_brush(self, x, y, pressure, speed):
        """Paint on the Canvas by moving the brush. Speed = 0 lifts brush before moving."""
        self.moves.append([x,y,pressure, speed])
        # print(f"recorded move {x, y, pressure, speed}")

    def canv_to_z(self, pressure):
        """Convert a pressure (0 - 10) into a gcode Z coordinate"""
        z = self.brush_z_max - self.brush_z_range  * pressure /10
        # print(f"converted pressure: {pressure} to z coord {z}")
        return round(z, self.decimal_rounding)
        
    def canv_to_g(self, canv_coord):
        g_coord = self.scale * canv_coord
        return round(g_coord, self.decimal_rounding)

    def canv_to_f(self, speed):
        f_val = self.brush_speed_min + speed * self.f_range / 10 
        return round(f_val, self.decimal_rounding)
    
    def brush_move(self, x, y, z):
        gcode = "; move\n"
        gcode += f"G0 F{self.brush_g0_z_speed} Z{self.brush_z_off}\n" # lift brush
        gcode += f"G0 F{self.brush_g0_xy_speed} X{x} Y{y}\n" # move x/y
        gcode += f"G0 F{self.brush_g0_z_speed} Z{z}\n" # drop brush
        return gcode
    
    def brush_paint(self, x, y, z, f):
        gcode = "; paint\n"
        gcode += f"G1 F{f} X{x} Y{y} Z{z}\n"
        return gcode

    def to_gcode(self):
        """Export the Canvas as gcode"""
        # print("\n\n## Export gcode ##\n")

        # Import gcode header boilerplate
        gcode = ''
        with open('start_gcode.txt') as file: # use .txt b/c .gcode is more likely to be accidentally deleted
            gcode += file.read()
        
        ## Generate some gcode
        # Find the Canvas dimensions
        max_x = max_y = 0
        for move in self.moves:
            max_x = max(max_x, move[0])
            max_y = max(max_y, move[1])
        # print(f"max_x{max_x} max_y{max_y}")
        max_x += self.bed_padding
        max_y += self.bed_padding
        x_scale = self.bed_x_max / max_x
        y_scale = self.bed_y_max / max_y
        self.scale = min(x_scale, y_scale) # scale to fit the longer canvas dimension (min b/c scales are inverse of canvas size)

        # Move to the starting location w/o drawing
        x = self.canv_to_g(self.moves[0][0])
        y = self.canv_to_g(self.moves[0][1])
        z = self.canv_to_z(self.moves[0][2])
        # print("Starting at", x, y, z)
        gcode += self.brush_move(x, y, z)

        # Draw everything else
        for move in self.moves[1:]:
            x = self.canv_to_g(move[0])
            y = self.canv_to_g(move[1])
            z = self.canv_to_z(move[2])
            if move[3] == 0: # Speed is zero. Don't draw. Lift and move.
                # print(f"Moving to {x, y, z}")
                gcode += self.brush_move(x, y, z)
            else: # Let's draw!
                f = self.canv_to_f(move[3])
                # print(f"Drawing to {x, y, z} at rate {f}")
                gcode += self.brush_paint(x, y, z, f)

        # Import gcode footer boilerplate
        with open('end_gcode.txt') as file:
            gcode += file.read()
    
        print("\n\n## The Final gcode ##\n", gcode)



    def to_turtle(self):
        """Simulate the Canvas using Turtle Graphics"""
        print("\n\n## Draw In Turtle ##\n")
        # Find the extreme coordinates and set up the drawing area
        max_x = max_y = min_x = min_y = 0
        padding = 100
        for move in self.moves: 
            max_x = max(max_x, move[0])
            min_x = min(min_x, move[0])
            max_y = max(max_y, move[1])
            min_y = min(min_y, move[1])
        # print(f"minx{min_x} maxx{max_x} miny{min_y} maxy{max_y}")
        turtle.setup(max_x - min_x + padding, max_y - min_y + padding)
        turtle.setworldcoordinates(min_x - padding/2, min_y - padding/2, max_x + padding/2, max_y + padding/2)
        turtle.tracer(False)
        turtle.hideturtle()
        # Draw the Brush Strokes
        # Move to the starting location w/o drawing
        # print(f"moving to {self.moves[0][0], self.moves[0][1]}")
        turtle.penup()
        turtle.goto(self.moves[0][0], self.moves[0][1])
        # Draw everything else
        for previous_move, current_move in zip(self.moves, self.moves[1:]):
            # print(f"from:{previous_move} to: {current_move}")
            start_x = previous_move[0]
            start_y = previous_move[1]
            start_pressure = previous_move[2]
            end_x = current_move[0]
            end_y = current_move[1]
            end_pressure = current_move[2] 
            speed = current_move[3]
            if(speed==0): # don't draw, just move
                # print(f"moving to {end_x, end_y}")
                turtle.penup()
                turtle.goto(end_x,end_y)
            else: # Let's draw!
                # print(f"drawing to {end_x, end_y}")
                turtle.pendown()
                pressure_change = end_pressure - start_pressure
                # print(f"pressure: start{start_pressure} end{end_pressure} change{pressure_change}")
                # Interpolate x, y, and pressure smoothly along the change in pressure
                if pressure_change == 0:
                    turtle.width(end_pressure)
                    turtle.goto(end_x, end_y)
                else:
                    for step in range(1, abs(pressure_change)+1):
                        incr_x = start_x + step * (end_x - start_x) / (abs(pressure_change))
                        incr_y = start_y + step * (end_y - start_y) / (abs(pressure_change))
                        line_width = start_pressure + step * (end_pressure - start_pressure) / (abs(pressure_change)) 
                        # print(f"incrementing to x{incr_x} y{incr_y} width{line_width}")
                        turtle.width(line_width)
                        turtle.goto(incr_x, incr_y)
                        
        # print("done drawing")
        turtle.tracer(True)
        turtle.exitonclick()




def main():
    canvas = Canvas()

    # # Basic Test Code
    # # canvas.move_brush(0,0,0,0) # go to origin fast without drawing (s=0) and leave pen up (z=0)
    # canvas.move_brush(100,200,5,0) # s=0, so lift pen, move fast to 20,20, then move pen to half pressure
    # canvas.move_brush(400,300,10,1) # starting from 20,20 with pen at half pressure, move to 40,40 while increasing brush pressure to full. do it slowly
    # canvas.move_brush(50,50,1,10) # move to 50,50 while decreasing brush pressure to 'off'. do it quickly
    # canvas.move_brush(0,0,10,0) #go back to origin without drawing then brush to full pressure
    # canvas.move_brush(20,400,1, 5) # draw another line from the origin
    # # print(f"Brush Strokes:\n{canvas.moves}")

    # canvas.to_gcode()
    # # canvas.to_turtle()


    # Classic 10print
    iterations = 10
    tile_size = 20
    for i in range(0,iterations):
        for j in range(0,iterations):
            if random.random() > (i+j)/(iterations * 2):
                canvas.move_brush(tile_size * i, tile_size * (j + 1), random.randint(1,10), 0)
                canvas.move_brush(tile_size * (i + 1), tile_size * (j), random.randint(1,10), random.randint(1,10))
            else:
                canvas.move_brush(tile_size * (i + 1), tile_size * (j+1), random.randint(1,10), 0)
                canvas.move_brush(tile_size * (i), tile_size * (j), random.randint(1,10), random.randint(1,10))
    canvas.to_gcode()
    canvas.to_turtle()





if __name__ == '__main__':
    main()
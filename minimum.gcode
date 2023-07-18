; assumptions and parameters:
;    to go from minimum pressure to full pressure, brush will travel 5mm
;    Zero out the Z axis at 10 mm above the build plate. Brush should just touch the paper at Z-5mm. Z-10 is corresponds to maximum brush pressure
;    maximum speed in Z direction is 90 mm/min
;    maximum speed in X/Y direction is 4300 mm/min (ish)
;    minimum reasonable speed in x/y direction is probably about 300 mm/min
;    keep the print bed and extruder off
;    
;
M140 S0 ;set bed temp to zero. don't wait
M104 S0 ; set hotend temp to zero. don't wait
G21;(metric values)
G90;(absolute positioning)
M107;(start with the fan off)
G28;(Home the printer)
G0 F4320 Z10 ; hop up to Z10
G0 F4320 X10 Y30 ; move to X10 Y30
G92 X0 Y0 Z0 ; set zero
; move the brush a few times with varying pressure
G0 F4300 X30 Y30
G0 F90 Z-5 ; brush just touches paper
G1 F1200 X30 Y40
G0 F4320 Z-7.5 ; medium pressure
G1 F600 X40 Y40
G0 F4320 Z-10 ; strongest pressure
G1 F300 X50 Y40
G0 F4300 Z0 ; lift the brush off the paper
G0 X0 Y120;(Stick out the part)
M84;(Turn off stepper motors.)
;End of Gcode
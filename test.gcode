;FLAVOR:Marlin
;TIME:155
;Filament used: 0.0498098m
;Layer height: 0.175
;MINX:57.7
;MINY:57.7
;MINZ:0.263
;MAXX:62.3
;MAXY:62.3
;MAXZ:4.988
;Generated with Cura_SteamEngine 5.2.2
M140 S0 ;set bed temp to zero. don't wait
;M105 ;report temperature
;M190 S70 ; wait for bed temp
M104 S0 ; set hotend temp to zero. don't wait
; M105 ; report temp
; M109 S116 ; wait for hotend temp
; M82 ;absolute extrusion mode
G21;(metric values)
G90;(absolute positioning)
; M82;(set extruder to absolute mode)
M107;(start with the fan off)
G28;(Home the printer)
; G92 E0;(Reset the extruder to 0). Use G92 X0 Y0 Z0 to zero other coordinates
; G0 Z5 E5 F500;(Move up and prime the nozzle)
; G0 X-1 Z0;(Move outside the printable area)
; G1 Y60 E8 F500;(Draw a priming/wiping line to the rear)
; G1 X-1;(Move a little closer to the print area)
; G1 Y10 E16 F500;(draw more priming/wiping)
; G1 E15 F250;(Small retract)
; G92 E0;(Zero the extruder)
; G92 E0
; G92 E0
; ;LAYER_COUNT:28
; ;LAYER:0
; M107
; ;MESH:Just a box.stl
; G0 F4320 X58.375 Y58.375 Z0.263 ; extrusion speed 4320, goto x58.. y58.. z 0.263
G0 F4320 Z30 ; hop up to Z30
G0 F4320 X10 Y30 ; move to X10 Y30
G92 X0 Y0 Z0 ; set zero
; move somewhere, drop brush, paint
G0 F4320 X30 Y30 
G4 S5
G0 F4320 Z-10 ; 
G4 S5
G1 F1200 X30 Y40
G4 S5
G0 F4320 Z-15 ; 
G4 S5
G1 F600 X40 Y40
G4 S5
G0 F4320 Z-20 ; 
G4 S5
G1 F300 X50 Y40
G4 S5
G0 F4300 Z0
G4 S20
; G0 X0 Y0
; G28

; G0 X0 Y120;(Stick out the part)
; M190 S0;(Turn off heat bed, don't wait.)

; G4 S300;(Delay 5 minutes)
; M107;(Turn off part fan)
M84;(Turn off stepper motors.)
;End of Gcode
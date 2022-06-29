import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thorx = initial_tx
thory = initial_ty

# game loop
while True:
    print(thorx,thory,file=sys.stderr, flush= True )
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if thory  == light_y or thorx == light_x:
        if thory > light_y:
             thory = thory - 1
             print("N")
        elif thory < light_y:
             thory = thory + 1
             print("S")
        elif thorx > light_x:
            thorx = thorx -1
            print("W")
        else:
            thorx = thorx +1
            print("E") 
    else:
         if thory > light_y:
             if thorx < light_x:
                 thorx = thorx +1
                 thory = thory -1
                 print("NE") 
             else:
                 print("NW")
                 thorx = thorx -1
                 thory = thory -1        
         elif thory < light_y:
              if thorx > light_y:
                thorx = thorx -1
                thory = thory  +1    
                print("SW")
              else:
                  thorx = thorx +1
                  thory = thory +1
                  print("SE")

         

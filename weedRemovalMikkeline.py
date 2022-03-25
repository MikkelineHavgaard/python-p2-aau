
#include <webots/motor.h>
#include <webots/pen.h>

# --- Information recieved from outside code --- 
recievedProgram="softClean" #The program which the user have chosen 
cleaning=True  # Variable to start the cleaning while loop
import time #Instead of an outside variable telling we are done cleaning, the time function is substituted

# --- Variables ---
brushWheel=hingeJointBrush # name for the hingeJointBrush child in the code
speed=0 # We start out moving with a speed of 0 until a program is chosen. (speeds unit is radians/sec)
lightLaser=False # We start out not lasering until a program is chosen

# --- Classes ---
class weedRemovalPrograms: 
    def __init__(self,program): 
        self.program=program
    def chooseProgram(self):
        match self.program:
            case 'softClean': # Case for light brushing and lasering
                speed=1 # The brush rotates with 1 radians per second / the brush does a half rotation per second
                lightLaser=True
                return(speed,lightLaser)
            case 'hardClean': # Case for hard brushing and lasering
                speed=2 # The brush rotates with 2 radians per second / the brush does a full rotation per second
                lightLaser=True
                return(speed,lightLaser)
            case 'maintainClean': # Case for only lasering
                speed=0 # The brush does not rotate
                lightLaser=True
                return(speed,lightLaser)
            case 'scrubClean': # Case for only brushing hard 
                speed=2 # The brush rotates with 2 radians per second / the brush does a full rotation per second
                lightLaser=False
                return(speed,lightLaser)

class weedRemoval: # 
    def __init__(self,speed,lightLaser):
         self.speed=speed
         self.light=lightLaser
    def executeCleaning(self):
        brushWheel.setPosition(float('init')) # Ummmmm ???
        brushWheel.setVelocity(self.speed) # Sets the velocity of the brush 
        #light laser code

# --- Start of "loop" ---

brushWheel.setPosition(float('init')) # Ummmm again
brushWheel.setVelocity(speed) # We start by moving 0 

program=weedRemovalPrograms(recievedProgram)

programValues=weedRemoval(speed,lightLaser)


while cleaning == True:
    programValues.executeCleaning()
    time.sleep(10)
    cleaning = False


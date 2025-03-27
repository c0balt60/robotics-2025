# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       andr6521                                                     #
# 	Created:      3/21/2025, 12:17:22 PM                                       #
# 	Description:  Branch for the stacker bot                                   #
#   Bot:          Stacker Bot                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Component definitions
brain = Brain()
controller = Controller()

# Motor definitions
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
extender_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1)
lifter1_motor = Motor(Ports.PORT4, GearSetting.RATIO_18_1)
lifter2_motor = Motor(Ports.PORT5, GearSetting.RATIO_18_1)

# Variables
drive_forward = False
drive_backward = False
direction = 0

# TODO: COnfigure Wheel base
# DriveTrain class.
drivetrain = DriveTrain(left_motor, right_motor, 319.19, 295, 40, MM, 1)

def Drive(dir: DirectionType.DirectionType, velocity: int = 100, units: VelocityPercentUnits = PERCENT): #type: ignore
    """
    Function for handling drive mechanics

    Args:
        dir (DirectionType): _description_
        velocity (int, optional): _description_. Defaults to 100.
        units (VelocityPercentUnits, optional): _description_. Defaults to PERCENT.
    """

    # TODO: Add safe-guards for movement

    drivetrain.drive(dir, velocity, units)

def Turn(dir, velocty, units):

    drivetrain.set_turn_velocity(velocty)
    drivetrain.turn(dir, velocty, units)

# Main loop
def main():
    while True:

        Turn(
            (direction > 0) and RIGHT or (direction < 0 and LEFT) or RIGHT,
            (direction > 0 or direction < 0) and 75 or 0,
            PERCENT
        )

        Drive(
            drive_forward==True and FORWARD or (drive_backward==True and REVERSE or FORWARD),
            (drive_forward==True or drive_backward==True) and 75 or 0,
            PERCENT
        )
  
        sleep(50)

# Input definitions
def drive_pressed():
    global drive_forward
    drive_forward = True

def drive_released(): 
    global drive_forward
    drive_forward = False

def reverse_pressed():
    global drive_backward
    drive_backward = True

def reverse_released():
    global drive_backward
    drive_backward = False

def axis3_changed():
    global direction
    """
    Up and down
    """
    
    percent: float = controller.axis3.value()
    print(percent)
    direction = percent

def axis4_changed():
    """
    Left and right
    """
    percent: float = controller.axis3.value()

def axis1_changed():
    """
    Extend the length of stack receiver
    """
    percent: float = controller.axis1.value()

def axis2_changed():
    """
    Elevate chain up or down
    """
    percent: float = controller.axis2.value()

controller.buttonR2.pressed( drive_pressed )
controller.buttonR2.released( drive_released )
controller.buttonL2.pressed( reverse_pressed )
controller.buttonL2.released( reverse_released )
controller.axis3.changed( axis3_changed )
controller.axis4.changed( axis4_changed )
controller.axis2.changed( axis2_changed )
controller.axis1.changed( axis1_changed )

main()

# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       andr6521                                                     #
# 	Created:      2/28/2025, 11:01:22 AM                                       #
# 	Description:  Main branch containing base config for robots                #
#   Bot:          ~general                                                     #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Component definitions
brain = Brain()
controller = Controller()

# Motor definitions
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)

# TODO: COnfigure Wheel base
# DriveTrain class.
drivetrain = DriveTrain(left_motor, right_motor, 319.19, 295, 40, MM, 1)

def Drive(dir: DirectionType, velocity: int = 100, units: VelocityPercentUnits = PERCENT): #type: ignore
    """
    Function for handling drive mechanics

    Args:
        dir (DirectionType): _description_
        velocity (int, optional): _description_. Defaults to 100.
        units (VelocityPercentUnits, optional): _description_. Defaults to PERCENT.
    """

    # TODO: Add safe-guards for movement

    drivetrain.drive(dir, velocity, units)

def DriveMotors(right: Motor, left: Motor):
    """_summary_

    Args:
        right (Motor): _description_
        left (Motor): _description_
    """
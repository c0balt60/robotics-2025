# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       andr6521                                                     #
# 	Created:      2/28/2025, 11:52:16 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Component definitions
brain = Brain()
controller = Controller()

# Drivetrain
right: Motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
left: Motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
drivetrain: DriveTrain = DriveTrain(left, right)
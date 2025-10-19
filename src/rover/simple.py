"""
A simple implementation of a rover
only 2 wheels allows for an understanding of the robot
"""

from dataclasses import dataclass
from constants import SIMPLE_ROVER_CONSTANTS
from motor.simple import SimpleMotorState, SimpleMotor

"""
A class to handle simple rover state to pass up through the layers
"""
@dataclass(frozen=True)
class SimpleRoverState():
    motor1: SimpleMotorState
    motor2: SimpleMotorState
    x: float
    y: float
    theta: float


"""
An implementation of the simple rover
"""
class SimpleRover():
    def __init__(self):
        pass
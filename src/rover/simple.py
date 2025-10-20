"""
A simple implementation of a rover
only 2 wheels allows for an understanding of the robot
"""

from dataclasses import dataclass
from motor.simple import SimpleMotorState, SimpleMotor
from motor.constants import SIMPLE_MOTOR_CONSTANTS
from typing import List
import math
from .base import Rover, RoverState

# """
# A class to handle all the angles assoicated with the rover
# """
# @dataclass(frozen=True)
# class AngleState():
#     vL:float
#     vR:float
#     R:float
#     omega:float

"""
A class to handle simple rover state to pass up through the layers
"""
@dataclass(frozen=True)
class SimpleRoverState(RoverState):
    motor1:SimpleMotorState
    motor2:SimpleMotorState
    v:float
    omega:float
    theta:float

"""
An implementation of the simple rover
"""
class SimpleRover(Rover):
    def __init__(self, radius:float, axelLength:float, startState:SimpleRoverState):
        self.__radius = radius
        self.__axel = axelLength
        self.motor1 = SimpleMotor(SIMPLE_MOTOR_CONSTANTS.MAX_RPM, SIMPLE_MOTOR_CONSTANTS.MAX_VOLTAGE, startState.motor1)
        self.motor2 = SimpleMotor(SIMPLE_MOTOR_CONSTANTS.MAX_RPM, SIMPLE_MOTOR_CONSTANTS.MAX_VOLTAGE, startState.motor2)
        self.cs = startState
    
    def getCurrentState(self) -> SimpleRoverState:
        return self.cs

    """
    converts to RPM to velocity
    """
    def getWheelVeloticy(self, RPM:float) -> float:
        return RPM * ((2*math.pi*self.__radius)/60.0)

    """
    takes a command and runs the tick
    command: list of voltages
    """
    def runTick(self, command: List[float], tickLength:int) -> None:
        motor1State = self.motor1.getNewState(command[0])
        motor2State = self.motor2.getNewState(command[1])

        vl = self.getWheelVeloticy(motor1State.rpm)
        vr = self.getWheelVeloticy(motor2State.rpm)

        v = (vl + vr)/2.0
        w = (vl - vr)/self.__axel

        if abs(w) > 1e-6:
            x_new = self.cs.x + (v/w)*(math.sin(self.cs.theta + w*tickLength) - math.sin(self.cs.theta))
            y_new = self.cs.y - (v/w)*(math.cos(self.cs.theta + w*tickLength) - math.cos(self.cs.theta))
            theta_new = self.cs.theta + w*tickLength
        else:
            x_new = self.cs.x + v*tickLength*math.cos(self.cs.theta)
            y_new = self.cs.y + v*tickLength*math.sin(self.cs.theta)
            theta_new = self.cs.theta

        # finally construct a new state to pull from
        self.cs = SimpleRoverState( x_new, y_new, motor1State, motor2State, v, w, theta_new)
    
    def reset(self) -> None:
        self.motor1.reset()
        self.motor2.reset()
        self.cs = SimpleRoverState(0, 0, self.motor1.getCurrentState(), self.motor2.getCurrentState(), 0, 0, 0)
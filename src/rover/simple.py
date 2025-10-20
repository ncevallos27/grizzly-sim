"""
A simple implementation of a rover
only 2 wheels allows for an understanding of the robot
"""

from dataclasses import dataclass
from constants import SIMPLE_ROVER_CONSTANTS
from motor.simple import SimpleMotorState, SimpleMotor
from typing import List
import math

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
class SimpleRoverState():
    motor1:SimpleMotorState
    motor2:SimpleMotorState
    x:float
    y:float
    v:float
    omega:float
    theta:float

"""
An implementation of the simple rover
"""
class SimpleRover():
    def __init__(self, radius:float, axelLength:float, startingX:float, startingY:float, startingTheta:float, startingV:float, startingW:float):
        self.__radius:float = radius
        self.__axel:float = axelLength
        self.motor1:SimpleMotor = SimpleMotor(SIMPLE_ROVER_CONSTANTS.RADIUS)
        self.motor2:SimpleMotor = SimpleMotor(SIMPLE_ROVER_CONSTANTS.RADIUS)
        self.__currentState:SimpleRoverState = SimpleRoverState(self.motor1.getCurrentState(), self.motor2.getCurrentState(), startingX, startingY, startingV, startingW, startingTheta)
    
    @property
    def getCurrentState(self):
        return self.__currentState

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
            x_new = self.__currentState.x + (v/w)*(math.sin(self.__currentState.theta + w*tickLength) - math.sin(self.__currentState.theta))
            y_new = self.__currentState.y - (v/w)*(math.cos(self.__currentState.theta + w*tickLength) - math.cos(self.__currentState.theta))
            theta_new = self.__currentState.theta + w*tickLength
        else:
            x_new = self.__currentState.x + v*tickLength*math.cos(self.__currentState.theta)
            y_new = self.__currentState.y + v*tickLength*math.sin(self.__currentState.theta)
            theta_new = self.__currentState.theta

        # finally construct a new state to pull from
        self.__currentState = SimpleRoverState(motor1State, motor2State, x_new, y_new, v, w, theta_new)

        return
    
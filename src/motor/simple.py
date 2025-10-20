"""
This file contains a simple and naive implementation of a motor.
It assumes an even mapping of voltage to rpm and that the action is instant.
"""
from dataclasses import dataclass
from constants import SIMPLE_MOTOR_CONSTANTS

"""
A class to handle simple motor state to pass up
"""
@dataclass(order=True, frozen=True)
class SimpleMotorState():
    voltage:float
    rpm:float

"""
An implementation of the simple motor
Assumes volage is a number between 0 and 5v
"""
class SimpleMotor():
    def __init__(self, maxRPM:float):
        self.maxRPM = maxRPM
        self.minRPM = SIMPLE_MOTOR_CONSTANTS.MIN_RPM #0
        self.maxVoltage:float = SIMPLE_MOTOR_CONSTANTS.MAX_VOLTAGE #5
        self.currentState = SimpleMotorState(0, 0)

    def getNewState(self, voltage:float):
        percentage = float(voltage/self.maxVoltage)
        self.currentState = SimpleMotorState(voltage=voltage, rpm=float(percentage*self.maxRPM))
        return self.currentState
    
    def getCurrentState(self):
        return self.currentState

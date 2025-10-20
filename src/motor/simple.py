"""
This file contains a simple and naive implementation of a motor.
It assumes an even mapping of voltage to rpm and that the action is instant.
"""
from dataclasses import dataclass

"""
A class to handle simple motor state to pass up
"""
@dataclass(order=True, frozen=True)
class SimpleMotorState():
    voltage:float
    rpm:float

"""
An implementation of the simple motor
Assumes volage is a number between 0 and 
"""
class SimpleMotor():
    def __init__(self, maxRPM:float, maxVoltage:float, startState:SimpleMotorState):
        self.maxRPM = maxRPM
        self.maxVoltage = maxVoltage
        self.currentState = startState

    def getNewState(self, voltage:float) -> SimpleMotorState:
        percentage = float(voltage/self.maxVoltage)
        self.currentState = SimpleMotorState(voltage=voltage, rpm=float(percentage*self.maxRPM))
        return self.currentState
    
    def getCurrentState(self) -> SimpleMotorState:
        return self.currentState
    
    def reset(self) -> None:
        self.currentState = SimpleMotorState(0, 0)
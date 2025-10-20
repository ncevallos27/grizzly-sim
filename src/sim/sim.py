from src.rover.base import Rover
from src.logger.base import Logger
from typing import Callable, List, Mapping, Any
from src.motor.constants import SIMPLE_MOTOR_CONSTANTS

class Simulator:
    def __init__(self, rover:Rover, logger:Logger, dt:float = 0.01, duration:float=5.0):
        self.rover = rover
        self.logger = logger
        self.tickLength = dt
        self.duration = duration
        self.currentTime = 0

    def run(self, cmd: Callable[[float, float], List[float]]) -> None:
        

        while self.currentTime < self.duration:
            state = self.rover.getCurrentState().ready()
            row:Mapping[str, Any] = {
                "t": self.currentTime,
                **state
            }

            self.logger.write(row)
            self.rover.runTick(cmd(self.currentTime, SIMPLE_MOTOR_CONSTANTS.MAX_VOLTAGE), self.tickLength)
            self.currentTime += self.tickLength


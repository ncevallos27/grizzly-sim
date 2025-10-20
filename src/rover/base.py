from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class RoverState(ABC):
    x:float
    y:float


class Rover(ABC):
    def __init__(self, radius:float, axelLength:float):
        self.radius = radius
        self.axelLength = axelLength

    @abstractmethod
    def getCurrentState(self) -> RoverState: ...

    @abstractmethod
    def runTick(self, command: List[float], tickLength:int) -> None: ...

    @abstractmethod
    def reset(self) -> None: ...

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any, Mapping

@dataclass(frozen=True)
class RoverState(ABC):
    x:float
    y:float

    @abstractmethod
    def ready(self) -> Mapping[str, Any]:
        pass


class Rover(ABC):
    def __init__(self, radius:float, axelLength:float):
        self.radius = radius
        self.axelLength = axelLength

    @abstractmethod
    def getCurrentState(self) -> RoverState: ...

    @abstractmethod
    def runTick(self, command: List[float], tickLength:float) -> None: ...

    @abstractmethod
    def reset(self) -> None: ...

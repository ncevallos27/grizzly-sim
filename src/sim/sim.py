from src.rover.base import Rover
from src.logger.base import Logger

class Simulator:
    def __init__(self, rover:Rover, logger:Logger):
        self.rover = rover
        self.logger = logger

    
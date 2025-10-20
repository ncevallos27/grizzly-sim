import src.rover.simple as rcSimple
from src.rover.constants import SIMPLE_ROVER_CONSTANTS
from src.motor.simple import SimpleMotorState
from src.sim.sim import Simulator
from src.logger.terminal import TerminalLogger
from src.commands.simple import goCircle
import math

def main():
    startState = rcSimple.SimpleRoverState(x=0, 
                              y=0, 
                              motor1=SimpleMotorState(rpm=0, voltage=0), 
                              motor2=SimpleMotorState(rpm=0, voltage=0), 
                              v=0, 
                              omega=0, 
                              theta=math.pi/4)

    rover = rcSimple.SimpleRover(SIMPLE_ROVER_CONSTANTS.RADIUS, SIMPLE_ROVER_CONSTANTS.AXEL_LENGTH, startState)
    logger = TerminalLogger(3, 1)

    sim = Simulator(rover, logger, duration=5)

    sim.run(goCircle)


if __name__ == "__main__":
    main()
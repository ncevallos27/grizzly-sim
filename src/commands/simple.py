"""
Commands for the simple rover
"""

from typing import List

def goForward(t: float, maxVoltage:float) -> List[float]:
    """
    Go foward for 4.5 seconds then stop moving
    """
    if t < 4.5:
        return [1*maxVoltage, 1*maxVoltage]
    else:
        return [0, 0]
    
def goLeft(t: float, maxVoltage:float) -> List[float]:
    """
    more power on the right wheel
    """
    if t < 4.5:
        return [0.25*maxVoltage, 1*maxVoltage]
    else:
        return [0, 0]
    
def goLeftMax(t: float, maxVoltage:float) -> List[float]:
    """
    only power on the right wheel
    """
    if t < 4.5:
        return [0, 1*maxVoltage]
    else:
        return [0, 0]
    
def goRight(t: float, maxVoltage:float) -> List[float]:
    """
    more power on the left wheel
    """
    if t < 4.5:
        return [1*maxVoltage, 0.25*maxVoltage]
    else:
        return [0, 0]
    
def goRightMax(t: float, maxVoltage:float) -> List[float]:
    """
    only power on the left wheel
    """
    if t < 4.5:
        return [1*maxVoltage, 0*maxVoltage]
    else:
        return [0, 0]
    
def goCircle(t: float, maxVoltage:float) -> List[float]:
    """
    spin a circle
    """
    if t < 4.5:
        return [1*maxVoltage, -1*maxVoltage]
    else:
        return [0, 0]
from dataclasses import dataclass

@dataclass
class SIMPLE_MOTOR_CONSTANTS:
    MAX_VOLTAGE = 5
    MIN_VOLTAGE = 0
    MIN_RPM = 0
    MAX_RPM = 200 # NOTE: this is accounting for a geared down, this is at wheel RPM

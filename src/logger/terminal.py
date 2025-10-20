from __future__ import annotations
from typing import Mapping, Any
from src.logger.base import Logger
import math

class TerminalLogger(Logger):
    """
    Logs simulation data directly to the terminal (stdout).
    Compatible with Simulator via the Logger interface.
    """

    def __init__(self, precision: int = 3, step_interval: int = 10):
        """
        Args:
            precision: Number of decimals to show for floats.
            step_interval: Print every Nth step to reduce clutter.
        """
        self.precision = precision
        self.step_interval = max(1, step_interval)
        self._count = 0

    def write(self, row: Mapping[str, Any]) -> None:
        self._count += 1
        if self._count % self.step_interval != 0:
            return

        t = row.get("t", 0.0)
        x = row.get("x", 0.0)
        y = row.get("y", 0.0)
        th = row.get("theta", 0.0) % math.pi
        v = row.get("v", 0.0)
        omega = row.get("omega", 0.0)

        fmt = f"[t={t:.2f}s] pos=({x:.{self.precision}f}, {y:.{self.precision}f}) " \
              f"θ={th:.{self.precision}f} v={v:.{self.precision}f} ω={omega:.{self.precision}f}"
        
        print(fmt)

    def flush(self) -> None:
        pass

    def close(self) -> None:
        print("Logger Closed")
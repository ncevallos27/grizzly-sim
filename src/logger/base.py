from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Mapping, Any

class Logger(ABC):
    @abstractmethod
    def write(self, row: Mapping[str, Any]) -> None: ...

    @abstractmethod
    def flush(self) -> None: ...
    
    @abstractmethod
    def close(self) -> None: ...
from logging import Logger
from numbers import Real

from cocotb.handle import NonHierarchyObject

class BaseClock:
    signal: NonHierarchyObject
    def __init__(self, signal: NonHierarchyObject) -> None: ...
    @property
    def log(self) -> Logger: ...

class Clock(BaseClock):
    def __init__(
        self, signal: NonHierarchyObject, period: float | Real, units: str = ...
    ) -> None: ...
    async def start(self, cycles: int | None = ..., start_high: bool = ...) -> None: ...

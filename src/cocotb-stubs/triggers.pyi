import abc
from typing import (
    Any,
    AsyncContextManager,
    Awaitable,
    Coroutine,
    Generator,
    Generic,
    TypeVar,
    overload,
)

from cocotb.decorators import RunningTask
from cocotb.handle import NonHierarchyObject
from cocotb.outcomes import Outcome

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
Self = TypeVar("Self")
TriggerT = TypeVar("TriggerT", bound=Trigger)

class Trigger(metaclass=abc.ABCMeta):
    def __await__(self: Self) -> Generator[Any, Any, Self]: ...

class PythonTrigger(Trigger, metaclass=abc.ABCMeta): ...
class GPITrigger(Trigger, metaclass=abc.ABCMeta): ...

class Timer(GPITrigger):
    def __init__(
        self,
        time: float,
        units: str,
        *,
        round_mode: str = ...,
    ) -> None: ...

class ReadOnly(GPITrigger): ...
class ReadWrite(GPITrigger): ...
class NextTimeStep(GPITrigger): ...

class _EdgeBase(GPITrigger, metaclass=abc.ABCMeta):
    signal: NonHierarchyObject
    def __init__(self, signal: NonHierarchyObject) -> None: ...

class RisingEdge(_EdgeBase): ...
class FallingEdge(_EdgeBase): ...
class Edge(_EdgeBase): ...

class Event(Generic[T]):
    fired: bool
    data: T | None
    def __init__(self) -> None: ...
    def set(self, data: T | None = ...) -> None: ...
    async def wait(self) -> None: ...
    def clear(self) -> None: ...
    def is_set(self) -> bool: ...

class Lock(AsyncContextManager[Lock]):
    locked: bool
    def __init__(self) -> None: ...
    async def acquire(self) -> None: ...
    async def release(self) -> None: ...
    def __bool__(self) -> bool: ...

class NullTrigger(Trigger): ...

class Join(PythonTrigger, Generic[T_co]):
    def __init__(
        self, coroutine: Coroutine[Any, Any, T_co] | RunningTask[T_co]
    ) -> None: ...
    @property
    def retval(self) -> T_co: ...
    @property
    def _outcome(self) -> Outcome[T_co]: ...

class Waitable(Awaitable[T_co], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def _wait(self) -> T_co: ...
    def __await__(self) -> Generator[Any, Any, T_co]: ...

class _AggregateWaitable(Waitable[T_co], metaclass=abc.ABCMeta):
    triggers: Any
    def __init__(self, *triggers: Trigger | RunningTask[Any]) -> None: ...

class Combine(_AggregateWaitable[Combine]):
    async def _wait(self) -> Combine: ...

class First(_AggregateWaitable[object]):
    async def _wait(self) -> object: ...

class ClockCycles(Waitable[ClockCycles]):
    signal: Any
    num_cycles: Any
    def __init__(
        self, signal: NonHierarchyObject, num_cycles: int, rising: bool = ...
    ) -> None: ...
    async def _wait(self) -> ClockCycles: ...

@overload
async def with_timeout(
    trigger: TriggerT, timeout_time: float, timeout_unit: str
) -> TriggerT: ...
@overload
async def with_timeout(
    trigger: RunningTask[T_co], timeout_time: float, timeout_unit: str
) -> T_co: ...
@overload
async def with_timeout(
    trigger: Waitable[T_co], timeout_time: float, timeout_unit: str
) -> T_co: ...

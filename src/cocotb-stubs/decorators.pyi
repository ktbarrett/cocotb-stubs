from logging import Logger
from typing import Any, Callable, Coroutine, Generator, Generic, Type, TypeVar

from cocotb.outcomes import Outcome
from cocotb.triggers import Join

T_co = TypeVar("T_co", covariant=True)

class RunningTask(Generic[T_co]):
    __name__: str
    __qualname__: str
    @property
    def log(self) -> Logger: ...
    @property
    def retval(self) -> T_co: ...
    @property
    def _outcome(self) -> Outcome[T_co]: ...
    @property
    def _finished(self) -> bool: ...
    def send(self, __value: Any) -> T_co: ...
    def throw(self, exc: BaseException) -> None: ...
    def close(self) -> None: ...
    def kill(self) -> None: ...
    def join(self) -> Join[T_co]: ...
    def has_started(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __await__(self) -> Generator[Any, Any, T_co]: ...

GenCoroFunc = Generator[Any, Any, T_co]
AsyncCoroFunc = Callable[..., Coroutine[Any, Any, T_co]]

class coroutine(Generic[T_co]):
    def __init__(
        self,
        f: GenCoroFunc[T_co] | AsyncCoroFunc[T_co],
    ) -> None: ...
    @property
    def log(self) -> Logger: ...
    def __call__(self, *args: Any, **kwargs) -> Callable[..., RunningTask[T_co]]: ...

class function(Generic[T_co]):
    def __init__(self, f: GenCoroFunc[T_co] | AsyncCoroFunc[T_co]) -> None: ...
    @property
    def log(self) -> Logger: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Callable[..., T_co]: ...

class external(Generic[T_co]):
    def __init__(self, f: Callable[..., T_co]) -> None: ...
    @property
    def log(self) -> Logger: ...
    def __call__(
        self, *args: Any, **kwargs: Any
    ) -> Callable[..., RunningTask[T_co]]: ...

class _test(coroutine[T_co]):
    timeout_time: float | None
    timeout_unit: str
    expect_fail: bool
    expect_error: bool
    skip: bool
    stage: int | None
    im_test: bool
    name: str
    def __init__(self, f: GenCoroFunc[T_co] | AsyncCoroFunc[T_co]) -> None: ...
    def __call__(
        self, *args: Any, **kwargs: Any
    ) -> Callable[..., RunningTask[T_co]]: ...

def test(
    self,
    timeout_time: float | None = ...,
    timeout_unit: str = ...,
    expect_fail: bool = ...,
    expect_error: bool = ...,
    skip: bool = ...,
    stage: int | None = ...,
) -> Type[_test]: ...

from typing import (
    Any,
    Callable,
    Coroutine,
    Generator,
    Generic,
    Sequence,
    TypeVar,
    overload,
)

from cocotb.triggers import Trigger

TestFunc = TypeVar(
    "TestFunc",
    bound=Generator[Trigger, Trigger, None]
    | Callable[..., Coroutine[Trigger, Trigger, None]],
)

class RegressionManager: ...

class TestFactory(Generic[TestFunc]):
    def __init__(self, test_function: TestFunc, *args: Any, **kwargs: Any) -> None: ...
    @overload
    def add_option(self, name: str, optionlist: Sequence[Any]) -> None: ...
    @overload
    def add_option(
        self, name: Sequence[str], optionlist: Sequence[Sequence[Any]]
    ) -> None: ...
    def generate_tests(self, prefix: str = ..., postfix: str = ...) -> None: ...

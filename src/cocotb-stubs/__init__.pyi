from collections.abc import Coroutine
from logging import Logger
from typing import Any, Dict, List, TypeVar, Union

from cocotb._version import __version__ as __version__
from cocotb.decorators import RunningTask
from cocotb.decorators import coroutine as coroutine
from cocotb.decorators import external as external
from cocotb.decorators import function as function
from cocotb.decorators import test as test
from cocotb.handle import SimHandleBase
from cocotb.regression import RegressionManager
from cocotb.scheduler import Scheduler

T_co = TypeVar("T_co", covariant=True)

scheduler: Scheduler
regression_manager: RegressionManager
argv: List[str]
argc: int
plusargs: Dict[str, Union[bool, str]]
LANGUAGE: str
SIM_NAME: str
SIM_VERSION: str
RANDOM_SEED: int
top: SimHandleBase
log: Logger

def fork(coro: RunningTask[T_co] | Coroutine[Any, Any, T_co]) -> RunningTask[T_co]: ...
def start_soon(
    coro: RunningTask[T_co] | Coroutine[Any, Any, T_co]
) -> RunningTask[T_co]: ...
async def start(
    coro: RunningTask[T_co] | Coroutine[Any, Any, T_co]
) -> RunningTask[T_co]: ...
def create_task(
    coro: RunningTask[T_co] | Coroutine[Any, Any, T_co]
) -> RunningTask[T_co]: ...

from typing import Generic, Iterator, TypeVar

from cocotb.binary import BinaryValue

T = TypeVar("T")

class SimHandleBase:
    @property
    def _name(self) -> str: ...
    @property
    def _type(self) -> str: ...
    @property
    def _path(self) -> str: ...
    @property
    def _def_name(self) -> str: ...
    @property
    def _def_file(self) -> str: ...
    def get_definition_name(self) -> str: ...
    def get_definition_file(self) -> str: ...
    def __len__(self) -> int: ...
    def __getattr__(self, name: str) -> SimHandleBase: ...
    def __str__(self) -> str: ...

class RegionObject(SimHandleBase):
    def __iter__(self) -> Iterator[SimHandleBase]: ...

class HierarchyObject(RegionObject):
    def _id(self, name: str, extended: bool = ...) -> SimHandleBase: ...

class HierarchyArrayObject(RegionObject):
    def __getitem__(self, index: int) -> SimHandleBase: ...

class NonHierarchyObject(SimHandleBase):
    def __iter__(self) -> Iterator[SimHandleBase]: ...
    @property
    def value(self) -> object: ...
    @value.setter
    def value(self, value: object) -> None: ...
    def setimmediatevalue(self, value: object) -> None: ...

class ConstantObject(NonHierarchyObject):
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __str__(self) -> str: ...

class NonHierarchyIndexableObject(NonHierarchyObject):
    def __getitem__(self, index: int) -> SimHandleBase: ...
    def value(self) -> list[object]: ...

class NonConstantObject(NonHierarchyIndexableObject):
    def drivers(self) -> Iterator[SimHandleBase]: ...
    def loads(self) -> Iterator[SimHandleBase]: ...

class _SetAction: ...

class _SetValueAction(_SetAction, Generic[T]):
    @property
    def value(self) -> T: ...
    def __init__(self, value: T) -> None: ...

class Deposit(_SetValueAction[T]): ...
class Force(_SetValueAction[T]): ...
class Freeze(_SetAction): ...
class Release(_SetAction): ...

class ModifiableObject(NonConstantObject):
    @property
    def value(self) -> BinaryValue: ...
    @value.setter
    def value(self, new_value: BinaryValue | int) -> None: ...
    def setimmediatevalue(self, value: BinaryValue | int) -> None: ...
    def __int__(self): ...
    def __str__(self) -> str: ...

class RealObject(ModifiableObject):
    @property
    def value(self) -> float: ...
    @value.setter
    def value(self, new_value: float) -> None: ...
    def setimmediatevalue(self, value: float) -> None: ...
    def __float__(self): ...

class EnumObject(ModifiableObject):
    @property
    def value(self) -> int: ...
    @value.setter
    def value(self, new_value: int) -> None: ...
    def setimmediatevalue(self, value: int) -> None: ...

class IntegerObject(ModifiableObject):
    @property
    def value(self) -> int: ...
    @value.setter
    def value(self, new_value: int) -> None: ...
    def setimmediatevalue(self, value: int) -> None: ...

class StringObject(ModifiableObject):
    @property
    def value(self) -> bytes: ...
    @value.setter
    def value(self, new_value: bytes) -> None: ...
    def setimmediatevalue(self, value: bytes) -> None: ...

def SimHandle(handle: int, path: str | None = ...) -> SimHandleBase: ...

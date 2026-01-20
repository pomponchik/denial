from itertools import count
from typing import Any, Optional, Union

from printo import descript_data_object


class InnerNoneType:
    id: Optional[Union[int, str]]  # pragma: no cover
    counter = count()

    def __init__(self, id: Optional[Union[int, str]] = None) -> None:  # noqa: A002
        if id is None:
            self.id = next(self.counter)
        else:
            self.id = id

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        if not self.id:
            return 'InnerNone'
        return descript_data_object(type(self).__name__, (self.id,), {})

    def __bool__(self) -> bool:
        return False


InnerNone = InnerNoneType()

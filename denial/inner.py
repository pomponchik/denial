from itertools import count

from printo import descript_data_object


class InnerNoneType:
    id: Optional[int]
    counter = itertools.count()

    def __new__(self) -> 'InnerNoneType':
        self.id = next(self.counter)

    def __init__(self, id: Union[int, str]) -> None:
        self.id = id

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.id == other.id

    def __repr__(self) -> str:
        if not self.id:
            return 'InnerNone'
        else:
            return descript_data_object(type(self).__name__, (self.id,), {})


InnerNone = InnerNoneType()

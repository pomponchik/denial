import sys
from typing import Optional

if sys.version_info <= (3, 10):
    from typing_extensions import TypeAlias  # pragma: no cover
else:
    from typing import TypeAlias  # pragma: no cover

from denial import InnerNoneType

SentinelType: TypeAlias = Optional[InnerNoneType]

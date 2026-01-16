# denial

[![Downloads](https://static.pepy.tech/badge/denial/month)](https://pepy.tech/project/denial)
[![Downloads](https://static.pepy.tech/badge/denial)](https://pepy.tech/project/denial)
[![Coverage Status](https://coveralls.io/repos/github/pomponchik/denial/badge.svg?branch=main)](https://coveralls.io/github/pomponchik/denial?branch=main)
[![Lines of code](https://sloc.xyz/github/pomponchik/denial/?category=code)](https://github.com/boyter/scc/)
[![Hits-of-Code](https://hitsofcode.com/github/pomponchik/denial?branch=main&label=Hits-of-Code&exclude=docs/)](https://hitsofcode.com/github/pomponchik/denial/view?branch=main)
[![Test-Package](https://github.com/pomponchik/denial/actions/workflows/tests_and_coverage.yml/badge.svg)](https://github.com/pomponchik/denial/actions/workflows/tests_and_coverage.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/denial.svg)](https://pypi.python.org/pypi/denial)
[![PyPI version](https://badge.fury.io/py/denial.svg)](https://badge.fury.io/py/denial)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/pomponchik/denial)


There is a small but annoying misunderstanding in the design of Python as a language. The language defines the constant `None`, which designates a special object that is used as a "stub" when it is not possible to use the "real" value. But sometimes, when implementing libraries, it is not possible to distinguish `None`, passed by the user as the default value, from `None`, which means that the value is *really undefined*. In some rare cases, this distinction is important.

For example, the [dataclasses](https://docs.python.org/3/library/dataclasses.html) library defines a special [MISSING](https://docs.python.org/3/library/dataclasses.html#dataclasses.MISSING) constant for such cases. This is used to separate the cases when the user has not set a default value from the case when he has set `None` as the default value. However, the use of `MISSING` is tied to the use of this library, and sometimes this constant may be needed for completely different purposes.

This library defines just such an object: `None` for situations where you need to distinguish `None` as a value from the user, and None as a designation that something is really undefined. This value should not fall "outside", into the user's space, it should remain only inside the libraries implementations.

Well, how to use it?

Let's start with the installation:

```bash
pip install denial
```

This is how this additional version of `None` and its class are imported (can be used for type hints or checks via isinstance):

```python
from denial import InnerNone, InnerNoneType
```

`InnerNone` is used the same way as `None`, with a couple of additional caveats:

1. `InnerNone` is not an instance of [`NoneType`](https://docs.python.org/3/library/types.html#types.NoneType), it has its own parent class.

2. `InnerNone` cannot be used as your own type hint. What am I talking about? Let's look at the documentation:

  > When used in a type hint, the expression `None` is considered equivalent to `type(None)`.

  > *[Official typing documentation](https://typing.python.org/en/latest/spec/special-types.html#none)*

  In most type checkers, this is implemented using a special "crutch", an exception in the code that cannot be repeated for any other value. Therefore, use `InnerNoneType` as a type hint.

<details>
  <summary>ⓘ</summary>

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

</details>


![logo](https://raw.githubusercontent.com/pomponchik/denial/develop/docs/assets/logo_1.svg)


The [`None`](https://docs.python.org/3/library/constants.html#None) constant built into Python is convenient for client code, but it is often insufficient when creating libraries. The fact is that this makes it impossible to [distinguish situations](https://colinmcginn.net/truth-value-gaps-and-meaning/) where a value is *undefined* from situations where it is *defined as undefined*. Does that sound too abstract?

In fact, the problem of this distinction is found everywhere in library development. `Sentinel objects` are used to resolve it, and [many modules](https://mail.python.org/archives/list/python-dev@python.org/message/JBYXQH3NV3YBF7P2HLHB5CD6V3GVTY55/) from the standard library define their own. For example, the [dataclasses](https://docs.python.org/3/library/dataclasses.html) library defines a special [MISSING](https://docs.python.org/3/library/dataclasses.html#dataclasses.MISSING) constant for such cases. This is used to separate the cases when the user has not set a default value from the case when he has set `None` as the default value.

However, we can't all use sentinel objects from some built-in module if we don't need the functionality of that module. Until the [PEP](https://peps.python.org/pep-0661/) has been adopted on this topic, it is better to use a special package containing only this primitive. Such a package is `denial`. It defines just such an object: `None` for situations where you need to distinguish `None` as a value from the user, and None as a designation that something is really undefined. This value should not fall "outside", into the user's space, it should remain only inside the libraries implementations. In addition, this library offers a special class that allows you to create your own sentinels.


## Table of contents

- [**Installation**](#installation)
- [**The second None**](#the-second-none)


## Installation

Install it:

```bash
pip install denial
```

You can also quickly try out this and other packages without having to install using [instld](https://github.com/pomponchik/instld).


## The second `None`

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

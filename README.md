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

However, we can't all use sentinel objects from some built-in module if we don't need the functionality of that module. Until the [PEP](https://peps.python.org/pep-0661/) has been adopted on this topic, it is better to use a special package containing only this primitive. Such a package is `denial`. It defines just such an object: `None` for situations where you need to distinguish `None` as a value from the user, and `None` as a designation that something is really undefined. This value should not fall "outside", into the user's space, it should remain only inside the libraries implementations. In addition, this library offers a special class that allows you to create your own sentinels.


## Table of contents

- [**Installation**](#installation)
- [**The second None**](#the-second-none)
- [**Your own None objects**](#your-own-none-objects)
- [**Type hinting**](#type-hinting)
- [**Analogues**](#analogues)


## Installation

Install it:

```bash
pip install denial
```

You can also quickly try out this and other packages without having to install using [instld](https://github.com/pomponchik/instld).


## The second `None`

This library defines an object that is proposed to be used in almost the same way as a regular `None`. This is how it is imported:

```python
from denial import InnerNone
```

This object is equal only to itself:

```python
print(InnerNone == InnerNone)
#> True
print(InnerNone == False)
#> False
```

This object is also an instance of [`InnerNoneType`](#your-own-none-objects) class (an analog of [`NoneType`](https://docs.python.org/3/library/types.html#types.NoneType), however, is not inherited from this), which makes it possible to check through [`isinstance`](https://docs.python.org/3/library/functions.html#isinstance):

```python
from denial import InnerNoneType

print(isinstance(InnerNone, InnerNoneType))
#> True
```

Like `None`, `InnerNone` (as well as all other `InnerNoneType` objects) always returns `False` when cast to `bool`:

```python
print(bool(InnerNone))
#> False
```

> ⓘ It is recommended to use the `InnerNone` object inside libraries where a value close to `None` is required, but meaning a situation where the value is not really set, rather than set as `None`. This object should be completely isolated from the user code space. None of the public methods of your library should return this object.


## Your own `None` objects

If `None` and [`InnerNone`](#the-second-none) are not enough for you, you can create your own similar objects by instantiating `InnerNoneType`:

```python
sentinel = InnerNoneType()
```

This object will also be equal only to itself:

```python
print(sentinel == sentinel)
#> True

print(sentinel == InnerNoneType())  # Comparison with another object of the same type
#> False
print(sentinel == InnerNone)  # Also comparison with another object of the same type
#> False
print(sentinel == None)  # Comparison with None
#> False
print(sentinel == 123)  # Comparison with an arbitrary object
#> False
```

You can also pass an integer or a string to the class constructor. An `InnerNoneType` object is equal to another such object with the same argument:

```python
print(InnerNoneType(123) == InnerNoneType(123))
#> True
print(InnerNoneType('key') == InnerNoneType('key'))
#> True

print(InnerNoneType(123) == InnerNoneType(1234))
#> False
print(InnerNoneType('key') == InnerNoneType('another key'))
#> False
print(InnerNoneType(123) == InnerNoneType())
#> False
print(InnerNoneType(123) == 123)
#> False
```

> 💡 Any `InnerNoneType` objects can be used as keys in dictionaries.


## Type hinting

> When used in a type hint, the expression `None` is considered equivalent to `type(None)`.

> *[Official typing documentation](https://typing.python.org/en/latest/spec/special-types.html#none)*

`None` is a special value for which Python type checkers make an exception, allowing it to be used as an annotation of its own type. Unfortunately, this behavior cannot be reproduced without changing the internal implementation of existing type checkers, which I would not expect until the [PEP](https://peps.python.org/pep-0661/) is adopted.

Therefore, it is suggested to use class `InnerNoneType` as a type annotation:

```python
def function(default: int | InnerNoneType):
    ...
```

In case you need a universal annotation for `None` and [`InnerNoneType`](#your-own-none-objects) objects, use the `SentinelType` annotation:

```python
from denial import SentinelType

variable: SentinelType = InnerNone
variable: SentinelType = InnerNoneType()
variable: SentinelType = None  # All 3 annotations are correct.
```


## Analogues

The problem of distinguishing types of uncertainty is often faced by programmers and they solve it in a variety of ways. This problem concerns all programming languages, because it ultimately describes our *knowledge*, and the questions of cognition are universal for everyone. And everyone (including me!) has [*their own opinions*](https://en.wikipedia.org/wiki/Not_invented_here) on how to solve this problem.

![standards](https://imgs.xkcd.com/comics/standards.png)
> *Current state of affairs*

Some programming languages are a little better thought out in this matter than Python. For example, [JavaScript](https://en.wikipedia.org/wiki/JavaScript) explicitly distinguishes between `undefined` and `null`. I think this is due to the fact that [form](https://en.wikipedia.org/wiki/HTML_form) validation is often written in JS, and it often requires such a distinction. However, this approach is not completely universal, since in the general case the number of layers of uncertainty is infinite, and here there are only 2 of them. In contrast, `denial` provides both features: the basic [`InnerNone`](#the-second-none) constant for simple cases and the ability to create an unlimited number of [`InnerNoneType`](#your-own-none-objects) instances for complex ones. Other languages, such as [AppleScript](https://en.wikipedia.org/wiki/AppleScript) and [SQL](https://en.wikipedia.org/wiki/SQL), also distinguish several different types of undefined values. A separate category includes the languages [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language)), [Haskell](https://en.wikipedia.org/wiki/Haskell), [OCaml](https://en.wikipedia.org/wiki/OCaml), and [Swift](https://en.wikipedia.org/wiki/Swift_(programming_language)), which use algebraic data types.

The Python standard library uses at least [15 sentinel objects](https://mail.python.org/archives/list/python-dev@python.org/message/JBYXQH3NV3YBF7P2HLHB5CD6V3GVTY55/):

- **_collections_abc: __marker__**
- **cgitb.__UNDEF__**
- **configparser: _UNSET**
- **dataclasses: _HAS_DEFAULT_FACTORY, MISSING, KW_ONLY**
- **datetime.timezone._Omitted**
- **fnmatch.translate() STAR**
- **functools.lru_cache.sentinel** (each @lru_cache creates its own sentinel object)
- **functools._NOT_FOUND**
- **heapq**: temporary sentinel in nsmallest() and nlargest()
- **inspect._sentinel**
- **inspect._signature_fromstr()** invalid
- **plistlib._undefined**
- **runpy._ModifiedArgv0._sentinel**
- **sched: _sentinel**
- **traceback: _sentinel**

Since the language itself does not regulate this in any way, there is chaos and code duplication. Before creating this library, I used one of them, but later realized that importing a module that I don't need for anything other than sentinel is a bad idea.

Not only did I come to this conclusion, the community also tried to standardize it. A standard for sentinels was proposed in [PEP-661](https://peps.python.org/pep-0661/), but at the time of writing it has still not been adopted, as there is no consensus on a number of important issues. This topic was also indirectly raised in [PEP-484](https://peps.python.org/pep-0484/), as well as in [PEP-695](https://peps.python.org/pep-0695/) and in [PEP-696](https://peps.python.org/pep-0696/). Unfortunately, while there is no "official" solution, everyone is still forced to reinvent the wheel on their own. Some, such as [Pydantic](https://github.com/pydantic/pydantic/issues/12090), are proactive, as if `PEP-661` has already been adopted. Personally, I don't like the solution proposed in `PEP-661`, mainly because of the implementation examples that suggest using a global registry of all created sentinels, which can lead to memory leaks and concurrency limitations.

In addition to `denial`, there are many packages with sentinels in [`Pypi`](https://pypi.org/). For example, there is the [sentinel](https://pypi.org/project/sentinel/) library, but its API seemed to me overcomplicated for such a simple task. The [sentinels](https://pypi.org/project/sentinels/) package is quite simple, but in its internal implementation it also relies on the [global registry](https://github.com/vmalloc/sentinels/blob/37e67ed20d99aa7492e52316e9af7f930b9ac578/sentinels/__init__.py#L11) and contains some other code defects. The [sentinel-value](https://github.com/vdmit11/sentinel-value) package is very similar to `denial`, but I did not see the possibility of autogenerating sentinel ids there. Of course, there are other packages that I haven't reviewed here.

And of course, there are still different ways to implement primitive sentinels in your code in a few lines of code without using third-party packages.

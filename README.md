# nones

[![Downloads](https://static.pepy.tech/badge/nones/month)](https://pepy.tech/project/nones)
[![Downloads](https://static.pepy.tech/badge/nones)](https://pepy.tech/project/nones)
[![Coverage Status](https://coveralls.io/repos/github/pomponchik/nones/badge.svg?branch=main)](https://coveralls.io/github/pomponchik/nones?branch=main)
[![Lines of code](https://sloc.xyz/github/pomponchik/nones/?category=code)](https://github.com/boyter/scc/)
[![Hits-of-Code](https://hitsofcode.com/github/pomponchik/nones?branch=main&label=Hits-of-Code&exclude=docs/)](https://hitsofcode.com/github/pomponchik/nones/view?branch=main)
[![Test-Package](https://github.com/pomponchik/nones/actions/workflows/tests_and_coverage.yml/badge.svg)](https://github.com/pomponchik/nones/actions/workflows/tests_and_coverage.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/nones.svg)](https://pypi.python.org/pypi/nones)
[![PyPI version](https://badge.fury.io/py/nones.svg)](https://badge.fury.io/py/nones)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/pomponchik/nones)


There is a small but annoying misunderstanding in the design of Python as a language. The language defines the constant `None`, which designates a special object that is used as a "stub" when it is not possible to use the "real" value. But sometimes, when implementing libraries, it is not possible to distinguish `None`, passed by the user as the default value, from `None`, which means that the value is *really undefined*. In some rare cases, this distinction is important.

For example, the [dataclasses](https://docs.python.org/3/library/dataclasses.html) library defines a special [MISSING](https://docs.python.org/3/library/dataclasses.html#dataclasses.MISSING) constant for such cases. This is used to separate the cases when the user has not set a default value from the case when he has set `None` as the default value.

This library defines just such an object: None for situations where you need to distinguish None as a value from the user, and None as a designation that something is really undefined. This value should not fall "outside", into the user's space, it should remain only inside the library implementation.

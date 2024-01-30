# Khulnasoft Checks Base

[![Latest PyPI version][1]][7]
[![Supported Python versions][2]][7]

## Overview

This package provides the Python bits needed by the [Khulnasoft Agent][4]
to run Agent-based Integrations (also known as _Checks_).

This package is used in two scenarios:

1. When used from within the Python interpreter embedded in the Agent, it
provides all the base classes and utilities needed by any Check.

2. When installed in a local environment with a regular Python interpreter, it
mocks the presence of a running Agent so checks can work in standalone mode,
mostly useful for testing and development.

Please refer to the [docs][5] for details.

## Installation

Checks from [integrations-core][6] already
use the toolkit in a transparent way when you run the tests but you can
install the toolkit locally and play with it:

```shell
pip install khulnasoft-checks-base
```

## Troubleshooting

Need help? Contact [Khulnasoft support][8].

[1]: https://img.shields.io/pypi/v/khulnasoft-checks-base.svg
[2]: https://img.shields.io/pypi/pyversions/khulnasoft-checks-base.svg
[4]: https://github.com/KhulnaSoft/khulnasoft-agent
[5]: https://khulnasofthq.dev/integrations-core/base/about/
[6]: https://github.com/KhulnaSoft/integrations-core
[7]: https://pypi.org/project/khulnasoft-checks-base/
[8]: https://docs.khulnasoft.com/help/

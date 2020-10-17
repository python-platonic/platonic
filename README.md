# platonic

[![Build Status](https://travis-ci.com/python-platonic/platonic.svg?branch=master)](https://travis-ci.com/python-platonic/platonic)
[![Coverage](https://coveralls.io/repos/github/python-platonic/platonic/badge.svg?branch=master)](https://coveralls.io/github/python-platonic/platonic?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/platonic.svg)](https://pypi.org/project/platonic/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![PyPI - License](https://img.shields.io/pypi/l/platonic)

Abstract data structures for Clean Architecture applications in Python. Amazon services, brokers, and backends represented as queues, mappings, lists, iterables, and more.

## Example 

```python
# TODO
```


# Available data structures

|                 | queue | iterable | dict | list | set | graph |
| ---             | ---   | ---      | ---  | ---  | --- | ---   |
| Amazon DynamoDB | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| Amazon SimpleDB | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| Amazon SQS      | ✔    ️| 🔧       | ❌    | 🔧   | 🔧  | 🔧    |
| Amazon S3       | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| Apache Kafka    | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| Local FS        | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| MongoDB         | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| MySQL           | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| OrientDB        | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| PostgreSQL      | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |
| Redis           | 🔧    | 🔧       | 🔧   | 🔧   | 🔧  | 🔧    |


## Installation

```bash
pip install platonic
```

## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [3cb37d9e138d83958c4d915a3b3aa737b27b6418](https://github.com/wemake-services/wemake-python-package/tree/3cb37d9e138d83958c4d915a3b3aa737b27b6418). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/3cb37d9e138d83958c4d915a3b3aa737b27b6418...master) since then.

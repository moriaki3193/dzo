# dzo
**This package is not ready for production use!!!**

## Overview
![MIT](https://img.shields.io/pypi/l/dzo.svg)
![version](https://img.shields.io/pypi/v/dzo.svg)
![pyversions](https://img.shields.io/pypi/pyversions/dzo.svg)
![codecov](https://codecov.io/gh/moriaki3193/dzo/branch/master/graph/badge.svg)

Python implemented portable and easy-to-use search engine.

## Installation
```shell
# just for use.
$ pip install dzo

# for developers.
$ git clone git@github.com:moriaki3193/dzo.git
$ pip install -e .[dev]  # installs extra dependencies for development.
```

## Usage
### Command line tool
#### Make inverted indices
```shell
# Local directory
$ dzo preprocess <target_dir> <result_path>

# e.g.
$ dzo preprocess ./data/products ./data/inverted-index.pkl
```

#### Search
```shell
$ dzo search <query> --index-path <index_path>

# e.g.
$ dzo search おにぎり --index-path ./data/inverted-index.pkl
```

### Python package
**WIP**

## Development
### Commands
```shell
# Building cython extensions.
$ make build/ext

# Linting
$ make check/lint

# Type hinting
$ make check/type

# Running tests using pytest.
$ make test

# Other utility commands are available.
# See Makefile for more details.
```

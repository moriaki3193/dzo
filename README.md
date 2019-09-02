# dzo
**This package is not ready for production use!!!**

## Overview
![MIT](https://img.shields.io/pypi/l/dzo.svg)
[![version](https://img.shields.io/pypi/v/dzo.svg)](https://pypi.org/project/dzo/)
![pyversions](https://img.shields.io/pypi/pyversions/dzo.svg)
![codecov](https://codecov.io/gh/moriaki3193/dzo/branch/master/graph/badge.svg)
[![CircleCI](https://circleci.com/gh/moriaki3193/dzo/tree/master.svg?style=svg)](https://circleci.com/gh/moriaki3193/dzo/tree/master)

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
# display help
$ dzo preprocess -h

# Local directory
## 1. n-gram tokenization
$ dzo preprocess <target_dir> <result_path>
### e.g.
$ dzo preprocess ./data/products ./inverted-index.pkl

## 2. mecab tokenization
$ dzo preprocess --tokenizer=mecab --dicdir=<dicdir> <target_dir> <result_path>
### e.g.
$ dzo preprocess --tokenizer=mecab --dicdir=/usr/local/lib/mecab/dic/ipadic ./data ./inverted-index.pkl
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
### Note
Style of all docstrings for functions and methods have to be **Google Style Python Docstring**. Please refer to [napoleon style guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

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

# Look up dictionary directories for MeCab
$ make list/dicdir

# Other utility commands are available.
# See Makefile for more details.
```

## Sponsors
<div style='max-width: 50px;'>

[![Recipio Inc.](./.images/recipio-logo.png)](http://about.recipio.jp/)
</div>

# dzo
Python (& partially Cython for optimization) implemented portable and easy-to-use search engine.

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

# e.g.
$ dzo search おにぎり --index-path ./data/inverted-index.pkl --dicdir=/usr/local/lib/mecab/dic/ipadic
```

### Python package
You can easily implement your own inverted index preprocessor and search engine. A brief example is below.

#### Impl your own preprocessor
Let's assume that we have a CSV file which contains a lots of (id, artist) like below.

```csv
id,artist
1,Red Hot Chili Peppers
2,Oasis
3,Arctic Monkeys
4,Rage Against The Machines
5,Gorillaz
...
```

You can implement your own ad-hoc preprocessor by inheriting **AbstractLoader**. All loaders inheriting this abstract class must have an implementation of `load()` instance method.

```python
from typing import List

import MeCab
import pandas as pd

from dzo.annot import Document
from dzo.base import AbstractLoader


class AdHocPandasLoader(AbstractLoader):

    def load(self) -> List[Document]:  # type hinting is optional.
        df = pd.read_csv(PATH_TO_CSV, usecols=['id', 'artist'])

        docs: List[Document] = []

        for idx, row in df.iterrows():
            doc = Document(idx, row['artist'])
            docs.append(doc)

        return docs
```

Since all classes inheriting **AbstractLoader** are valid as a protocol **annot.Loader**, so all you have to do from now on is choose **Tokenizer**, and then pass those `AdHocPandasLoader` and the tokenizer to **Preprocessor**.

```python
from dzo.tokenizer import WhitespaceTokenizer


loader = AdHocPandasLoader()
tokenizer = WhitespaceTokenizer()

preprocessor = Preprocessor(loader, tokenizer)
inv_index = preprocessor.preprocess()

# You can save the inverted index so as to use it later.
preprocessor.save(inv_index, '/path/to/inv-index.pkl')
```

Other useful tokeinzer classes are implemented. Please see [dzo.tokenizer](./dzo/tokenizer) subpackage.

#### Impl your own search engine
After you dump the inverted index as above, you can implement your own search engine using the index.

```python
from dzo.engine import Engine


engine = Engine('/path/to/index.pkl')
tokenizer = WhitespaceTokenizer()
```

Yes! That's all. Let's try the search engine like below.

```python
# Let's search!!!
# >>> query = 'Chili'
# >>> engine.search(query)
# [1]  ← since ID for 'Red Hot Chili Peppers' is 1
```

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

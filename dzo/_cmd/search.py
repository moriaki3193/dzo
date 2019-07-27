# -*- coding: utf-8 -*-
"""Search command script.
"""
from argparse import Namespace

from . import ExitStatus
from ..engine import Engine
from ..tokenizer import NGramTokenizer


def search(args: Namespace) -> ExitStatus:
    """search
    """
    query: str = args.query
    index_path: str = args.index_path
    print(f'Query: {query}')
    print(f'Index Path: {index_path}')
    tokenizer = NGramTokenizer()
    engine = Engine(index_path, tokenizer)
    print('Engine is ready...')
    results = engine.search(query)
    print(results)
    return ExitStatus.SUCCESS

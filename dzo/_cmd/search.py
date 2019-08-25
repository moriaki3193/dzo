# -*- coding: utf-8 -*-
"""Search command script.
"""
from argparse import Namespace
from typing import Optional

from . import ExitStatus
from ..engine import Engine


def search(args: Namespace) -> ExitStatus:
    """search
    """
    query: str = args.query
    index_path: str = args.index_path
    dicdir: Optional[str] = args.dicdir if hasattr(args, 'dicdir') else None

    print(f'Query: {query}')
    print(f'Index Path: {index_path}')
    if dicdir is not None:
        print(f'MeCab Dictionary: {dicdir}')

    engine = Engine(index_path, dicdir=dicdir)

    print('Engine is ready...')

    results = engine.search(query)

    print(results)

    return ExitStatus.SUCCESS

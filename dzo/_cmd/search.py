# -*- coding: utf-8 -*-
"""Search command script.
"""
from argparse import Namespace

from . import ExitStatus


def search(args: Namespace) -> ExitStatus:
    """search
    """
    query: str = args.query
    print(f'Query: {query}')
    return ExitStatus.SUCCESS

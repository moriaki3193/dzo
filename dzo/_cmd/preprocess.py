# -*- coding: utf-8 -*-
"""Preprocess command script.
"""
from argparse import Namespace

from . import ExitStatus
from ..indexer import InvIndex
from ..preprocess import Preprocessor
from ..tokenizer import NGramTokenizer


def preprocess(args: Namespace) -> ExitStatus:
    """preprocess
    """
    try:
        preprocessor = Preprocessor(args.target_dir)
        ngram_tokenizer = NGramTokenizer()
        inv_index: InvIndex
        if hasattr(args, 'ignored_exts'):
            inv_index = preprocessor.preprocess(
                ngram_tokenizer,
                ignored_exts=set(args.ignored_exts))
        else:
            inv_index = preprocessor.preprocess(ngram_tokenizer)
        preprocessor.save(inv_index, args.result_path)
    except FileNotFoundError as err:
        print(err)
        return ExitStatus.ERROR_NOT_EXECUTABLE
    return ExitStatus.SUCCESS

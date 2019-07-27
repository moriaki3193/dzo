# -*- coding: utf-8 -*-
"""Preprocess command script.
"""
from argparse import Namespace

from . import ExitStatus
from ..preprocess import Preprocessor
from ..tokenizer import NGramTokenizer


def preprocess(args: Namespace) -> ExitStatus:
    """preprocess
    """
    try:
        preprocessor = Preprocessor(args.target_dir)
        ngram_tokenizer = NGramTokenizer()
        if hasattr(args, 'ignored_exts'):
            preprocessor.preprocess(ngram_tokenizer, ignored_exts=set(args.ignored_exts))
        else:
            preprocessor.preprocess(ngram_tokenizer)
        # preprocessor.save()
    except FileNotFoundError as err:
        print(err)
        return ExitStatus.ERROR_NOT_EXECUTABLE
    return ExitStatus.SUCCESS

# -*- coding: utf-8 -*-
"""Preprocess command script.
"""
from argparse import Namespace
from os import path

import MeCab

from . import ExitStatus
from ..annot import Tokenizer
from ..indexer import InvIndex
from ..loader import DirectoryLoader
from ..preprocess import Preprocessor
from ..tokenizer.mecab import MeCabTokenizer
from ..tokenizer.ngram import NGramTokenizer


def preprocess(args: Namespace) -> ExitStatus:
    """preprocess
    """
    try:
        directory_loader = DirectoryLoader(args.target_dir)
        # parse --tokenizer option
        tokenizer: Tokenizer
        if hasattr(args, 'tokenizer'):
            # NGramTokenizer
            if args.tokenizer == 'ngram':
                tokenizer = NGramTokenizer(n=3)
            # MeCabTokenizer
            elif args.tokenizer == 'mecab':
                if not hasattr(args, 'dicdir'):
                    msg = '--dicdir has to be set when --tokenizer is mecab'
                    raise ValueError(msg)
                d = args.dicdir
                if not path.isdir(d):
                    raise FileNotFoundError
                tagger = MeCab.Tagger(d)
                tokenizer = MeCabTokenizer(tagger)
            # Invalid tokenizer handler
            else:
                msg = 'value for --tokenizer option has to be one either `mecab` or `ngram`'
                raise ValueError(msg)

        preprocessor = Preprocessor(directory_loader, tokenizer)

        # parse --ignore option
        inv_index: InvIndex
        if hasattr(args, 'ignored_exts'):
            inv_index = preprocessor.preprocess(ignored_exts=set(args.ignored_exts))
        else:
            inv_index = preprocessor.preprocess()

        preprocessor.save(inv_index, args.result_path)
    except FileNotFoundError as err:
        print(err)
        return ExitStatus.ERROR_NOT_EXECUTABLE
    except ValueError as err:
        print(err)
        return ExitStatus.ERROR_INVALID_USAGE

    return ExitStatus.SUCCESS

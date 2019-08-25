# -*- coding: utf-8 -*-
"""Engine module
"""
import os
import logging
import pickle
from os import path
from typing import Optional, Tuple

import MeCab

from ._meta import _VERSION
from .indexer import InvIndex
from .tokenizer import MeCabTokenizer, NGramTokenizer
from .tokenizer.base import TokenizerBase


class Engine:
    """Engine class.
    """

    def __init__(
            self,
            index_path: str,
            dicdir: Optional[str] = None
        ) -> None:
        """Initialize the search engine.
        """
        _inv_index, _tokenizer = self.__load_inv_index(index_path, dicdir)

        logging.info('Loaded inverted index')

        self._inv_index = _inv_index
        self._tokenizer = _tokenizer

    @staticmethod
    def __load_inv_index(
            index_path: str,
            dicdir: Optional[str]
        ) -> Tuple[InvIndex, TokenizerBase]:
        """Load inverted index.
        """
        name: str
        version: str
        inv_index: InvIndex

        tokenizer: TokenizerBase

        if not path.exists(index_path):
            raise FileNotFoundError
        with open(index_path, mode='rb') as fp:
            name, version, inv_index = pickle.load(fp)

        if version != _VERSION:
            msg = f'Versions differ: current {_VERSION}, index {version}'
            logging.warning(msg)

        if name == MeCabTokenizer.name:
            if dicdir is None:
                msg = 'dicdir should not be None set when the index was made by MeCabTokenizer'
                raise ValueError(msg)
            if not os.path.isdir(dicdir):
                raise FileNotFoundError(f'not found: {dicdir}')
            tagger = MeCab.Tagger(dicdir)
            tokenizer = MeCabTokenizer(tagger)
        elif name == NGramTokenizer.name:
            tokenizer = NGramTokenizer(n=3)  # TODO retrive `n`
        else:
            raise ValueError(f'name of the inverted index is invalid')

        return inv_index, tokenizer

    def search(self, query: str) -> list:  # TODO type hinting
        """Returns search results.

        Parameters:
            query: a search query, represented as a string.

        Returns:
            results: WIP
        """
        tokens = self._tokenizer.tokenize(query)
        results = []
        for token in tokens:
            if token.get_normalized() in self._inv_index.keys():
                results.extend([name for name in self._inv_index[token.get_normalized()].keys()])
        return results

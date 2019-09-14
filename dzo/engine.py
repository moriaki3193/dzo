# -*- coding: utf-8 -*-
"""Engine module
"""
import os
from os import path
import logging
import pickle
from typing import Optional, Tuple

import MeCab

from .annot import Tokenizer
from .const import _VERSION
from .indexer import InvIndex
from .tokenizer import MeCabTokenizer, NGramTokenizer


class Engine:
    """Engine class.
    """

    version: str = _VERSION

    def __init__(
            self,
            index_path: str,
            dicdir: Optional[str] = None
        ) -> None:
        """Initialize the search engine.
        """
        _inv_index: InvIndex
        _tokenizer: Tokenizer
        _inv_index, _tokenizer = self.__load_inv_index(index_path, dicdir)

        logging.info('Loaded inverted index')

        self._inv_index = _inv_index
        self._tokenizer = _tokenizer

    def __load_inv_index(
            self,
            index_path: str,
            dicdir: Optional[str]
        ) -> Tuple[InvIndex, Tokenizer]:
        """Load inverted index.
        """
        name: str
        version: str
        inv_index: InvIndex

        tokenizer: Tokenizer

        if not path.exists(index_path):
            raise FileNotFoundError
        with open(index_path, mode='rb') as fp:
            name, version, inv_index = pickle.load(fp)

        if version != self.version:
            msg = f'Versions differ: current {self.version}, index {version}'
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
            if token.normalized in self._inv_index.keys():
                results.extend([name for name in self._inv_index[token.normalized].keys()])
        return results

# -*- coding: utf-8 -*-
"""Engine module
"""
import logging
import pickle
from os import path

from ._meta import __VERSION
from .indexer import InvIndex
from .tokenizer.base import TokenizerBase


class Engine:
    """Engine class.
    """

    def __init__(
            self,
            index_path: str,
            tokenizer: TokenizerBase,
        ) -> None:
        """Initialize the search engine.
        """
        self._inv_index = self.__load_inv_index(index_path)

        logging.info('Loaded inverted index')

        self._tokenizer = tokenizer

    @staticmethod
    def __load_inv_index(index_path: str) -> InvIndex:
        version: str
        inv_index: InvIndex

        if not path.exists(index_path):
            raise FileNotFoundError
        with open(index_path, mode='rb') as fp:
            _, version, inv_index = pickle.load(fp)

        if version != __VERSION:
            msg = f'Versions differ: current {__VERSION}, index {version}'
            logging.warning(msg)

        return inv_index

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

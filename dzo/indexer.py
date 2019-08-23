# -*- coding: utf-8 -*-
"""Indexer module
"""
from typing import Dict, List, NamedTuple


Index = Dict[str, List[int]]                 # {'<Token>': [<Position>, ...]}
FullIndex = Dict[str, Dict[str, List[int]]]  # {'<DocumentID>': {'<Token>': [<Position>, ...]}}
InvIndex = Dict[str, Dict[str, List[int]]]   # {'<Token>': {'<DocumentID>': [<Position>, ...]}}


class NamedIndex(NamedTuple):
    """Index with its document title.
    """
    name: str
    idx: Index


class Indexer:
    """An ordinary indexer class.
    """

    @staticmethod
    def make_index(tokens: List[str]) -> Index:
        """Make an index for a document (represented as a list of tokens).

        Example:
            >>> tokens = ['すもも', 'も', 'もも', 'も', 'もも', 'の', 'うち']
            >>> Indexer.make_index(tokens)
            >>> {'すもも': [0], 'も': [1, 3], 'もも', [2, 4], 'の': [5], 'うち': [6]}

        Args:
            tokens: A list of strings in a document.

        Returns:
            An index of the document.
        """
        index: Index = {}
        for i, token in enumerate(tokens):
            if token in index.keys():
                index[token].append(i)
            else:
                index[token] = [i]
        return index

    @staticmethod
    def merge(named_indices: List[NamedIndex]) -> FullIndex:
        """Merge a list of named indices, and returns full index.

        Example:
            >>> first_idx = NamedIndex('first', {
            ...     'すもも': [0], 'も': [1, 3], 'もも': [2, 4], 'の': [5], 'うち': [6]
            ... })
            >>> second_idx = NamedIndex('second', {
            ...     'もも': [0], 'くり': [1], 'さんねん': [2], 'かき': [3], 'はちねん': [4]
            ... })
            >>> Indexer.merge([first_idx, second_idx])
            >>> {
            >>>     'first': {
            >>>         'すもも': [0],
            >>>         'も': [1, 3],
            >>>         'もも': [2, 4],
            >>>         'の': [5],
            >>>         'うち': [6],
            >>>     },
            >>>     'second': {
            >>>         'もも': [0],
            >>>         'くり': [1],
            >>>         'さんねん': [2],
            >>>         'かき': [3],
            >>>         'はちねん': [4],
            >>>     },
            >>> }

        Args:
            named_indices: A list of named indices.

        Returns:
            A full index of given indices.
        """
        return {name: idx for name, idx in named_indices}

    @staticmethod
    def make_inv_index(full_index: FullIndex) -> InvIndex:
        """Make an inverted index from full index.

        Example:
            >>> first_idx = NamedIndex('first', {
            ...     'すもも': [0], 'も': [1, 3], 'もも': [2, 4], 'の': [5], 'うち': [6]
            ... })
            >>> second_idx = NamedIndex('second', {
            ...     'もも': [0], 'くり': [1], 'さんねん': [2], 'かき': [3], 'はちねん': [4]
            ... })
            >>> full_idx = Indexer.merge([first_idx, second_idx])
            >>> Indexer.make_inv_index(full_idx)
            >>> {
            >>>     'すもも': {'first': [0]},
            >>>     'も': {'first': [1, 3]},
            >>>     'もも': {'first': [2, 4], 'second': [0]},
            >>>     'の': {'first': [5]},
            >>>     'うち': {'first': [6]},
            >>>     'くり': {'second': [1]},
            >>>     'さんねん': {'second': [2]},
            >>>     'かき': {'second': [3]},
            >>>     'はちねん': {'second': [4]},
            >>> }

        Args:
            full_index: A full index which is returned by Indexer.merge() method.

        Returns:
            An inverted index of given documents.
        """
        inv_index: InvIndex = {}
        for name, index in full_index.items():
            for token in index.keys():
                if token in inv_index.keys():
                    if name in inv_index[token].keys():
                        inv_index[token][name].extend(index[token][:])
                    else:
                        inv_index[token][name] = index[token]
                else:
                    inv_index[token] = {name: index[token]}
        return inv_index

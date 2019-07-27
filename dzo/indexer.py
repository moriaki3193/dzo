# -*- coding: utf-8 -*-
"""Indexer module
"""
from typing import Dict, List, NamedTuple


Index = Dict[str, List[int]]
FullIndex = Dict[str, Dict[str, List[int]]]
InvIndex = Dict[str, Dict[str, List[int]]]


class NamedIndex(NamedTuple):
    """Index with its document title.
    """
    name: str
    index: Index


class Indexer:
    """An ordinary indexer class.
    """

    @staticmethod
    def make_index(tokens: List[str]) -> Index:
        """Make an index for a document (represented as a list of tokens).
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
        """
        return {name: index for name, index in named_indices}

    @staticmethod
    def make_inv_index(full_index: FullIndex) -> InvIndex:
        """Make an inverted index from full index.
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

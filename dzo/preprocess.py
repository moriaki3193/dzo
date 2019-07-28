# -*- coding: utf-8 -*-
"""Preprocess module
"""
import pickle
from os import path
from typing import List, Optional, Set

from .indexer import Indexer, NamedIndex, InvIndex
from .loader import DirectoryLoader
from .tokenizer.base import TokenizerBase


def _extr_ext(p: str) -> str:
    """Extract a file extension.
    """
    fname = path.basename(p)
    _, ext = path.splitext(fname)
    return ext


# TODO parallelization: tokenization & indexing steps
class Preprocessor:
    """Preprocess pipeline class.
    """

    def __init__(
            self,
            loader: DirectoryLoader,
            tokenizer: TokenizerBase) -> None:
        self._loader = loader
        self._tokenizer = tokenizer

    def preprocess(self, ignored_exts: Optional[Set[str]] = None) -> InvIndex:
        """A preprocessing pipeline.
        """
        docs = self._loader.load(ignored_exts=ignored_exts)
        # Make inverted index
        named_indices: List[NamedIndex] = []
        for doc in docs:
            tokens = self._tokenizer.tokenize(doc.content)
            normalized_tokens = [t.get_normalized() for t in tokens]
            index = Indexer.make_index(normalized_tokens)
            named_indices.append(NamedIndex(doc.name, index))
        full_index = Indexer.merge(named_indices)
        inv_index = Indexer.make_inv_index(full_index)
        return inv_index

    @staticmethod
    def save(inv_index: InvIndex, result_path: str) -> None:
        """save the results of preprocess pipeline.
        """
        if path.exists(result_path):
            raise FileExistsError
        with open(result_path, mode='wb') as fp:
            pickle.dump(inv_index, fp)

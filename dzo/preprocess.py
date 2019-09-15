# -*- coding: utf-8 -*-
"""Preprocess module
"""
import logging
import pickle
from os import path
from typing import List, Optional, Set

from .annot import Tokenizer
from .indexer import Indexer, NamedIndex, InvIndex
from .loader import DirectoryLoader


def _extr_ext(p: str) -> str:
    """Extract a file extension.

    Example:
        >>> p = '/path/to/file.ext'
        >>> _extr_ext(p)
        >>> '.ext'

    Args:
        p: a file path.

    Returns:
        ext: an extension of the file.
    """
    fname = path.basename(p)
    _, ext = path.splitext(fname)
    return ext


class Preprocessor:
    """Preprocess pipeline class.

    Todo:
        - parallelization: tokeninzation & indexing steps
    """

    def __init__(
            self,
            loader: DirectoryLoader,
            tokenizer: Tokenizer
        ) -> None:
        self._loader = loader
        self._tokenizer = tokenizer

    def preprocess(self, ignored_exts: Optional[Set[str]] = None) -> InvIndex:
        """A preprocessing pipeline.

        This method consists of some steps;
        1) Loading documents (loaders are in charge of this step).
        2) Tokenization (tokenizers are in chargs of this step).
        3) Make an inverted index of documents represented as a series of tokens.

        Args:
            ignored_exts: File extensions to be ignored. Defaults to None.

        Returns:
            An inverted index.
        """
        if (isinstance(self._loader, DirectoryLoader)) and (ignored_exts is not None):
            exts = ', '.join(ignored_exts)
            msg = f'Files whose extension is {exts} will be ignored'
            logging.info(msg)

        docs = self._loader.load(ignored_exts=ignored_exts)

        # Make inverted index
        named_indices: List[NamedIndex] = []
        for doc in docs:
            tokens = self._tokenizer.tokenize(doc.content)
            normalized_tokens = [t.normalized for t in tokens]
            index = Indexer.make_index(normalized_tokens)
            named_indices.append(NamedIndex(doc.name, index))
        full_index = Indexer.merge(named_indices)
        inv_index = Indexer.make_inv_index(full_index)
        return inv_index

    def save(self, inv_index: InvIndex, result_path: str) -> None:
        """save the results of preprocess pipeline.
        """
        if path.exists(result_path):
            raise FileExistsError
        with open(result_path, mode='wb') as fp:
            obj = (self._tokenizer.name, self._tokenizer.version, inv_index)
            pickle.dump(obj, fp)

        msg = f'Successfully saved the inverted index to {result_path}'
        logging.info(msg)

# -*- coding: utf-8 -*-
"""Preprocess module
"""
import glob
import pickle
from os import path
from typing import List, Optional, Set

from .indexer import Indexer, NamedIndex, InvIndex
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

    def __init__(self, target_dir: str) -> None:
        if path.isdir(target_dir):
            self.target_dir = target_dir
        else:
            raise FileNotFoundError(f'Not found {target_dir}')

    def _load_dir(self, ignored_exts: Optional[Set[str]]) -> List[str]:
        """Returns file paths included in target directory.

        Parameters:
            ignored_exts: file extensions to be ignored. e.g. {'.py', '.so'}

        Returns:
            file_paths: a list of file paths.
        """
        pathname = path.join(self.target_dir, '**')
        file_paths = glob.glob(pathname, recursive=True)
        if ignored_exts is None:
            return [p for p in file_paths if path.isfile(p)]
        valid_paths = [p for p in file_paths if _extr_ext(p) not in ignored_exts]
        return [p for p in valid_paths if path.isfile(p)]

    def preprocess(
            self,
            tokenizer: TokenizerBase,
            ignored_exts: Optional[Set[str]] = None) -> InvIndex:
        """A preprocessing pipeline.
        """
        # Load files
        file_paths = self._load_dir(ignored_exts=ignored_exts)
        if not file_paths:
            raise FileNotFoundError('The directory seems to be empty')
        # Make inverted index
        named_indices: List[NamedIndex] = []
        for file_path in file_paths:
            with open(file_path, mode='r') as fp:
                sentence = fp.read().replace('\n', '')
                tokens = tokenizer.tokenize(sentence)
                normalized_tokens = [token.get_normalized() for token in tokens]
            index = Indexer.make_index(normalized_tokens)
            named_indices.append(NamedIndex(file_path, index))
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

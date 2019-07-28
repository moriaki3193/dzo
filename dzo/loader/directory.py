# -*- coding: utf-8 -*-
"""DirectoryLoader module
"""
import glob
import logging
import os.path
from typing import List, NamedTuple, Optional, Set


class _Document(NamedTuple):
    """A document class
    """
    name: str
    content: str


class DirectoryLoader:
    """DirectoryLoader is a utility class for loading documents from a local directory.
    """

    def __init__(self, target_dir: str) -> None:
        if os.path.isdir(target_dir):
            self._target_dir = target_dir
        else:
            raise FileNotFoundError(f'Not found {target_dir}')

    @staticmethod
    def _extr_ext(p: str) -> str:
        """Extracts a file extension.
        """
        file_name = os.path.basename(p)
        _, ext = os.path.splitext(file_name)
        return ext

    def _get_file_paths(self, ignored_exts: Optional[Set[str]]) -> List[str]:
        """Returns file paths included in target directory.

        Parameters:
            ignored_exts: file extensions to be ignored. e.g. {'.py', '.so'}

        Returns:
            file_paths: a list of file paths.
        """
        dir_path = os.path.join(self._target_dir, '**')
        all_paths = glob.glob(dir_path, recursive=True)
        if ignored_exts is None:
            return [p for p in all_paths if os.path.isfile(p)]
        file_paths = [p for p in all_paths if self._extr_ext(p) not in ignored_exts]
        return [p for p in file_paths if os.path.isfile(p)]

    def load(self, ignored_exts: Optional[Set[str]] = None) -> List[_Document]:
        """Load the target directory and load all of the files.
        """
        # Read file paths
        file_paths = self._get_file_paths(ignored_exts=ignored_exts)
        if not file_paths:
            raise FileNotFoundError('The directory seems to be empty')
        # Read all files
        docs: List[_Document] = []
        invalid_doc_paths: List[str] = []
        for file_path in file_paths:
            with open(file_path, mode='r') as fp:
                try:
                    content = fp.read().replace('\n', '')
                except UnicodeDecodeError:
                    invalid_doc_paths.append(file_path)
            docs.append(_Document(file_path, content))
        if not invalid_doc_paths:
            listed_paths = '\n'.join(invalid_doc_paths)
            msg = f'Files in the following paths seem to be binary files:\n{listed_paths}'
            logging.warning(msg)
        return docs

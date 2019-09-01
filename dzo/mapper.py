# -*- coding: utf-8 -*-
"""Mapper module.
"""
import json
import os
from typing import Dict, MutableMapping, Optional, Sequence, Set


class SynonymMap:
    """Synonym mapping class.

    Methods:
        lookup
        register
        unregister

    Example:
        >>> fp = '/path/to/synonym_map.json'
        >>> synonym_map: Synonym = maps.read_synonym(fp)
        >>> keyword = 'おにぎり'  # registered ones
        >>> synonym_map.lookup(keyword)
        ['おむすび', 'にぎり']
        >>> unk_keyword = 'UNKNOWN'
        >>> synonym_mpa.lookup(unk_keyword)
        None
    """

    def __init__(self, m: MutableMapping[str, Sequence[str]]) -> None:
        table: Dict[str, Set[str]] = {}
        for k, v in m.items():
            if k in table.keys():
                table[k] = table[k].union(v)
            else:
                table[k] = set(v)
        self._table = table

    def lookup(self, kw: str) -> Optional[Set[str]]:
        """Lookup synonyms of the given keyword.

        Args:
            kw: a keyword.

        Returns:
            a set of synonyms.

        Example:
            >>> kw = 'おにぎり'  # known keyword
            >>> synonym_map.lookup(kw)
            {'おむすび', '握り飯', 'ライスボール'}
            >>> unk_kw = 'UNKNOWN'  # unknown keyword
            None
        """
        return self._table.get(kw)

    def register(self, kw: str, vs: Sequence[str]) -> None:
        """Register a new synonym mapping.

        Args:
            kw: a keyword.
            vs: a set of synonyms.
        """
        if self._table.get(kw) is not None:
            self._table[kw] = self._table[kw].union(vs)
        else:
            self._table[kw] = set(vs)

    def unregister(self, kw: str, vs: Optional[Sequence[str]] = None) -> None:
        """Unregister a mapping which is already registered.

        If `vs` is not None, this method try to remove keywords whose key is `kw`.

        Args:
            kw: a keyword.
            vs: a set of synonyms.

        Example:
            >>> kw = 'おにぎり'
            >>> synonym_map.lookup(k)
            {'おむすび', '握り飯', 'ライスボール'}
            >>> synonym_map.unregister(kw, ['握り飯'])
            >>> synonym_map.lookup(k)
            {'おむすび', 'ライスボール'}
            >>> synonym_map.unregister(kw)
            >>> synonym_map.lookup(k)
            None
        """
        if vs is None:
            _ = self._table.pop(kw)
            return
        if self._table.get(kw) is not None:
            self._table[kw] = {s for s in self._table[kw] if s not in vs}


def read_synonym(p: str, fmt: str = 'json') -> SynonymMap:
    """Read synonym mapping table from the specified path and returns SynonymMap instance.

    Args:
        p: a path to the synonym mapping file.
        fmt: format of the file.

    Returns:
        synonym mapping table object.
    """
    valid_formats = {'json'}

    if fmt not in valid_formats:
        msg = f'arg `fmt` must be one of ({", ".join(valid_formats)})'
        raise ValueError(msg)

    if not os.path.isfile(p):
        msg = f'file not found: {p}'
        raise FileNotFoundError(msg)

    m: MutableMapping[str, Sequence[str]]

    with open(p, mode='r') as fp:
        if fmt == 'json':
            m = json.load(fp)

    return SynonymMap(m)

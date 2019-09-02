# -*- coding: utf-8 -*-
"""Testing mapper module.
"""
import json
import os
import tempfile
from uuid import uuid4

import pytest

from dzo import mapper
from dzo.mapper import SynonymMap


synonyms = {
    'おにぎり': ['おむすび', '握り飯'],
    '牛乳': ['ミルク'],
}


def test_read_synonym() -> None:
    """Test for mapper.read_synonyms() function.
    """
    with tempfile.TemporaryDirectory() as tp:
        # should raise FileNotFoundError.
        invalid_path = os.path.join(tp, f'{uuid4()}.json')
        with pytest.raises(FileNotFoundError):
            mapper.read_synonym(invalid_path)

        # should raise ValueError.
        invalid_fmt = 'foobar'
        with pytest.raises(ValueError):
            p = os.path.join(tp, f'{uuid4()}.{invalid_fmt}')
            mapper.read_synonym(p, fmt=invalid_fmt)

        # should be an instance of SynonymMap.
        p = os.path.join(tp, 'synonyms.json')
        with open(p, mode='w') as fp:
            json.dump(synonyms, fp, ensure_ascii=False)
        got = mapper.read_synonym(p, fmt='json')
        assert isinstance(got, SynonymMap)

def test_SynonymMap() -> None:
    """Test for mapper.SynonymMap class.
    """
    synonym_map = SynonymMap(synonyms)

    # should return None.
    got = synonym_map.lookup('foo')
    assert got is None

    # should return a list of strings.
    got = synonym_map.lookup('おにぎり')
    want = {'おむすび', '握り飯'}
    assert isinstance(got, set)
    assert got == want

    # should be updated: 'ライスボール' will be registered.
    synonym_map.register('おにぎり', ['ライスボール'])
    got = synonym_map.lookup('おにぎり')
    want = {'おむすび', '握り飯', 'ライスボール'}
    assert got == want

    # should be updated: 'ハリーポッター' will be registered.
    synonym_map.register('ハリーポッター', ['ハリポタ'])
    got = synonym_map.lookup('ハリーポッター')
    want = {'ハリポタ'}
    assert isinstance(got, set)
    assert got == want

    # should be updated: 'ライスボール' will be unregistered.
    synonym_map.unregister('おにぎり', ['ライスボール'])
    got = synonym_map.lookup('おにぎり')
    want = {'おむすび', '握り飯'}
    assert got == want

    # should be updated: 'おにぎり' key will be removed.
    synonym_map.unregister('おにぎり')
    got = synonym_map.lookup('おにぎり')
    assert got is None

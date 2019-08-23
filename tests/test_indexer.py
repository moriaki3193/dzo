# -*- coding: utf-8 -*-
"""Testing indexer module.
"""
from dzo import indexer
from dzo.indexer import Indexer


def test_Indexer_make_index() -> None:
    """Test for Indexer.make_index() static method.
    """
    # check result
    tokens = ['すもも', 'も', 'もも', 'も', 'もも', 'の', 'うち']
    got = Indexer.make_index(tokens)
    want: indexer.Index = {
        'すもも': [0],
        'も': [1, 3],
        'もも': [2, 4],
        'の': [5],
        'うち': [6],
    }
    assert got == want

def test_Indexer_merge() -> None:
    """Test for Indexer.merge() static method.
    """
    named_indices = [
        indexer.NamedIndex('first', {
            'すもも': [0],
            'も': [1, 3],
            'もも': [2, 4],
            'の': [5],
            'うち': [6],
        }),
        indexer.NamedIndex('second', {
            'もも': [0],
            'くり': [1],
            'さんねん': [2],
            'かき': [3],
            'はちねん': [4],
        }),
    ]
    got = Indexer.merge(named_indices)
    want: indexer.FullIndex = {
        'first': {
            'すもも': [0],
            'も': [1, 3],
            'もも': [2, 4],
            'の': [5],
            'うち': [6],
        },
        'second': {
            'もも': [0],
            'くり': [1],
            'さんねん': [2],
            'かき': [3],
            'はちねん': [4],
        },
    }
    assert got == want

def test_Indexer_make_inv_index() -> None:
    """Test for Indexer.make_inv_index() static method.
    """
    full_idx: indexer.FullIndex = {
        'first': {
            'すもも': [0],
            'も': [1, 3],
            'もも': [2, 4],
            'の': [5],
            'うち': [6],
        },
        'second': {
            'もも': [0],
            'くり': [1],
            'さんねん': [2],
            'かき': [3],
            'はちねん': [4],
        },
    }
    got = Indexer.make_inv_index(full_idx)
    want: indexer.InvIndex = {
        'すもも': {'first': [0]},
        'も': {'first': [1, 3]},
        'もも': {'first': [2, 4], 'second': [0]},
        'の': {'first': [5]},
        'うち': {'first': [6]},
        'くり': {'second': [1]},
        'さんねん': {'second': [2]},
        'かき': {'second': [3]},
        'はちねん': {'second': [4]},
    }
    assert got == want

# -*- coding: utf-8 -*-
"""Testing whitespace module.
"""
from dzo.tokenizer import WhitespaceTokenizer


def test_WhitespaceTokenizer_tokenize() -> None:
    """Test for tokenizer.WhitespaceTokenizer().tokenize method.
    """
    sentence = 'super ultra  hyper    miracle　romantic sentence'  # contains full-width space
    got = WhitespaceTokenizer().tokenize(sentence)
    want = ['super', 'ultra', 'hyper', 'miracle', 'romantic', 'sentence']
    assert isinstance(got, list)
    assert got == want

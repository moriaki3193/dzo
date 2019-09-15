# -*- coding: utf-8 -*-
"""Testing ngram module.
"""
from dzo.tokenizer import NGramTokenizer
from dzo.tokenizer.ngram import NGramToken


def test_NGramToken() -> None:
    """Test for NGramToken.
    """
    token = NGramToken('a')

    assert hasattr(token, 'surface')

    assert token.normalized == 'a'


def test_NGramTokenizer_tokenize() -> None:
    """Test for tokenizer.NGramTokenizer().tokenize method.
    """
    tokenizer = NGramTokenizer(n=3)

    # long enough
    sentence = '吾輩は猫である'
    res = tokenizer.tokenize(sentence)
    got = [tok.normalized for tok in res]
    want = ['吾輩は', '輩は猫', 'は猫で', '猫であ', 'である']
    assert isinstance(res, list)
    assert isinstance(res[0], NGramToken)
    assert got == want

    # short one
    sentence = 'はい'
    res = tokenizer.tokenize(sentence)
    got = [tok.normalized for tok in res]
    want = ['はい']
    assert got == want

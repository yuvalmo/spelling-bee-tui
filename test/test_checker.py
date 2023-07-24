import pytest

from typing import Iterable, Type

from src.checker import WordChecker
from src.dictionary import NullDict
from src.errors import BadLetters, MissingCenterLetter, TooShort
from src.letters import Letters


def checker():
    return WordChecker(Letters("a", "bcdefg"), d=NullDict())


def expect_raise_list(
    checker: WordChecker,
    error: Type,
    words: Iterable[str]
) -> None:
    ''' Expect each word to raise an exception when checked
    by the given checker.
    '''
    for word in words:
        with pytest.raises(error):
            checker.check(word)


def test_has_enough_letters():
    wc = checker()

    expect_raise_list(wc, TooShort, (
        "a",
        "ab",
        "abc",
    ))

    assert wc.check("aaaa")
    assert wc.check("aaaaa")


def test_contains_central_letter():
    wc = checker()

    expect_raise_list(wc, MissingCenterLetter, (
        "bcde",
        "cbde",
    ))

    assert wc.check("abcde")
    assert wc.check("bacde")
    assert wc.check("bcade")
    assert wc.check("bcdae")
    assert wc.check("bcdea")


def test_contains_only_valid_letters():
    wc = checker()

    expect_raise_list(wc, BadLetters, (
        "abcdek",
        "afcbdm",
    ))

    assert wc.check("abcdefg")


def test_cannot_contain_whitespace():
    wc = checker()

    expect_raise_list(wc, BadLetters, (
        "a bcde",
        "ab cde",
        "abc de",
        "abcd e",
        "a bcd e",
    ))


def test_is_pangram():
    wc = checker()

    assert not wc.is_pangram("abcdef")
    assert not wc.is_pangram("abcdeg")

    assert wc.is_pangram("abcdefg")
    assert wc.is_pangram("gfedcba")

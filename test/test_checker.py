from src.checker import WordChecker
from src.dictionary import NullDict
from src.letters import Letters


def checker():
    return WordChecker(Letters("a", "bcdefg"), d=NullDict())


def test_has_enough_letters():
    wc = checker()

    assert not wc.check("a")
    assert not wc.check("ab")
    assert not wc.check("abc")

    assert wc.check("aaaa")
    assert wc.check("aaaaa")


def test_contains_central_letter():
    wc = checker()

    assert not wc.check("bcde")
    assert not wc.check("cbde")

    assert wc.check("abcde")
    assert wc.check("bacde")
    assert wc.check("bcade")
    assert wc.check("bcdae")
    assert wc.check("bcdea")


def test_contains_only_valid_letters():
    wc = checker()

    assert not wc.check("abcdek")
    assert not wc.check("afcbdm")

    assert wc.check("abcdefg")


def test_cannot_contain_whitespace():
    wc = checker()

    assert not wc.check("a bcde")
    assert not wc.check("ab cde")
    assert not wc.check("abc de")
    assert not wc.check("abcd e")
    assert not wc.check("a bcd e")


def test_is_pangram():
    wc = checker()

    assert not wc.is_pangram("abcdef")
    assert not wc.is_pangram("abcdeg")

    assert wc.is_pangram("abcdefg")
    assert wc.is_pangram("gfedcba")

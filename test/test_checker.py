from src.checker import WordChecker


def test_has_enough_letters():
    wc = WordChecker("a", "bcde")

    assert not wc.check("a")
    assert not wc.check("ab")
    assert not wc.check("abc")

    assert wc.check("aaaa")
    assert wc.check("aaaaa")


def test_contains_central_letter():
    wc = WordChecker("a", "bcde")

    assert not wc.check("bcde")
    assert not wc.check("cbde")

    assert wc.check("abcde")
    assert wc.check("bacde")
    assert wc.check("bcade")
    assert wc.check("bcdae")
    assert wc.check("bcdea")


def test_contains_only_valid_letters():
    wc = WordChecker("a", "bcde")

    assert not wc.check("abcdef")
    assert not wc.check("afcbde")

    assert wc.check("abcde")


def test_cannot_contain_whitespace():
    wc = WordChecker("a", "bcde")

    assert not wc.check("a bcde")
    assert not wc.check("ab cde")
    assert not wc.check("abc de")
    assert not wc.check("abcd e")
    assert not wc.check("a bcd e")


def test_is_pangram():
    wc = WordChecker("a", "bcde")

    assert not wc.is_pangram("abcd")
    assert not wc.is_pangram("abce")

    assert wc.is_pangram("abcde")
    assert wc.is_pangram(str(reversed("abcde")))

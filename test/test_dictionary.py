from src.dictionary import NullDict, Enchant


def test_null_dict():
    d = NullDict()

    assert d.check("asdasdasd")
    assert d.check("12334345345")


def test_echant():
    d = Enchant()

    assert not d.check("hllo")
    assert not d.check("attck")
    assert not d.check("extnction")

    assert d.check("hello")
    assert d.check("attack")
    assert d.check("extinction")

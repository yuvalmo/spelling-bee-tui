import pytest
from src.letters import Letters


def test_throws_on_wrong_input():
    with pytest.raises(ValueError, match="central letter"):
        Letters("ab", "cdefgh")

    with pytest.raises(ValueError, match="only .* letters"):
        Letters("a", "cdefghgg")

    with pytest.raises(ValueError, match="only .* letters"):
        Letters("a", "cdefg")

    with pytest.raises(ValueError, match="only letters"):
        Letters("a", "bcdef1")

    with pytest.raises(ValueError, match="only letters"):
        Letters("1", "bcdefg")

    with pytest.raises(ValueError, match="must be unique"):
        Letters("a", "ccdefg")

    with pytest.raises(ValueError, match="must be unique"):
        Letters("a", "cadefg")


def test_accepts_valid_input():
    Letters("a", "bcdefg")
    Letters("l", "aehivy")
    Letters("p", "ghinow")

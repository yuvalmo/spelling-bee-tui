import pytest

from src.game import Game
from src.letters import Letters


def game() -> Game:
    return Game(Letters("l", "aehivy"))


correct = [
    "heal",
    "heel",
    "hill",
    "hall",
]

wrong = [
    "l",
    "hhhh",
    "hvll",
]


def test_can_be_created():
    g = game()

    assert g.score == 0
    assert g.answers == []


def test_score():
    g = game()

    assert 0 == g.score_word("a")
    assert 0 == g.score_word("aa")
    assert 0 == g.score_word("aaa")

    # 4-letter words score 1 point
    assert 1 == g.score_word("a"*4)
    assert 1 == g.score_word("b"*4)

    # Longer words score 1 point per letter
    assert 5 == g.score_word("a"*5)
    assert 6 == g.score_word("a"*6)
    assert 9 == g.score_word("a"*9)

    # Pangrams are worth 7 extra points
    assert 14 == g.score_word("heavily")
    assert 14 == g.score_word("laehivy")


def test_score_increases():
    g = game()

    for word in correct:
        score = g.score
        g.try_word(word)
        assert score < g.score 


def test_remembers_past_answers():
    g = game()
    a = []

    for word in correct:
        g.try_word(word)
        a.append(word)
        assert word in g.answers
        assert a == g.answers


@pytest.mark.parametrize("word", wrong)
def test_does_not_accept_wrong_word(word):
    g = game()

    with pytest.raises(ValueError):
        g.try_word(word)

    assert g.score == 0
    assert g.answers == []


@pytest.mark.parametrize("word", correct)
def test_does_not_accept_same_word_twice(word):
    g = game()
    g.try_word(word)

    with pytest.raises(ValueError):
        g.try_word(word)

    assert g.answers == [word]

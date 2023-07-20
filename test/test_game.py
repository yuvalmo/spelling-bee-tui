from src.game import Game
from src.letters import Letters


def game() -> Game:
    return Game(Letters("l", "aehivy"))


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

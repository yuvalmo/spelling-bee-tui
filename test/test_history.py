from pathlib import Path
from tempfile import TemporaryDirectory

from src.game import Game
from src.history import History
from src.letters import Letters


def test_filename():
    l = Letters("a", "bcdefg")
    assert "abcdefg" == History.filename(l)

    l = Letters("a", "cefgbd")
    assert "abcdefg" == History.filename(l)

    l = Letters("y", "temnia")
    assert "yaeimnt" == History.filename(l)


def test_load_not_found():
    l = Letters("y", "temnia")

    with TemporaryDirectory() as td:
        path = Path(td)
        hist = History(path)
        assert not hist.load(l)


def test_save_first_time():
    l = Letters("y", "temnia")

    game = Game(l)
    game.try_word("tiny")
    game.try_word("teeny")
    game.try_word("entity")
    game.try_word("amenity")

    with TemporaryDirectory() as td:
        path = Path(td)
        hist = History(path)

        # Save game
        hist.save(game)
        assert (path / "yaeimnt").exists()

        # Load it
        loaded = hist.load(l)

    assert loaded

    loaded_game = Game(l)
    for w in loaded:
        loaded_game.try_word(w)

    assert game.score == loaded_game.score
    assert game.answers == loaded_game.answers


def test_save_overwrite():
    l = Letters("y", "temnia")

    game = Game(l)
    game.try_word("tiny")
    game.try_word("teeny")

    with TemporaryDirectory() as td:
        path = Path(td)
        hist = History(path)

        # Save game
        hist.save(game)
        assert (path / "yaeimnt").exists()

        game.try_word("entity")
        game.try_word("amenity")

        # Save game again
        hist.save(game)
        assert (path / "yaeimnt").exists()

        # Load it
        loaded = hist.load(l)

    assert loaded

    loaded_game = Game(l)
    for w in loaded:
        loaded_game.try_word(w)

    assert game.score == loaded_game.score
    assert game.answers == loaded_game.answers


def test_reset():
    l = Letters("y", "temnia")

    game = Game(l)
    game.try_word("tiny")
    game.try_word("teeny")

    with TemporaryDirectory() as td:
        path = Path(td)
        hist = History(path)

        # Save once
        hist.save(game)

        # Delete save
        hist.reset(l)

        # Try to load
        loaded = hist.load(l)

    assert not loaded

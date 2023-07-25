from pathlib import Path
from tempfile import TemporaryDirectory

from src import save
from src.game import Game
from src.letters import Letters


def test_filename():
    l = Letters("a", "bcdefg")
    assert "abcdefg" == save.filename(l)

    l = Letters("a", "cefgbd")
    assert "abcdefg" == save.filename(l)

    l = Letters("y", "temnia")
    assert "yaeimnt" == save.filename(l)


def test_load_not_found():
    l = Letters("y", "temnia")

    with TemporaryDirectory() as td:
        assert not save.load(l, Path(td))


def test_save_first_time():
    l = Letters("y", "temnia")

    game = Game(l)
    game.try_word("tiny")
    game.try_word("teeny")
    game.try_word("entity")
    game.try_word("amenity")

    with TemporaryDirectory() as td:
        path = Path(td)

        # Save game
        save.save(game, path)
        assert (path / "yaeimnt").exists()

        # Load it
        loaded = save.load(l, path)

    assert loaded
    assert game.score == loaded.score
    assert game.answers == loaded.answers


def test_save_overwrite():
    l = Letters("y", "temnia")

    game = Game(l)
    game.try_word("tiny")
    game.try_word("teeny")

    with TemporaryDirectory() as td:
        path = Path(td)

        # Save game
        save.save(game, path)
        assert (path / "yaeimnt").exists()

        game.try_word("entity")
        game.try_word("amenity")

        # Save game again
        save.save(game, path)
        assert (path / "yaeimnt").exists()

        # Load it
        loaded = save.load(l, path)

    assert loaded
    assert game.score == loaded.score
    assert game.answers == loaded.answers

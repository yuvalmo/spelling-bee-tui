''' A module to take care of save management.

Its API includes:
- Save a game to fs.
- Load a game from fs.
- Reset a save.
'''
import json

from pathlib import Path
from typing import List

from .game import Game
from .letters import Letters


DEFAULT_PATH = Path.home() / ".sbee"


def save(game: Game, path: Path = DEFAULT_PATH) -> None:
    path = savepath(game.letters, path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as file:
        json.dump(game.answers, file, indent=2)


def load(letters: Letters,
         path: Path = DEFAULT_PATH) -> List[str]:
    path = savepath(letters, path)

    if not path.exists():
        return []

    with open(path) as file:
        answers = json.load(file)

    return answers


def reset(letters: Letters,
          path: Path = DEFAULT_PATH) -> None:
    path = savepath(letters, path)
    path.unlink(missing_ok=True)


def filename(letters: Letters) -> str:
    center = letters.central
    others = letters.letters
    return center + ''.join(sorted(others))


def savepath(letters: Letters,
             path: Path = DEFAULT_PATH) -> Path:
    return path / filename(letters)

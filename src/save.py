import json

from pathlib import Path
from typing import List

from .game import Game
from .letters import Letters


DEFAULT_PATH = Path.home() / ".sbee"


def save(game: Game, path: Path = DEFAULT_PATH) -> None:
    path.mkdir(parents=True, exist_ok=True)
    path = path / filename(game.letters)

    with path.open("w") as file:
        json.dump(game.answers, file, indent=2)


def load(letters: Letters,
         path: Path = DEFAULT_PATH) -> List[str]:
    path = path / filename(letters)

    if not path.exists():
        return []

    with open(path) as file:
        answers = json.load(file)

    return answers


def filename(letters: Letters) -> str:
    center = letters.central
    others = letters.letters
    return center + ''.join(sorted(others))

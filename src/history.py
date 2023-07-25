import json

from pathlib import Path
from typing import List

from .game import Game
from .letters import Letters


class History:
    ''' This class manages past games and saves.
    '''
    DEFAULT_PATH = Path.home() / ".sbee"

    def __init__(self,
                 path: Path = DEFAULT_PATH) -> None:
        self.path = path
        
    def save(self, game: Game) -> None:
        path = self.getpath(game.letters)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w") as file:
            json.dump(game.answers, file, indent=2)

    def load(self, letters: Letters,) -> List[str]:
        path = self.getpath(letters)

        if not path.exists():
            return []

        with open(path) as file:
            answers = json.load(file)

        return answers

    def reset(self, letters: Letters) -> None:
        path = self.getpath(letters)
        path.unlink(missing_ok=True)

    def getpath(self, letters: Letters) -> Path:
        return self.path / self.filename(letters)

    @staticmethod
    def filename(letters: Letters) -> str:
        center = letters.central
        others = letters.letters
        return center + ''.join(sorted(others))

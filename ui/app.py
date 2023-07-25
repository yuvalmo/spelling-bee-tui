from textual.app import App, ComposeResult
from textual.widgets import Footer, Input
from textual.containers import Center, Container, Vertical

from src.errors import SpellingBeeError
from src.game import Game
from src.history import History
from src.letters import Letters

from .answers import Answers, Word
from .widgets import textbox, title
from .error import Error
from .hive import Hive
from .info import info


class SpellingBee(App):
    ''' Spelling Bee app.
    '''
    CSS_PATH = "style.css"

    BINDINGS = [
        ("ctrl+r", "shuffle_hive", "Shuffle letters")
    ]

    def __init__(self, letters: Letters):
        super().__init__()
        self._letters = letters
        self._game = Game(letters)

    def compose(self) -> ComposeResult:
        yield info()
        with Vertical():
            yield title()
            with Container(id="main-panel"):
                yield textbox(self._letters)
                with Center():
                    yield Error()
                yield Hive(self._letters)
        yield Answers()
        yield Footer()

    def on_mount(self) -> None:
        answers = History().load(self._letters)
        if not answers:
            return
        for word in answers:
            self.check_word(word)

    def on_exit_app(self) -> None:
        if self._game.answers:
            History().save(self._game)

    def action_shuffle_hive(self):
        self.query_one(Hive).shuffle()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if not event.value:
            return
        self.check_word(event.value.lower())

    def check_word(self, word: str) -> None:
        try:
            self._game.try_word(word)
            self.query_one(Answers).add(Word(
                value = word,
                score = self._game.score_word(word),
                pangram = self._game.checker.is_pangram(word)
            ))
        except SpellingBeeError as err:
            self.query_one(Error).set(str(err))

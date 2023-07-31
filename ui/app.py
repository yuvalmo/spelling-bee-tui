from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Input
from textual.containers import Center, Container, Vertical

from src.errors import SpellingBeeError
from src.game import Game

from .answers import Answers, Word
from .widgets import textbox, title
from .error import Error
from .hive import Hive
from .info import info


class SpellingBee(App[Game]):
    ''' Spelling Bee app.
    '''
    CSS_PATH = "style.css"

    BINDINGS = [
        Binding("ctrl+r", "shuffle_hive", "Shuffle letters"),
        Binding("ctrl+c", "quit", "Quit", priority=True)
    ]

    def __init__(self, game: Game):
        super().__init__()
        self._letters = game.letters
        self._game = game

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
        if not self._game.answers:
            return

        # If this is a continued game, populate answers
        #   from history.
        for word in self._game.answers:
            self.populate_answers(word)

    def action_quit(self) -> None:
        self.exit(self._game)

    def action_shuffle_hive(self):
        self.query_one(Hive).shuffle()

    @on(Input.Submitted, selector="#textbox")
    def on_input_submitted(self, event: Input.Submitted) -> None:
        word = event.value

        # No point in checking an empty word
        if not word:
            return

        try:
            self._game.try_word(word)
            self.populate_answers(word)
        except SpellingBeeError as err:
            self.populate_error(str(err))

    def populate_answers(self, word: str) -> None:
        self.query_one(Answers).add(Word(
            value = word,
            score = self._game.score_word(word),
            pangram = self._game.checker.is_pangram(word)
        ))

    def populate_error(self, msg: str) -> None:
        self.query_one(Error).set(msg)

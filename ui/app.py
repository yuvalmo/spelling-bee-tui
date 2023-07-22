from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Input, Static

from src.letters import Letters
from src.game import Game

from .hive import Hive
from .answers import Answers, Word
from .highlighter import BeeHighlighter


class Textbox(Input):
    DEFAULT_CLASSES = "box"
    
    def __init__(self, letters: Letters):
        super().__init__(
            id="textbox",
            highlighter=BeeHighlighter(letters)
        )
        self.border_title = "Enter Word"


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
        title = '''
the
New York Times
presents:

The Spelling Bee
'''

        yield Static(title, id="title", classes="box")
        yield Textbox(self._letters)
        yield Answers()
        yield Hive(self._letters)
        yield Footer()

    def action_shuffle_hive(self):
        self.query_one(Hive).shuffle()

    @on(Input.Submitted)
    def check_word(self, event: Input.Submitted) -> None:
        word = event.value

        try:
            self._game.try_word(word)
            self.query_one(Answers).add(Word(
                value = word,
                score = self._game.score_word(word),
                pangram = self._game.checker.is_pangram(word)
            ))
        except ValueError:
            pass  # TODO: Show error message

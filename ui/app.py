from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Input, Static

from src.letters import Letters

from .hive import Hive
from .answers import Answers
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

    def compose(self) -> ComposeResult:
        title ='''
the
New York Times
presents:

The Spelling Bee
'''

        yield Static(title, id="title", classes="box")
        yield Textbox(self._letters)
        yield Answers(self._letters)
        yield Hive(self._letters)
        yield Footer()

    def action_shuffle_hive(self):
        self.query_one(Hive).shuffle()

    @on(Input.Submitted)
    def check_word(self, event: Input.Submitted) -> None:
        # TODO: Replace with event
        self.query_one(Answers).check(event.value)

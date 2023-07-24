''' Here we define the basic components who do not deserve
their own file.
'''

from textual.containers import Center
from textual.widget import Widget
from textual.widgets import Input, Static

from src.letters import Letters

from .highlighter import BeeHighlighter


TITLE = "Spelling Bee"


def title() -> Widget:
    return Static(TITLE, id="title", classes="panel")


def textbox(letters: Letters) -> Widget:
    hl = BeeHighlighter(letters)

    return Center(
        Input(
            id="textbox",
            placeholder="Enter word...",
            highlighter=hl
        )
    )

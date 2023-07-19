#!/bin/env python3

from textual.app import App, ComposeResult
from textual.widgets import Footer, Static


class Title(Static):
    DEFAULT_CLASSES = "box"


class Hive(Static):
    DEFAULT_CLASSES = "box"


class Textbox(Static):
    DEFAULT_CLASSES = "box"
    pass


class Wordlist(Static):
    DEFAULT_CLASSES = "box"
    pass


class SpellingBee(App):
    ''' Spelling Bee app.
    '''
    CSS_PATH = "style.css"

    BINDINGS = [
        ("ctrl+r", "shuffle_hive", "Shuffle letters")
    ]

    def compose(self) -> ComposeResult:
        title ='''
the
New York Times
presents:

The Spelling Bee
'''

        yield Title(title, id="title")
        yield Textbox(id="textbox")
        yield Wordlist(id="wordlist")
        yield Hive(id="hive")
        yield Footer()

    def action_shuffle_hive(self):
        pass

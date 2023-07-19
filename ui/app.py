#!/bin/env python3

from textual.app import App, ComposeResult
from textual.widgets import Footer, Static

from .hive import Hive


class Title(Static):
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

    def __init__(self, center: str, letters: str):
        super().__init__()
        self._center = center
        self._letters = letters

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
        yield Hive(self._center, self._letters)
        yield Footer()

    def action_shuffle_hive(self):
        self.query_one("Hive").shuffle()

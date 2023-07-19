#!/bin/env python3

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Input, Static

from src.checker import WordChecker

from .hive import Hive


class Title(Static):
    DEFAULT_CLASSES = "box"


class Textbox(Input):
    DEFAULT_CLASSES = "box"
    
    def __init__(self):
        super().__init__(id="textbox")
        self.border_title = "Enter word:"


class Wordlist(Static):
    DEFAULT_CLASSES = "box"

    def __init__(self, center: str, letters: str):
        super().__init__(id="wordlist")
        self._c = WordChecker(center, letters)

    def check(self, word: str):
        if self._c.check(word):
            self.update(word)


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
        yield Textbox()
        yield Wordlist(self._center, self._letters)
        yield Hive(self._center, self._letters)
        yield Footer()

    def action_shuffle_hive(self):
        self.query_one("Hive").shuffle()

    @on(Input.Submitted)
    def check_word(self, event: Input.Submitted) -> None:
        self.query_one("Wordlist").check(event.value)

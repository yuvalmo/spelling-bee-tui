#!/bin/env python3

from os import linesep

from rich.console import RenderableType

from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Footer, Input, Static

from src.game import Game
from src.letters import Letters

from .hive import Hive


class Title(Static):
    DEFAULT_CLASSES = "box"


class Textbox(Input):
    DEFAULT_CLASSES = "box"
    
    def __init__(self):
        super().__init__(id="textbox")
        self.border_title = "Enter word:"


class Answers(Static):
    DEFAULT_CLASSES = "box"

    score = reactive(0)
    answers = reactive(list())

    def __init__(self, letters: Letters):
        super().__init__(id="answers")
        self._game = Game(letters)

    def check(self, word: str):
        try:
            self._game.try_word(word)
            self.score = self._game.score
            self.answers = self._game.answers
        except ValueError:
            pass  # TODO: Show error message

    def render(self) -> RenderableType:
        self.border_title = f"{self.score} Points"

        # TODO: Show in columns
        return linesep.join(sorted(self.answers))


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

        yield Title(title, id="title")
        yield Textbox()
        yield Answers(self._letters)
        yield Hive(self._letters)
        yield Footer()

    def action_shuffle_hive(self):
        self.query_one("Hive").shuffle()

    @on(Input.Submitted)
    def check_word(self, event: Input.Submitted) -> None:
        # TODO: Replace with event
        self.query_one("Answers").check(event.value)

import re

from termcolor import colored


def highlight(text: str, substr: str) -> str:
    ''' Highlight the given substring in the given text.
    '''
    return re.sub(substr, colored(substr, "yellow"), text)


def bold(text: str) -> str:
    ''' Make the given text bold.
    '''
    return colored(text, attrs=["bold"])

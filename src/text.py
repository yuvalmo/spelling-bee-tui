import re
from typing import Optional
from termcolor import colored


def highlight(text: str,
              substr: Optional[str] = None) -> str:
    ''' Highlight the given substring in the given text.
    If no substring is given, highlight the whole text.
    '''
    substr = substr or text
    return re.sub(substr, colored(substr, "yellow"), text)


def bold(text: str) -> str:
    ''' Make the given text bold.
    '''
    return colored(text, attrs=["bold"])

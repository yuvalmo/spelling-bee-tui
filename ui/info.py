from textual.containers import Container
from textual.widget import Widget
from textual.widgets import Markdown

LINK = "https://www.nytimes.com/puzzles/spelling-bee"

INFO_TEXT = f'''
*How to Play*

Create as many words using letters from the hive.

Words must:
* Contain the center letter.
* Contain at least 4 letters.

Letters can be used more than once.

Each puzzle includes at least one `pangram`, which uses every letter.

*Score*

* 4 letters -> `1p`
* 5 or more -> `1p` per letter
* pangram   -> `+7p`

See original game [here]({LINK}).

© New York Times
'''


def info() -> Widget:
    return Container(
        Markdown(INFO_TEXT),
        id="info",
        classes="panel"
    )

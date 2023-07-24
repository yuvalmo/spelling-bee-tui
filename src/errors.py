''' Custom spelling bee exceptions.
'''

class SpellingBeeError(Exception):
    msg: str = ""
    
    def __init__(self) -> None:
        super().__init__(self.msg)

class TooShort(SpellingBeeError):
    msg = "Too short"

class MissingCenterLetter(SpellingBeeError):
    msg = "Missing center letter"

class BadLetters(SpellingBeeError):
    msg = "Bad letters"

class NotInWordList(SpellingBeeError):
    msg = "Not in word list"

class AlreadyFound(SpellingBeeError):
    msg = "Already found"

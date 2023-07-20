

class Letters:
    ''' Packs together the chosen letters for a game
    of spelling bee.
    '''
    LEN = 6

    def __init__(self, central: str, letters: str):
        self.central = central.lower()
        self.letters = letters.lower()

        Letters.check_input(self.central, self.letters)

    @property
    def all(self) -> str:
        return self.central + self.letters

    @staticmethod
    def check_input(central: str, letters: str):
        if len(central) != 1:
            raise ValueError("Cannot have more than one central letter")

        if len(letters) != Letters.LEN:
            raise ValueError("Must have only {Letters.LEN} letters")

        if not letters.isalpha() or not central.isalpha():
            raise ValueError("Must contain only letters")

        if len(letters) != len(set(letters)):
            raise ValueError("Each letter must be unique")

        if central in letters:
            raise ValueError("Each letter must be unique")

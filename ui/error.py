from textual.widgets import Static


class Error(Static):

    def __init__(self) -> None:
        super().__init__(id="error-msg")
        self.styles.opacity = 0.0

    def set(self, msg: str) -> None:
        self.update(msg)

        # Make visible
        self.styles.opacity = 1.0

        # Animate fade-out
        self.styles.animate(
            "opacity",
            value=0.0,
            delay=1.0,
            duration=0.2
        )

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer
from textual.widgets import Button
from musicpy import *


class MusicPad(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CHORDS_MAPPING = {
        "C": ("C", 3),
        "G": ("G", 2),
        "Am": ("Am", 2),
        "Em": ("Em", 2),
        "F": ("F", 2),
    }

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # args = self.CHORDS_MAPPING[event.button.id]
        default_args = (2, 1 / 4, 1 / 8)
        chord = C(event.button.id, *default_args) * 2
        play(chord, bpm=100, instrument=25)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Grid(
            Button("F", id="F", variant="success"),
            Button("C", id="C", variant="success"),
            Button("Dm", id="Dm", variant="success"),
            Button("Bb", id="Bb", variant="success"),
            Button("Am", id="Am", variant="success"),
        )
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = MusicPad()
    app.run()

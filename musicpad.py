from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal
from textual.widgets import Header, Footer
from textual.widgets import Button
from musicpy import *


class MusicPad(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = "musicpad.tcss"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # args = self.CHORDS_MAPPING[event.button.id]
        default_args = (2, 1 / 4, 1 / 8)

        if event.button.id.startswith("chord-"):
            chord = str(event.button.id).replace("chord-", "")
            chord = C(chord, *default_args) * 2
            play(chord, bpm=100, instrument=25)

        if event.button.id == "drumbeat":
            drum1 = drum("K, H, S, H, r:2, K, H, S, H, r:2")
            play(drum1, instrument=1)

        if event.button.id.startswith("drums-"):
            beat = event.button.id.replace("drums-", "")
            beat = drum(beat)
            play(beat, instrument=1)

        if event.button.id == "wholesong":
            chorus = (
                C("F", 2, 1 / 4, 1 / 8) * 2
                | C("F", 3, 1 / 4)
                | C("C", 2, 1 / 4, 1 / 8) * 2
                | C("C", 2, 1 / 4)
                | C("Dm", 2, 1 / 4, 1 / 8) * 2
                | C("Dm", 2, 1 / 4)
                | C("C", 2, 1 / 4, 1 / 8) * 2
                | C("C", 2, 1 / 4)
                | C("Bb", 2, 1 / 4, 1 / 8) * 2
                | C("Bb", 2, 1 / 4)
                | C("C", 2, 1 / 4, 1 / 8) * 2
                | C("C", 2, 1 / 4)
            ) * 2

            chorus = (
                chorus | 
                C("F", 2, 1 / 4, 1 / 8) * 2
                | C("F", 3, 1 / 4)
            )


            drum1 = drum("K, H, S, H, r:2, K, H, S, H, r:2").notes * 8
            drum1.set_volume(112)

            result = piece(
                [chorus, drum1] ,
                [25, 1],
                bpm=90,
                start_times=[0, 0],
                channels=[0, 9],
            )
            play(result)


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Grid(
            Button("F", id="chord-F", variant="success"),
            Button("C", id="chord-C", variant="success"),
            Button("Dm", id="chord-Dm", variant="success"),
            Button("Bb", id="chord-Bb", variant="success"),
            Button("Am", id="chord-Am", variant="success"),
            Button("Kick", id="drums-K", variant="success"),
            Button("Hi-hat", id="drums-H", variant="success"),
            Button("Snare", id="drums-S", variant="success"),
            Button("Open Hi-hat", id="drums-OH", variant="success"),
            Button("Pedal Hi-hat", id="drums-PH", variant="success"),
            Button("Drums", id="drumbeat", variant="success"),
            Button("Play", id="wholesong", variant="success")
        )
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = MusicPad()
    app.run()

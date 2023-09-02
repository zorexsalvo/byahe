from musicpy import C, play

# Plays a guitar rhythm using the musicpy library.

# The rhythm consists of the following chords:
# C, C, G, G, Am, Am, Em, Em, F, F, Em, Em, F, F, G, G

# The function uses the `play` function from the musicpy library to play the rhythm.
# The `bpm` parameter is set to 90 and the `instrument` parameter is set to 25.

# chord = C("C").play()

guitar = (
    C("C", 3, 1 / 4, 1 / 8) * 2 # chord name, octave, duration, delay
    | C("C", 3, 1 / 4)
    | C("G", 2, 1 / 4, 1 / 8) * 2
    | C("G", 2, 1 / 4)
    | C("Am", 2, 1 / 4, 1 / 8) * 2
    | C("Am", 2, 1 / 4)
    | C("Em", 2, 1 / 4, 1 / 8) * 2
    | C("Em", 2, 1 / 4)
    | C("F", 2, 1 / 4, 1 / 8) * 2
    | C("F", 2, 1 / 4)
    | C("Em", 2, 1 / 4, 1 / 8) * 2
    | C("Em", 2, 1 / 4)
    | C("F", 2, 1 / 4, 1 / 8) * 2
    | C("F", 2, 1 / 4)
    | C("G", 2, 1 / 4, 1 / 8) * 2
    | C("G", 2, 1 / 4)
) * 1

play(guitar, bpm=100, instrument=25)

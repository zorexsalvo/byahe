from musicpy import C, play, piece, chord

intro = (
    C("C", 3, 1 / 4, 1 / 8) * 2
    | C("C", 3, 1 / 4)
    | C("Em", 2, 1 / 4, 1 / 8) * 2
    | C("Em", 2, 1 / 4)
    | C("Am", 2, 1 / 4, 1 / 8) * 2
    | C("Am", 2, 1 / 4)
    | C("G", 2, 1 / 4, 1 / 8) * 2
    | C("G", 2, 1 / 4)
    | C("C", 3, 1 / 4, 1 / 8) * 2
    | C("C", 3, 1 / 4)
    | C("C", 3, 1 / 4, 1 / 8) * 2
    | C("C", 3, 1 / 4)
)
verse = (
    C("C", 3, 1 / 4, 1 / 8) * 2
    | C("C", 3, 1 / 4)
    | C("G", 2, 1 / 4, 1 / 8) * 1
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
)

string1 = chord(
    "A5[.6;.],G5[.1;.],A5[.8;.],D5[.8;.],C5[1.1;.],\
    B4[.2;.], A4[.2;.],G4[1;.]"
)

result = piece(
    [intro | verse * 1, string1],
    [2, 34, 49, 31, 1],
    bpm=105,
    start_times=[0, 0],
    channels=[0, 1],
)
play(result)

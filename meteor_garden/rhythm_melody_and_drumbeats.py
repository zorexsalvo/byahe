from musicpy import C, play, piece, chord, drum

verse = (
    C("C", 3, 1 / 4, 1 / 8) * 2
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
)

result = piece(
    [verse] ,
    [2, 34, 49, 31, 1],
    bpm=105,
    start_times=[0, 0],
    channels=[0, 1],
)
play(result)

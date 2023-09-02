from musicpy import C, play, piece, chord

string1 = chord(
    "A5[.6;.],G5[.1;.],A5[.8;.],D5[.8;.],C5[1.1;.],\
    B4[.2;.], A4[.2;.],G4[1;.]"
)

result = piece(
    [string1],
    [2, 34, 49, 31, 1],
    bpm=180,
    start_times=[0, 0],
    channels=[0, 1],
)
play(result)

from musicpy import play, chord

string1 = chord(
    "A5[.6;.],G5[.1;.],A5[.8;.],D5[.8;.],C5[1.1;.],\
    B4[.2;.], A4[.2;.],G4[1;.]"
)

play(string1, bpm=180, instrument=41)
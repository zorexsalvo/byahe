from musicpy import C, chord, drum, play, piece

guitar = (
    (C("Cmaj7") @ 1) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | (C("Fmaj7", 3) ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | (C("G7sus", 3) ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | C("Am11", 3) @ [1, 2, 4, 6, 1, 4, 6, 4]
    | (C("Cmaj7") @ 1) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | C("Fadd9", 3).up(2, 1) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | (C("G7sus", 3) ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | C("Am11", 3) @ [1, 2, 4, 6, 1, 4, 6, 4]
) % (1 / 2, 1 / 8)
guitar2 = (
    C("Am11", 3) @ [1, 2, 4, 6, 1, 4, 6, 4]
    | (C("Em7", 3) ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | (C("Fmaj9", 3) ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | (C("Cmaj9") ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | C("Am11", 3) @ [1, 2, 4, 6, 1, 4, 6, 4]
    | (C("Em7", 3) ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | (C("Fmaj9", 3) ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
    | (C("Cmaj9") ^ 2) @ [1, 2, 3, 4, 1, 2, 3, 2]
) % (1 / 2, 1 / 8)
bass1 = chord(
    "D2[.8;.],E2[.8;.],D2[.8;.],E2[1;.], F2[1;.], G2[1;.], A1[.2;.], A2[.8;.], G2[.8;.], E2[.8;.], D2[.8;.]"
)
bass2 = (
    (
        chord("E2") * 8
        + chord("F1") * 8
        + chord("G1") * 8
        + chord("A1,A1,E2,A1,A2,A1,G2,D2")
    )
    % (1 / 8, 1 / 8)
    * 2
)
bass3 = (
    (
        chord("A2") * 8
        + chord("E2") * 8
        + chord("F2") * 8
        + chord("C2,C2,G2,C2,C3,C2,G2,C2")
    )
    % (1 / 8, 1 / 8)
    * 2
)
bass = bass1 | bass2 | bass3
rhythm_guitar = (
    C("A5(+octave)", 2, 1)
    | C("E5(+octave)", 2, 1)
    | C("F5(+octave)", 2, 1)
    | C("C5(+octave)", 3, 1 / 2)
    | C("G5(+octave)", 2, 1 / 2)
) * 2
string1 = chord(
    "B5[1;.],C6[1;.],D6[.2;.],E6[.2;.],\
F6[.2;.],E6[.2;.],C6[1;.],B5[.2;.],C6[.2;.],G5[1;.],\
F5[.2;.],E5[.2;.],C5[1;.],D5[.4;.],E5[.4;.],F5[.4;.],\
E5[.4;.],D5[.2;.],G5[.2;.],E5[1;.]"
)
drum1 = drum("K, H, S, H, r:2, K, H, OH;S, H, K, H, S, H").notes
drum1.set_volume(112)
result = piece(
    [guitar * 2 | guitar2, bass, string1, rhythm_guitar, drum1 * 4 + 2],
    [2, 34, 49, 31, 1],
    bpm=165,
    start_times=[0, 4 - 3 / 8, 12, 16, 16],
    channels=[0, 1, 2, 3, 9],
)
play(result - 2)

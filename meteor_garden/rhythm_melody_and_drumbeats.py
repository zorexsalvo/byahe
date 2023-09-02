from musicpy import C, play, piece, chord, drum


# K = Kick
# H = Hi-hat
# S = Snare
# OH = Open Hi-hat
# PH = Pedal Hi-hat
# t = Triplet
# r = Rest
# drum('K, H, H, K, S, H, H, H, t:1').play()

chorus = (
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
) * 2

drum1 = drum("K, H, S, H, r:2, K, H, S, H, r:2").notes * 4
drum1.set_volume(112)

result = piece(
    [chorus, drum1] ,
    [25, 1],
    bpm=105,
    start_times=[0, 0],
    channels=[0, 9],
)
play(result)

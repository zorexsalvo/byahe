from musicpy import translate, P, drum, play

bass11 = translate('B1[l:.8; i:.; r:8], D2[l:.8; i:.; r:8], A1[l:.8; i:.; r:8], G1[l:.8; i:.; r:8]')
bass12 = translate('G1[l:.8; i:.; r:6], A1[l:.8; i:.; r:2]')
bass1 = bass11 * 2 | bass12

guitar11 = translate('B3[l:.4; i:.], D4[l:.8; i:.], E4[l:3/8; i:.], D4[l:.8; i:.], E4[l:.8; i:.]')
guitar12 = guitar11.down(2, 0)
guitar13 = guitar12.down(1, [1, 3])
guitar14 = translate('G3[l:.4; i:.], B3[l:.8; i:.], A4[l:5/8; i:.]')
guitar1 = (guitar11|guitar12|guitar13|guitar14) * 2

drum11 = drum('C;K, H, S, H | K, H, S, H, r:5, C;K, H;S[r:2], PH, OH, S;OH[r:3]').notes
drum12 = drum('C;K;H;S, H;S[r:2], PH, OH, S;OH[r:3]').notes
drum1 = drum11 * 2 | drum12

synth11 = translate('D5[l:.8; i:.], B5[l:.8; i:.], r:16')
synth1 = synth11

result = P([bass1, guitar1, drum1, synth1],
           [34, 31, 1, 91],
           bpm=165,
           channels=[0,1,9,2],
           start_times=[0,0,0,4])

play(result)
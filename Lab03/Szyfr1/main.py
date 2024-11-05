def swap_letters(s, index1, index2):
    s_list = list(s)

    s_list[index1], s_list[index2] = s_list[index2], s_list[index1]

    return ''.join(s_list)

text = """EICEXERSF#POROR#GUC#MEIHARL#DOPRCERN#YOTIYHGRAP##S#LIHEAVYABMNOSED##TAAITHEMAC#LAYRTHEO#DNEUP#COMT#R#CNSCIEERPCECACTI#YRHARPTOGPCITRO#ALGIMHE#ES#ARDISOA#GNEDRNUTPMD#COUTAA#LIONAHDRSA#NESSSMUMSNPTIO#KAHUSING#CA#MTILGORH#S#T#HARDORBANIEAK##TCCRPUAL#AITN#YCE#BA#YRSRADVEA#YT#EWHILII#EOES#THRITO#YCALLPSS#T#IBLEORBONIEAK#TA#E#L#WELDISSS#GNEDYET#I#M#ITSNIEBIFEASLI#LUTN#ACAP##CIRACTEOTSOS#DO##CUEEHH#SCM#S#LEIF#WLEDADESIGN#EROER#THEFER#EM#TERDOCOTAMPUTIANUESLLY#CERTRO#THEECINVDAL#AAECA#DS#ANFTSUMOER#CPITNCENG#THLOUEROGY#QRI#SEE#THEEDO#SSIGNTB#NTNE#COIAUVERLLY#ELAN#DUATEA#DSCEIF#NEASTADRY#APDEARO#INFMITREHON#TOTESYLICAL#CEECSURE#HEMPTAS#TH#ORA#YVABLCNNR#EOT#BBKO#EVEN#ENIWMLNTH#UITIUMOED#CPITRWONG#PES#TSAUCH##EHMT##ONEI#E#RAPAD#EUM#ROCH#MEID#LUFFICTOT#I##USENRPTECACTI#AHE#EN#THBTSTRO#THEECIEB#ALLYRKATB#ABLEUC#IATOMPUTNOCS#ALLYERUEEHE#SCM#S"""

x = 20

podciągi = [text[i:i+x] for i in range(0, len(text), x)]

answer = ""

for str in podciągi:
    str = swap_letters(str, 1, 4)
    str = swap_letters(str, 2, 3)
    str = swap_letters(str, 3, 6)
    str = swap_letters(str, 4, 6)
    str = swap_letters(str, 6, 7)
    str = swap_letters(str, 5, 7)
    str = swap_letters(str, 8, 9)
    str = swap_letters(str, 10, 13)
    str = swap_letters(str, 11, 14)
    str = swap_letters(str, 12, 15)
    str = swap_letters(str, 13, 16)
    str = swap_letters(str, 14, 15)
    str = swap_letters(str, 16, 17)
    str = swap_letters(str, 18, 19)
    str = swap_letters(str, 0, 7)
    str = swap_letters(str, 0, 2)

    answer += str

answer = answer.replace("#", ' ')
print(answer)



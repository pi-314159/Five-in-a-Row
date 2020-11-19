from Supplements.Rearrange import rearrange

# The base score of the stone at each point.
def scoreIndexList(List):
    indexList = [0] * len(List)
    i_test = 0
    for i in range(0, len(List)):
        if List[i] != 0 and i >= i_test:
            twoIndex = 0
            zeroIndex = 0
            negIndex = 0
            i_test = i
            stop = "no"
            while i_test < len(List) and stop == "no":
                if List[i_test] == List[i]:
                    twoIndex += 1
                elif i_test + 1 < len(List):
                    if List[i_test + 1] == List[i] and List[i_test] == 0:
                        zeroIndex += 1
                    else:
                        stop = "yes"
                else:
                    stop = "yes"
                i_test += 1
            if stop == "yes":
                i_test -= 1
            if i <= 0 or List[i - 1] != 0:
                negIndex += 1
            if i_test >= len(List) or List[i_test] != 0:
                negIndex += 1
            if negIndex == 2:
                negIndexJ = 2.5
            else:
                negIndexJ = negIndex
            scoreIndex = float(abs(5 ** (twoIndex - negIndexJ) + 1.4 * negIndex - 0.9 * zeroIndex))
            if zeroIndex == 0 and twoIndex > 4:
                scoreIndex = scoreIndex + 5 ** twoIndex + 100
            for indexListi in range(i, i_test):
                indexList[indexListi] = int(scoreIndex * 10)
    scoreList = list(map(lambda l, L: l * L, List, indexList))
    return scoreList

# Add new scores to the original score list.
def AddScore(sB, SB):
    for sb in range(0, len(SB)):
        for sbi in range(0, len(SB[sb])):
            if sB[sb][sbi] != 0:
                sB[sb][sbi] = sB[sb][sbi] + 3 * SB[sb][sbi]
            else:
                sB[sb][sbi] = SB[sb][sbi]
    return sB
   
# Create the score board.
def scoreBoard(Row, Col, Dia, Ada):
    # Anti-rearrange class.
    size = len(Row)
    sB = []
    for row in Row: # Reversed Row.
        sB.append(scoreIndexList(row))
    COL = [] # Reversed Column.
    SB = []
    for col in range(0, size):
        COL.append(scoreIndexList(Col[col]))
    for COLi in range(0, len(COL)):
        SB.append([item[COLi] for item in COL])
    AddScore(sB, SB)
    DIA = [] # Reversed Diagonal.
    SB = []
    SBss = [0] * size
    for dia in Dia:
        DIA.append(scoreIndexList(dia))
    for sizei in range(size):
        SBss[sizei] = DIA[sizei][sizei]
    SB.append(SBss)
    for diai in range(1, size):
        starti = 0
        diaii = diai
        SBs = [0] * size
        while starti != size - diaii:
            SBs[starti] = DIA[diai][starti]
            starti += 1
            diai += 1
        diaiii = size - diaii
        temp_size = size
        while diaiii != size:
            SBs[diaiii] = DIA[temp_size][size - 1 - diaii]
            diaiii += 1
            temp_size += 1
        SB.append(SBs)
    AddScore(sB, SB)
    ADA = [] # Reversed Anti-Diagonal.
    SB = []
    sbs = [1] * size
    for ada in Ada:
        ADA.append(scoreIndexList(ada))
    for ada_i in range(size - 1, 2 * size - 1):
        sbs[ada_i + 1 - size] = ADA[ada_i][0]
    SB.append(sbs)
    for adai in range(size - 2, -1, -1):
        SBs = [0] * size
        ADAi = 0
        ADAi2 = adai
        while adai != size - 1:
            SBs[ADAi] = ADA[adai][ADAi]
            ADAi += 1
            adai += 1
        adai2 = size - 1 - ADAi2
        while adai2 != size:
            SBs[adai2] = ADA[adai2 + ADAi2][size - 1 - ADAi2]
            adai2 += 1
        SB.append(SBs)
    AddScore(sB, SB)
    return sB

# Calculate the score based on the score board.
def score(ogBoard, size, first):
    reArr = rearrange(ogBoard, size)
    sB = scoreBoard(reArr.Row(), reArr.Col(), reArr.Dia(), reArr.Ada())
    del reArr
    score_L = []
    for scoreL in sB:
        for scores in scoreL:
            score_L.append(scores)
    scoreL_noZero = list(filter((0).__ne__, score_L))
    neg_score = sum(negScore for negScore in scoreL_noZero if negScore < 0)
    pos_score = sum(posScore for posScore in scoreL_noZero if posScore > 0)
    if first == 1:
        return pos_score + neg_score
    else:
        return 4 * neg_score + pos_score

import math

# Recursive calls to find the next step.
def nextStep(board, depth, side, size, b_range, first):
    if depth > 2:
        nextBoard = nBoards(board, side, b_range)
        boardScore = []
        for next_board in nextBoard:
            boardScore.append(nextStep(next_board, depth - 1, side * -1, size, b_range, first))
        if side > 0:
            return max(boardScore)
        else:
            return min(boardScore)
    elif depth == 2:
        global scoreStandard
        if side == -1:
            scoreStandard = math.inf
        else:
            scoreStandard = -math.inf
        nextBoard = nBoards(board, side, b_range)
        for next_board in nextBoard:
            nextStep(next_board, depth - 1, side * -1, size, b_range, first)
        return scoreStandard
    else:
        boardScore = []
        nextBoard = nBoards(board, side, b_range)
        for nBi in range(len(nextBoard)):
            sC_t = score(nextBoard[nBi], size, first)
            if side == 1:
                if sC_t >= scoreStandard:
                    break
                else:
                    boardScore.append(sC_t)
            else:
                if sC_t <= scoreStandard:
                    break
                else:
                    boardScore.append(sC_t)
        if len(boardScore) == len(nextBoard):
            if side == 1:
                scoreStandard = max(boardScore)
            else:
                scoreStandard = min(boardScore)

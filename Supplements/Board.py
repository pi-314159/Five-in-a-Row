import math
import copy

# Limit next move.
def board_range(board, size, depth):
    boardRange = [math.inf, -math.inf, math.inf, -math.inf]
    for ri in range(size):
        for ci in range(size):
            if board[ri][ci] != 0:
                if ri < boardRange[0]:
                    boardRange[0] = ri
                if ri > boardRange[1]:
                    boardRange[1] = ri
                if ci < boardRange[2]:
                    boardRange[2] = ci
                if ci > boardRange[3]:
                    boardRange[3] = ci
    if depth < 5:
        b_margin = depth + 1
    else:
        b_margin = 6
    if boardRange[0] - b_margin < 0 or boardRange[2] - b_margin < 0:
        boardRange[0] = 0
        boardRange[2] = 0
    else:
        boardRange[0] = boardRange[0] - b_margin
        boardRange[2] = boardRange[2] - b_margin
    if boardRange[1] + b_margin >= size or boardRange[3] + b_margin >= size:
        boardRange[1] = size
        boardRange[3] = size
    else:
        boardRange[1] = boardRange[1] + b_margin + 1
        boardRange[3] = boardRange[3] + b_margin + 1
    return boardRange

# Create new lists based on the next possible move.
def nBoards(boardStructure, side, rcBS):
    zeroPos = []
    nextBoards = []
    for bSi in range(rcBS[0], rcBS[1]):
        for bsi in range(rcBS[2], rcBS[3]):
            zeropos = []
            if boardStructure[bSi][bsi] == 0:
                zeropos.append(bSi)
                zeropos.append(bsi)
            zeroPos.append(zeropos)
    zeroPos = list(filter(None, zeroPos))
    for pos in zeroPos:
        nextBoard = copy.deepcopy(boardStructure)
        nextBoard[pos[0]][pos[1]] = side
        nextBoards.append(nextBoard)
    return nextBoards    

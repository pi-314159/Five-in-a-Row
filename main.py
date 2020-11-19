# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:56:45 2018

@author: Pi-314159
@instructor: D. Eggli
"""

########## Five in a Row ##########

# https://i.imgur.com/mkFFfzz.jpg
# https://t1.picb.cc/uploads/2018/06/03/2XMXC6.jpg

import copy, math, sys
from multiprocessing import Pool

from Supplements.Score import *
from Supplements.Board import board_range, nBoards
from Supplements.numCPU import cpuNum
import NextStep

# Main function.
CPU_Num = cpuNum(2)

boardSize = int(input("Please enter the side length of the board (must be greater than 4): "))
while boardSize < 5:
    boardSize = int(input("Please enter the side length of the board (must be greater than 4): "))

depth = int(input("Please enter the depth (must be greater than 1): "))
while depth < 2:
    depth = int(input("Please enter the depth (must be greater than 1): "))

goFirst = input('Who will go first? Please enter "A" below if the AI will go first; otherwise, enter "B" below. \n')
while goFirst != "A" and goFirst != "B" and goFirst != "a" and goFirst != "b":
    goFirst = input('Who will go first? Please enter "A" below if the AI will go first; otherwise, enter "B" below. \n')

if goFirst == "A" or goFirst == "a":
    go_first = 1
else:
    go_first = -1

boardStructure = []
zeroBoardS = [0] * boardSize
bsize = 0
while bsize != boardSize:
    boardStructure.append(zeroBoardS[:])
    bsize += 1
del bsize, zeroBoardS, goFirst

if go_first == 1:
    temp_first = math.floor((boardSize - 1) / 2)
    boardStructure[temp_first][temp_first] = 1
    print("\nAI chooses to place its stone in row:", str(temp_first + 1), "and column:", str(temp_first + 1))
    del temp_first

otherStep = str(input("Please tell me where did the other person go (row,col; e.g., 5,3; or $$$$$ to exit)? "))

while otherStep != "$$$$$":
    ns_cood = otherStep.split(",")
    boardStructure[int(ns_cood[0]) - 1][int(ns_cood[1]) - 1] = -1
    bRange = board_range(boardStructure, boardSize, depth)
    if bRange[1] - bRange[0] == bRange[3] - bRange[2] and bRange[3] - bRange[2] == boardSize:
        board_structure = copy.deepcopy(boardStructure)
    else:
        board_structure = []
        for b_si in range(bRange[0], bRange[1]):
            b_sub_structure = []
            for b_sii in range(bRange[2], bRange[3]):
                b_sub_structure.append(boardStructure[b_si][b_sii])
            board_structure.append(b_sub_structure)
            
    zeroCoord = []
    for board in board_structure:
        start = board.count(0)
        zeroCoord.append(start)
    del start 
    
    if depth > sum(zeroCoord):
        depth = sum(zeroCoord)
        if depth == 0:
            sys.exit("There is no possible next move!")
        elif depth == 1:
            nextRow = zeroCoord.index(1)
            nextCol = board_structure[nextRow].index(0)
            sys.exit("AI chooses to place its stone in row: " + str(nextRow + 1) + " and column: " + str(nextCol + 1))    
    
    nextBoards = nBoards(boardStructure, 1, bRange)
    nextMvScoreList = []
    if depth > 2:
        nBPool = Pool(processes = CPU_Num)
        nBPool_result = []
        for nextBoard in nextBoards:
            nBPool_result.append(nBPool.apply_async(nextStep, args=(nextBoard, depth - 1, -1, boardSize, bRange, go_first)))
        nBPool.close()
        nBPool.join()
        for nBPool_r in nBPool_result:
            nextMvScoreList.append(nBPool_r.get())
    else:
        for nextBoard in nextBoards:
            tempnNextMvScoreList = []
            next_Boards = nBoards(nextBoard, -1, bRange)
            for next_Board in next_Boards:
                tempnNextMvScoreList.append(score(next_Board, boardSize, go_first))
            nextMvScoreList.append(min(tempnNextMvScoreList))
    nextMvScore = max(nextMvScoreList)
    nextMv = nextMvScoreList.index(nextMvScore) + 1

    start = 0
    for zCi in range(len(zeroCoord)):
        start += zeroCoord[zCi]
        if start >= nextMv:
            if zCi != 0:
                nextRow = zCi + 1
                nextCol = nextMv + zeroCoord[zCi] - start
            else:
                nextRow = 1
                nextCol = nextMv
            break
    nextRow = nextRow + bRange[0] - 1
    nextCol = nextCol + bRange[2] - 1
    nextCol = [nextCol_i for nextCol_i, zero_place in enumerate(boardStructure[nextRow]) if zero_place == 0][nextCol]
    boardStructure[nextRow][nextCol] = 1
    nextRow += 1
    nextCol += 1
    print("AI chooses to place its stone in row: " + str(nextRow) + " and column: " + str(nextCol))
    
    otherStep = str(input("Please tell me where did the other person go (row,col; e.g., 5,3; or $$$$$ to exit)? "))

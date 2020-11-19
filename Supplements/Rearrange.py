class rearrange:
    # Could be simplified by using matrix.
    # You are not expected to understand this.
    def __init__(self, og_board, board_size):
        self.ogBoard = og_board
        self.boardSize = board_size
    # Row Analysis.
    def Row(self):
        return self.ogBoard
    # Column Analysis.
    def Col(self):
        Col = []
        for wi in range(0, self.boardSize):
            col = []
            for si in range(0, self.boardSize):
                col.append(self.ogBoard[si][wi])
            Col.append(col)
        return Col
    # Diagonal Analysis.
    def Dia(self):
        Dia = []
        for wi in range(0, self.boardSize - 1):
            dia = []
            si = 0
            while wi != -1:
                dia.append(self.ogBoard[wi][si])
                si += 1
                wi -= 1
            Dia.append(dia)
        for wi in range(0, self.boardSize):
            dia = []
            si = self.boardSize - 1
            while wi != self.boardSize:
                dia.append(self.ogBoard[si][wi])
                si -= 1
                wi += 1
            Dia.append(dia)
        return Dia

    # Anti-Diagonal Analysis.
    def Ada(self):
        Ada = []
        for si in range(0, self.boardSize):
            ada = []
            wi = 0
            while si != self.boardSize:
                ada.append(self.ogBoard[si][wi])
                si += 1
                wi += 1
            Ada.append(ada)
        Ada = Ada[::-1]
        for wi in range(1, self.boardSize):
            ada = []
            si = 0
            while wi != self.boardSize:
                ada.append(self.ogBoard[si][wi])
                si += 1
                wi += 1
            Ada.append(ada)
        return Ada
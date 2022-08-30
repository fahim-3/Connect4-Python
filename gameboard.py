class GameBoard:
    def __init__(self, width, height, FirstPlayerSymbol, SecondPlayerSymbol):
        self.__space = ' '  # Space will be empty
        self.row = width       # Width of the board
        self.col = height       # Height of the board
        self.FirstPlayerSymbol = FirstPlayerSymbol      # First player symbol as specified in main
        self.SecondPlayerSymbol = SecondPlayerSymbol    # Second player symbol as specified in main
        self.__board = []

        for i in range(self.row):
            row = [' '] * self.col
            self.__board.append(row)

    def getRows(self):
        return self.row

    def getColumns(self):
        return self.col

    def make_move(self, row, col, element):
        self.__board[row][col] = element

    def check_winner(self):  # Looking for winner with the below conditions

        # This function returns True if  any of the player has won with accordance to the their symbol.
        winner = (self.check_hz() or self.check_vt() or self.check_diag() or self.check_diag1())
        return winner

    def check_diag(self):  # Check for winner diagonally top right to bottom left /
        for x in range(self.row - 3):
            for y in range(3, self.col):
                if (self.__board[x][y] == self.FirstPlayerSymbol and self.__board[x+1][y-1] == self.FirstPlayerSymbol and self.__board[x+2][y-2] == self.FirstPlayerSymbol and self.__board[x+3][y-3] == self.FirstPlayerSymbol) or (self.__board[x][y] == self.SecondPlayerSymbol and self.__board[x+1][y-1] == self.SecondPlayerSymbol and self.__board[x+2][y-2] == self.SecondPlayerSymbol and self.__board[x+3][y-3] == self.SecondPlayerSymbol):
                    # Check if the first or second player symbol is connect diagonally top right to bottom left /
                    return True

        return False

    def check_diag1(self):  # Check for winner diagonally top left to bottom right \
        for x in range(self.row - 3):
            for y in range(self.col - 3):
                if (self.__board[x][y] == self.FirstPlayerSymbol and self.__board[x+1][y+1] == self.FirstPlayerSymbol and self.__board[x+2][y+2] == self.FirstPlayerSymbol and self.__board[x+3][y+3] == self.FirstPlayerSymbol) or (self.__board[x][y] == self.SecondPlayerSymbol and self.__board[x+1][y+1] == self.SecondPlayerSymbol and self.__board[x+2][y+2] == self.SecondPlayerSymbol and self.__board[x+3][y+3] == self.SecondPlayerSymbol):
                    # Check if the first or second player symbol is connect diagonally top left to bottom right \
                    return True

        return False

    def check_hz(self):  # Checking for winner horizontally -
        row = ''
        for x in range(self.row):
            for y in range(self.col):
                row += self.__board[x][y]
            if (self.FirstPlayerSymbol * 4 in row) or (self.SecondPlayerSymbol * 4 in row):
                # Check if the first or second player symbol is connect horizontally
                return True

            row = ''
        return False  # return false if no winner was found

    def check_vt(self):  # Checking for winner vertically |
        col = ''
        for y in range(self.col):
            for x in range(self.row):
                col += self.__board[x][y]
            if (self.FirstPlayerSymbol * 4 in col) or (self.SecondPlayerSymbol * 4 in col):
                # Check if the first or second player symbol is connect vertically
                return True

            col = ''
        return False  # return false if no winner found

    # NOT WORKING
    def is_board_full(self):
        for x in range(self.row):
            for y in range(self.col):
                if self[x][y] == ' ':
                    return False
        return True

    def is_space_free(self, row, col):
        #  Check if space is free before player inserts their dice inside the grid.
        if self.__board[row][col] == ' ':
            return True
        return False

    def show_board_dynamic(self):
        # Number each of the column starting from 0 up to the number fo columns on the board
        for j in range(self.col):
            print(end=" ")
            print(j, end="")
        print()

        # Draw the board using symbols
        for i in range(self.row):
            for j in range(self.col):
                print("|", end="")
                print(self.__board[i][j], end=""),
            print("|")

        # To make it look nice, print stars at the button of the board
        for j in range(self.col):
            print(end="**")
        print(end="*")  # Print one star at the end of the previous as is lacks by one at the end
        print()

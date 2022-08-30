import random
import time


class Player:
    def __init__(self, letter, board):
        self.symbol = letter
        self.gboard = board  # Store a reference to the board

    def get_player_symbol(self):
        return self.symbol


class HumanPlayer(Player):
    def __init__(self, letter, board):
        Player.__init__(self, letter, board)

    def play(self):
        free = False
        row = 0
        while (free == False): # While loop to set conditions and until its correct it will not stop asking
            Col = input("Player %s turn, Please enter the column No : " % self.get_player_symbol())
            # Take input of Human Player with their symbol
            check = True
            while check == True:
                try:
                    if not ((Col.isdigit()) and (int(Col) < self.gboard.getColumns())):
                        # Only accepts digit and must be according to the number of columns
                        Col = input("Player %s, please enter column number according to the number of columns: " % self.get_player_symbol())
                        # If both conditions not met ask again until its correct and take input of Human Player with their symbol
                    else:
                        check = False
                except ValueError:
                    Col = input(Col)  # Take the user input for Col
            Col = int(Col)  # Take input as as integer

            for i in range(self.gboard.getRows() - 1, -1, -1):
                # Drop symbol at the bottom of the board where space is free, if occupied drop it on top of it
                row = i
                free = self.gboard.is_space_free(row, Col)
                if free == True:
                    break
        self.gboard.make_move(row, Col, self.get_player_symbol())


class ComputerPlayer(Player):
    def __init__(self, letter, board):
        Player.__init__(self, letter, board)

    def play(self):

        free = False
        row = 0
        while (free == False):
            print("Computer player %s is thinking..." % self.get_player_symbol())
            # Show a message with the player symbol
            time.sleep(2)  # Gives an illusion that computer player is thinking
            Col = random.randint(0, self.gboard.getColumns()-1)
            # Drop symbol on a column from 0 up to the number of columns on the board
            for i in range(self.gboard.getRows() - 1, -1, -1):
                # Drop symbol at the bottom of the board where space is free, if occupied drop it on top of it
                row = i
                free = self.gboard.is_space_free(row, Col)
                if free == True:
                    break
        self.gboard.make_move(row, Col, self.get_player_symbol())

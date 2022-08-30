from gameboard import GameBoard
from player import HumanPlayer
from player import ComputerPlayer


def main():
    # Message with hints to what the game features are
    print()  # Empty line so everything doesn't get cramped
    print("WELCOME TO CONNECT FOUR")  # Welcoming the player to the game at start
    print()  # Empty line so everything doesn't get cramped
    print("You can choose different grid size combinations.")
    # Make the user aware that they are able to chose grid size
    print("As well as different Game Modes:")
    # Let the user know about each of the game mode before-hand
    print("     *Human Player vs Human Player.")  # Letting the user know of this specific game mode
    print("     *Human Player vs Computer Player.")  # Letting the user know of this specific game mode
    print("     *Computer Player vs Computer Player.")  # Letting the user know of this specific game mode
    print()  # Empty line so everything doesn't get cramped

    # Gives a sense of a starting point of the game
    BeginGame = input("press ENTER to begin!: ")  # Take keypress ENTER
    check = True
    while check == False:
        try:
            print(BeginGame)
        except SyntaxError:
            pass

    # Allow the user to pick a symbol from the keyboard
    FirstPlayerSymbol = str(input("Please enter Symbol for First Player: "))  # Take player chosen string symbol
    check = True
    while check == True:  # While loop to set conditions and until its correct it will not stop
        try:
            if not (FirstPlayerSymbol.isalpha() and (len(FirstPlayerSymbol) <=1)):
                # Take only one alphabetical character
                print("Invalid character! ") # This message will be shown if all of the above conditions are not met
                FirstPlayerSymbol = str(input("Please enter one alphabetical character for First Player: "))
                # Ask player again and again until all of the above conditions are met
            else:
                check = False
        except ValueError:
            FirstPlayerSymbol = str(input(FirstPlayerSymbol))  # Take player chosen string symbol

    # Allow the user to pick a symbol from the keyboard
    SecondPlayerSymbol = str(input("Please enter Symbol for Second Player : "))  # Take player chosen string symbol
    check = True
    while check == True:  # While loop to set conditions and until its correct it will not stop
        try:
            if not ((SecondPlayerSymbol.isalpha()) and ((SecondPlayerSymbol) != FirstPlayerSymbol) and (len(SecondPlayerSymbol)<=1)):
                # Only one alphabetical character, and different symbol from the First Player
                print("Invalid character! ") # This message will be shown if all of the above conditions are not met
                SecondPlayerSymbol = str(input("Enter one alphabetical character and must be different from first player: "))
                # Ask player again and again until all of the above conditions are met
            else:
                check = False
        except ValueError:
            SecondPlayerSymbol = str(input(SecondPlayerSymbol)) # Take player chosen string symbol


    Rows = input("Please enter number of Rows: ") #  Take player chosen row number
    check = True
    while check == True:  # While loop to set conditions and until its correct it will not stop
        try:
            if not ((Rows.isdigit()) and (int(Rows)>=6 and int(Rows)<=50)):
                # Must be a digit and greater than or equal 6 as well as less than or equal 50
                print("Invalid number! ")  # This message will be shown if all of the above conditions are not met
                Rows = input("Please enter number between 6 and 50 for the Rows: ")
                # Ask player again and again until all of the above conditions are met
            else:
                check = False
        except ValueError:
            Rows = input(Rows)  # Take the input value for Rows
    Rows = int(Rows)  # Take row number as integer

    Columns = input("Please enter number of Columns: ")  # Take player chosen row number
    check = True
    while check == True:  # While loop to set conditions and until its correct it will not stop
        try:
            if not ((Columns.isdigit()) and (int(Columns)>=7 and int(Columns)<=50)):
                # Must be a digit and greater than or equal 7 as well as less than or equal 50
                print("Invalid number! ")  # This message will be shown if all of the above conditions are not met
                Columns = input("Please enter number between 7 and 50 for the Columns: ")
                # Ask player again and again until all of the above conditions are met
            else:
                check = False
        except ValueError:
            Columns = input(Columns)  # Take the input value for Columns
    Columns = int(Columns)  # Take column number as integer

    gboard = GameBoard(Rows, Columns, FirstPlayerSymbol, SecondPlayerSymbol)

    GameMode = str(input("Enter HH, HC or CC:\n"
                         "* HH = Human Player vs Human Player\n"
                         "* HC = Human Player vs Computer Player\n"
                         "* CC = Computer Player vs Computer Player: ").upper())
    # Take user input and as upper case for the game mode
    check = True
    while check == True: # While loop to set conditions and until its correct it will not stop
        try:
            if not ((GameMode == "HH") or (GameMode == "HC") or (GameMode == "CC")):
                # Only take user input HH, HC or CC
                print("Invalid character! ") # This message will be shown if all of the above conditions are not met
                GameMode = str(input("Please enter HH, HC or CC for your desired Game Mode: ").upper())
                # Ask player again and again until all of the above conditions are met
            else:
                check = False
        except ValueError:
            GameMode = str(input(GameMode)) # Take player chosen mode input as string

    # If statements to set different game modes and allow user to pick one
    if GameMode == "HH":  # Setting up a game mode with a specific string character which in this case is 'HH'
        hp0 = HumanPlayer(FirstPlayerSymbol, gboard)  # Set symbol for each player
        hp1 = HumanPlayer(SecondPlayerSymbol, gboard)  # Set symbol for each player
        GameMode = (hp0, hp1)  # Created a tuple in which the players will take turns
    elif GameMode == "HC":  # Setting up a game mode with a specific string character which in this case is 'HC'
        hp0 = HumanPlayer(FirstPlayerSymbol, gboard)  # Set symbol for each player
        cp0 = ComputerPlayer(SecondPlayerSymbol, gboard)  # Set symbol for each player
        GameMode = (hp0, cp0)  # Created a tuple in which the players will take turns
    elif GameMode == "CC":  # Setting up a game mode with a specific string character which in this case is 'CC'
        cp0 = ComputerPlayer(FirstPlayerSymbol, gboard)  # Set symbol for each player
        cp1 = ComputerPlayer(SecondPlayerSymbol, gboard)  # Set symbol for each player
        GameMode = (cp0, cp1)  # Created a tuple in which the players will take turns

    players_lst = GameMode
    # Place first player and second player in tuple for turn based game in accordance with player chosen game mode.
    winner = False

    gboard.show_board_dynamic()  # Show empty grid at the start of the game

    while (winner == False):

        for p in players_lst:
            p.play()
            gboard.show_board_dynamic()  # Board is shown on the screen after each move
            winner = gboard.check_winner()  # The board will check for winner after each move

            if winner == True:
                print()
                print("Player %s is the Winner!" % p.get_player_symbol())  # Show current player's symbol as Winner
                # Allow user to restart after winner found and game ended
                while True:  # While loop to set conditions and until its correct it will not stop
                    answer = str(input('Do you want to play again? (Y/N): ').upper())
                    # Take user input as upper case string and match with bellow condition
                    if answer in ('Y', 'N'):  # Determine the answer
                        break
                    print('Invalid input.')  # This message will be shown if the above conditions is not met
                if answer == 'Y':  # Checking if user input is upper case 'Y'
                    main()  # If user input is upper case 'Y', the game will go back to main()
                else:
                    print()  # Empty line so everything doesn't get cramped
                    print('Thanks for playing, Goodbye')  # Show this friendly message if user input was 'N'
                    break  # Terminate the game if user input was 'N'
main()

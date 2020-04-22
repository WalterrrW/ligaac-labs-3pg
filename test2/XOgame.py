import random
from collections import OrderedDict


def doYouWantToPlay():
    answer = input("Do you want to play X&O? yes/no --> ")
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("This is not a valid answer please type 'yes' or 'no': ")
        return doYouWantToPlay()


def addPlayer(player):
    return input(f"Name for {player} --> ")


def orderPlayers(player1, player2):
    create_players = OrderedDict()
    if bool(random.getrandbits(1)):  # player 1 starts or not--> true or false
        if bool(random.getrandbits(1)):  # player 1 is with X
            create_players[player1] = "X"
            create_players[player2] = "O"
        else:
            create_players[player1] = "O"
            create_players[player2] = "X"
    else:  # player 2 starts or not--> true or false
        if bool(random.getrandbits(1)):  # player 2 is with X
            create_players[player2] = "X"
            create_players[player1] = "O"
        else:
            create_players[player2] = "O"
            create_players[player1] = "X"
    return create_players


def generateBoard(XOX_board):

    print("\n\n\n\n\n")
    print("________________________________________________________________________________________")

    print('   |   |')
    print(' ' + XOX_board[7] + ' | ' + XOX_board[8] + ' | ' + XOX_board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + XOX_board[4] + ' | ' + XOX_board[5] + ' | ' + XOX_board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + XOX_board[1] + ' | ' + XOX_board[2] + ' | ' + XOX_board[3])
    print('   |   |')


def checkIfAvailable(XOX_board, decision, player):
    if XOX_board[decision] != "X" and XOX_board[decision] != "O":
        return True
    return False


def isFinished(XOX_board, mark):
    if ((XOX_board[1] == mark and XOX_board[2] == mark and XOX_board[3] == mark) or
            (XOX_board[4] == mark and XOX_board[5] == mark and XOX_board[6] == mark) or
            (XOX_board[7] == mark and XOX_board[8] == mark and XOX_board[9] == mark) or
            (XOX_board[1] == mark and XOX_board[4] == mark and XOX_board[7] == mark) or
            (XOX_board[2] == mark and XOX_board[5] == mark and XOX_board[8] == mark) or
            (XOX_board[3] == mark and XOX_board[6] == mark and XOX_board[9] == mark) or
            (XOX_board[1] == mark and XOX_board[5] == mark and XOX_board[9] == mark) or
            (XOX_board[3] == mark and XOX_board[5] == mark and XOX_board[7] == mark)):
        return True
    return False


def isfullboard(XOX_board):
    for elem in XOX_board:
        if elem != "X" and elem != "O":
            return False
    return True


def playerChoice(XOX_board, player):
    print(f"It is your turn {player[0]}: ")
    try:
        decision = input("Choose a number where you want to move! ")
        decision = int(decision)
        if 0 < decision < 10:
            if checkIfAvailable(XOX_board, decision, player):
                XOX_board[decision] = player[1]
                return XOX_board
            else:
                print("This field is already set, choose an empty one!")
                return playerChoice(XOX_board, player)
        else:
            print("This is not a valid box number choose between 1-9!")
            return playerChoice(XOX_board, player)
    except:
        print("This is not an integer, please insert a number between 1-9!")
        return playerChoice(XOX_board, player)


def getNames():
    try:
        player1 = addPlayer("player1")
        player2 = addPlayer("player2")
        # print(f"{len(player1)}     {len(player2)}")
        if player1.isspace() or player2.isspace():
            print("Player name cannot be just spaces!")
            raise Exception()
        if player1.__str__().__eq__(player2.__str__()):
            print("Names cannot be the same, try again!")
            raise Exception()
        if len(player1) < 3 or len(player2) < 3:
            print("Names must be longer than 3 characters!")
            raise Exception()
        return player1, player2
    except:
        print("Error at name, try again!")
        return getNames()


if __name__ == "__main__":
    while True:
        if not doYouWantToPlay():
            break

        XOX_board = [str(elem) for elem in range(10)]
        XOX_board[0] = "O"
        
        player1, player2 = getNames()
        players = orderPlayers(player1, player2)
        print(f"{list(players.items())[0]} VS {list(players.items())[1]}")

        playing = True
        while True:
            for player in players.items():
                generateBoard(XOX_board)
                XOX_board = playerChoice(XOX_board, player)
                if isFinished(XOX_board, player[1]):
                    generateBoard(XOX_board)
                    print(f"{player[0]} has won")
                    playing = False
                    break
                if isfullboard(XOX_board):
                    generateBoard(XOX_board)
                    print(f"It is a tie!")
                    playing = False
                    break
            if not playing:
                break

'''
Assigment: Tic-Tac-Toe
Hector Barillas
'''
spacios = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, turn = 'X', 'O', ' ' # Values

def main():
    print("Tic-Tac-Toe Game")
    print("Good Luck")
    game = getBoard()
    Player1, Player2 = X, O # Indicates who goes first.
    
    while True:
        print(getBoardStr(game)) # Display the board.

        move = None # Ask the player to enter a number between 1-9.
        while not isValidSpace(game, move):
            print('Where {} will set? (1-9)'.format(Player1))
            move = input('> ')
        updateBoard(game, move, Player1) # Make a move.

        if isWinner(game, Player1): # Check if the game is over
            print(getBoardStr(game))      # and if we have a winner.
            print(Player1 + ' Won the game')
            break
        elif isBoardFull(game): # Check if the game is tie.
            print(getBoardStr(game))
            print("It's a tie!")
            break
        Player1, Player2 = Player2, Player1 # Switch turns.
    print("Good Game. Thanks for playing")
#----------------------------------------------------------------------------
def getBoard(): # Create a new board.
    board = {}
    for space in spacios:
        board[space] = turn
    return board
#---------------------------------------------
def getBoardStr(board): # Display a representation of the board.
    return '''
  {}|{}|{} 1 2 3
  -+-+-
  {}|{}|{} 4 5 6
  -+-+-
  {}|{}|{} 7 8 9'''.format(board['1'], board['2'], board['3'],
                               board['4'], board['5'], board['6'],
                               board['7'], board['8'], board['9'])
#-------------------------------------------------------------------
def isValidSpace(board, space):
    """Returns True if the space on the board is a valid space number
    and the space is blank."""
    return space in spacios and board[space] == turn
#------------------------------------------------------------------------
def isWinner(board, player):
    """Return True if player is a winner on this TTTBoard."""

    b, p = board, player
    return ((b['1'] == b['2'] == b['3'] == p) or
           (b['4'] == b['5'] == b['6'] == p) or 
           (b['7'] == b['8'] == b['9'] == p) or 
           (b['1'] == b['4'] == b['7'] == p) or 
           (b['2'] == b['5'] == b['8'] == p) or 
           (b['3'] == b['6'] == b['9'] == p) or 
           (b['3'] == b['5'] == b['7'] == p) or 
           (b['1'] == b['5'] == b['9'] == p)) 
#------------------------------------------------------
def isBoardFull(board):
    """Return True if every space on the board has been taken."""
    for space in spacios:
        if board[space] == turn:
            return False # If a space is blank return False.
    return True # If no blank spaces return True.
#-----------------------------------------------------------------
def updateBoard(board, space, mark):
    """Sets the space on the board to mark."""
    board[space] = mark

if __name__ == '__main__':
    main() 
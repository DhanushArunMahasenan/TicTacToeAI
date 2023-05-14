board = {1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " " }
turn = "X"


def computerMove(board):
    bestScore = -10
    bestMove = 0
    
    for key in board.keys():
        if board[key] == " ":
            board[key] = "X"
            score = miniMax(board, False)
            board[key] = " "
            
            if score > bestScore:
                bestScore = score
                bestMove = key
    
    insertValue(bestMove, "X")

def miniMax(board, maximizing):
    if checkForWin(board, "X"):
        return 1
    
    elif checkForWin(board, "O"):
        return -1
    
    elif checkForDraw(board):
        return 0

    if maximizing:
        bestScore = -10
        
        for key in board.keys():
            if board[key] == " ":
                board[key] = "X"
                score = miniMax(board, False)
                board[key] = " "
                
                if score > bestScore:
                    bestScore = score
        
        return bestScore
    
    else:
        bestScore = 10
        
        for key in board.keys():
            if board[key] == " ":
                board[key] = "O"
                score = miniMax(board, True)
                board[key] = " "
                
                if score < bestScore:
                    bestScore = score
        
        return bestScore
        

def displayBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    
displayBoard(board)

def insertValue(position, value):
    global turn
    
    if board[position] == " ":
        board[position] = value

        if checkForWin(board, value):
            displayBoard(board)
            print(f"{turn} has won the game.")
            quit()
            
        if checkForDraw(board):
            displayBoard(board)
            print("This game is a draw.")
            quit()

        if value == "X":
            turn = "O"
        
        else:
            turn = "X"
    
    else:
        print("Error: position is already occupied.")
        turn = value

def checkForDraw(board):
    for i in board.values():
        if i == " ":
            return False
        
    return True

def checkForWin(board, player):
    #horizontal 1
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    
    #horizontal 2
    if board[4] == board[5] and board[5] == board[6] and board[6]  == player:
        return True

    #horizontal 3
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True
    
    #vertical 1
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    
    #vertical 2
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    
    #vertical 3
    elif board [3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    
    #diagonal 1
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    
    #diagonal 2
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    
    #no win
    else:
        return False
    
    
while True:
    if turn == "X":
        computerMove(board)
        displayBoard(board)
    
    else:
        position = int(input(f"Enter the position to place {turn}: "))
        insertValue(position, turn)
        displayBoard(board)

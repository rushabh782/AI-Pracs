def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 1
            elif board[row][0] == 'O':
                return -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 1
            elif board[0][col] == 'O':
                return -1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 1
        elif board[0][0] == 'O':
            return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O':
            return -1
    return 0

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def minimax(board, depth, isMaximizingPlayer):
    score = evaluate(board)
    if score == 1:
        return score
    if score == -1:
        return score
    if not isMovesLeft(board):
        return 0
    if isMaximizingPlayer:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i][j] = '_'
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i][j] = '_'
        return best

def findBestMove(board):
    bestVal = float('-inf')
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

def printBoard(board):
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(board[i][j], end=" | ")
            else:
                print(board[i][j], end=" ")
        print()

board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

print("Let's play Tic Tac Toe!")
while isMovesLeft(board):
    printBoard(board)
    x = int(input("Enter row (0-2) : "))
    y = int(input("Enter column (0-2) : "))
    if board[x][y] != '_':  
        print("Invalid move! Try again.")
        continue
    board[x][y] = 'O'
    if evaluate(board) == -1:
        printBoard(board)
        print("You win!")
        break
    if not isMovesLeft(board):
        printBoard(board)
        print("It's a draw!")
        break
    print("AI is thinking...")
    i, j = findBestMove(board)
    board[i][j] = 'X'
    if evaluate(board) == 1:
        printBoard(board)
        print("AI wins!")
        break
else:
    printBoard(board)
    print("It's a draw!")

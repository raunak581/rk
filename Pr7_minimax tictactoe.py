# Tic Tac Toe Minimax Algorithm

# Constants for player and AI
PLAYER = 'X'
AI = 'O'
EMPTY = ' '
# Initial state of the board
initial_state = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]
# Function to check for terminal state
def is_terminal_state(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return True
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return True
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    # Check for a draw
    for row in board:
        if EMPTY in row:
            return False
    return True








# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if is_terminal_state(board):
        if is_maximizing:
            return -1  # AI loses
        else:
            return 1   # AI wins
    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval




# AI's move selection
def get_best_move(board):
    best_move = None
    best_eval = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                eval = minimax(board, 0, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Example usage
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

# ... (remaining code)





def main():
    board = initial_state
    while not is_terminal_state(board):
        print_board(board)
        row, col = get_best_move(board)
        board[row][col] = AI
        print("\nAI's Move:")
        print_board(board)
        if is_terminal_state(board):
            break
        player_row = int(input("Enter row (0, 1, or 2): "))
        player_col = int(input("Enter col (0, 1, or 2): "))
        board[player_row][player_col] = PLAYER

    print("Game Over!")
    print_board(board)
    
if __name__ == "__main__":
    main()



    

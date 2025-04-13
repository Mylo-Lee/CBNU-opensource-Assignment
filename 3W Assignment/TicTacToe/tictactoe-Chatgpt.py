#Chat GPT가 제작한 틱택토 알고리즘
# 미니맥스 알고리즘을 사용, alpha-beta pruning을 사용하여 알고리즘을 최적화함.
# Copilot과 차이점은 인터페이스에 행 구분이 생겼고, math가 아닌 random 라이브러리를 import 했다.
# 향상된점은 키패드에 어느정도 매치되는 1~9의 숫자를 입력받아 게임진행
# 하지만 여전히 인터페이스가 엉성하고, 키패드에 반전되어있어서 사용자가 헷갈릴 수 있다.
# 
import random

# 게임판을 출력하는 함수
def print_board(board):
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("-" * 5)

# 게임이 끝났는지 체크하는 함수
def check_winner(board, player):
    # 가로, 세로, 대각선 체크
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# 게임판이 꽉 찼는지 확인하는 함수
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# 가능한 수를 찾는 함수
def get_empty_positions(board):
    positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                positions.append((i, j))
    return positions

# 미니맥스 알고리즘을 구현한 함수
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"):  # AI가 이긴 경우
        return 10 - depth
    elif check_winner(board, "X"):  # 플레이어가 이긴 경우
        return depth - 10
    elif is_full(board):  # 무승부
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for (i, j) in get_empty_positions(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for (i, j) in get_empty_positions(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# AI의 최적 수를 찾는 함수
def best_move(board):
    best_value = float('-inf')
    move = None
    for (i, j) in get_empty_positions(board):
        board[i][j] = "O"
        move_value = minimax(board, 0, False, float('-inf'), float('inf'))
        board[i][j] = " "
        if move_value > best_value:
            best_value = move_value
            move = (i, j)
    return move

# 플레이어의 수를 입력받는 함수
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Invalid move, try again.")
        except (ValueError, IndexError):
            print("Invalid input, try again.")

# 게임 루프
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    while True:
        # 플레이어 차례
        print("\nYour turn!")
        row, col = player_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI 차례
        print("\nAI's turn!")
        row, col = best_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# 게임 시작
if __name__ == "__main__":
    play_game()

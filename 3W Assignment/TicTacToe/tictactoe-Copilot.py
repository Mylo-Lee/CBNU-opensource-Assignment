#copilot이 제작한 Tic-Tac-Toe Algorithm.
#알고리즘은 Minimax Algorithm을 사용하였음.
#하지만 0 이 입력이 되지 않고, 인터페이스도 엉성해 수정이 필요함.
#0-8까지 번호를 입력하라는데, 0-8까지의 번호가 어디에 대응하는지 알기 힘듬

import math

# 틱택토 보드 초기화
board = [" " for _ in range(9)]

# 보드 출력 함수
def print_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("|".join(row))
    print()

# 승리 조건 확인 함수
def check_winner(b, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 가로
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 세로
        [0, 4, 8], [2, 4, 6]             # 대각선
    ]
    return any(all(b[i] == player for i in pattern) for pattern in win_patterns)

# Minimax 알고리즘
def minimax(is_maximizing):
    winner = None
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# 컴퓨터의 최적의 움직임 찾기
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# 게임 플레이
def play_game():
    while True:
        print_board()
        if check_winner(board, "O"):
            print("컴퓨터가 이겼습니다!")
            break
        if check_winner(board, "X"):
            print("플레이어가 이겼습니다!")
            break
        if " " not in board:
            print("무승부입니다!")
            break

        # 플레이어의 턴
        player_move = int(input("0-8까지 번호를 입력하세요: "))
        if board[player_move] == " ":
            board[player_move] = "X"
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        # 컴퓨터의 턴
        if " " in board:
            computer_move = best_move()
            board[computer_move] = "O"

play_game()

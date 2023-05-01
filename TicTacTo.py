import os, time, random, typing

print("\tTic Tac To\t")

win_color = "\033[42m"
clear_color = "\033[0m"
loser_color = "\033[41m"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_winner(board) -> typing.Union[typing.Literal[0, 1, 2, 3], list]:
    res = 0
    win_board = [ [0,0,0], [0,0,0], [0,0,0] ]

    # 가로 체크
    for row in board:
        if row.count(1) == 3:
            res=row[0]
            win_board[board.index(row)] = [1,1,1]

        elif row.count(2) == 3:
            res=row[0]
            win_board[board.index(row)] = [1,1,1]


    # 세로 체크
    for col in range(3):
        if (N := board[0][col]) == board[1][col] == board[2][col]:
            res = N
            a_list = [0, 0, 0]
            a_list[col] = 1
            for i in range(3):
                win_board[i] = a_list
            break


    # 대각선 체크
    diagonal1 = [board[i][i] for i in range(3)] # 좌상단 -> 우하단
    diagonal2 = [board[i][2-i] for i in range(3)] # 우상단 -> 좌하단

    if (diagonal1.count(1) == 3) or (diagonal1.count(2) == 3):
        res = diagonal1[0] 
        win_board = [ [1,0,0], [0,1,0], [0,0,1] ]

    if (diagonal2.count(1) == 3) or (diagonal2.count(2) == 3):
        res = diagonal2[0]
        win_board = [ [0,0,1], [0,1,0], [1,0,0] ]


    # 무승부
    if all(row.count(0) == 0 for row in board) and not res:
        res = 3


    return res, win_board

def print_board(board):
    print('    1  2  3', end='')

    for i in range(3):
        print('\t')
        for j in range(3):
            if j == 0:
                print(i+1, end='  ')
            print(' O' if (d := board[i][j]) == 1 else ' X' if d == 2 else ' N', end=' ')
    
    print("\n\n")

def print_board_for_winner(board, win_board, score):
    print(f"Score: User : {score['user']} | Computer : {score['computer']}")
    print('    1  2  3', end='')
    for i in range(3):
        print('\t')
        for j in range(3):
            if j == 0:
                print(i+1, end='  ')

            if win_board[i][j] == 1: # win board 해당 부분이 1 인 경우
                color = win_color
                color_2 = loser_color
            else:
                color = clear_color
                color_2 = clear_color
            
            if (d := board[i][j]) == 1:
                print(f' {color}O{clear_color}', end=' ')
            elif d == 2:
                print(f' {color_2}X{clear_color}', end=' ')
            else:
                print(f" {color}N{clear_color}", end=' ')
    
    print("\n\n")


def user_input() -> tuple:
    col = int(input("행: "))
    row = int(input("열: "))

    return col, row

check_ture_pos = lambda col, row: False if Board[col][row] != 0 else True
input_computer = lambda x=None: (random.randint(0, 2), random.randint(0, 2))

class Turn:
    User = 0,
    Computer = 1


Score = {
    "user" : 0,
    "computer" : 0
}


# Game
while True:
    clear_console()
    Board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    Winner = None
    TURN = Turn.User

    while True:
        print("GMark: User : O | Computer : X")
        print(f"Score: User : {Score['user']} | Computer : {Score['computer']}")
        print_board(Board)

        if TURN == Turn.User: # User Turn
            print("User Turn")
            while True:
                col, row = user_input()
                if ((col > 3) or (row > 3)) or ((col < 1) or (row < 1)):
                    print('올바른 행 / 열을 입력해 주세요') 
                elif check_ture_pos(col-1, row-1) is False:
                    print("이미 표시된 위치이에요")
                else:
                    break

            Board[col-1][row-1] = 1
            TURN = Turn.Computer

        else: # Computer Turn
            print("Computer Turn")
            col, row = (input_computer())

            while True:
                if check_ture_pos(col, row) is False:
                    col, row = (input_computer())
                else:
                    break

            Board[col][row] = 2

            print(f'행: {col+1}')
            print(f'열: {row+1}')
            time.sleep(2)

            TURN = Turn.User

        clear_console()



        p, win_board = check_winner(board=Board)
        if p: # Check Winner
            print_board_for_winner(Board, win_board, Score)
            if p == 1:
                print(f"\n\t{win_color}승리!{clear_color}\n")
                Score['user'] += 1

            elif p == 2:
                print(f"\n\t{loser_color}패배¡{clear_color}\n")
                Score['computer'] += 1

            elif p == 3:
                print("\n\t¡무승부!\n")

    
            print("\n이어서 플레이 하기 (Y=1/N=0)")
            while True:
                is_continue = int(input("> "))
                if is_continue < 0 or is_continue > 1 :
                    print('(Y=1/N=0) 중에서 입력해 주세요') 
                else:
                    break
            break


    if is_continue == 0:
        print(f"Score: User : {Score['user']} | Computer : {Score['computer']}")
        break
    clear_console()



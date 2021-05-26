import random as rd


def gbb_game(you_n):
    com_n = rd.randint(1, 4)
    if com_n - you_n == -2 or com_n - you_n == 1:
        print('컴퓨터가 이겼습니다')
        print(f'COM:{com_n}')
    elif com_n - you_n == 2 or com_n - you_n == -1:
        print('당신이 이겼습니다')
        print(f'COM:{com_n}')
    elif com_n == you_n:
        print('비겼습니다')
        print(f'COM:{com_n}')
    else:
        pass


def input_num():
    you_n = int(input('YOU 입력 (1:가위,2:바위,3:보) : '))
    gbb_game(you_n)
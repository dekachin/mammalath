import random

board = [[[0 for i in range(2)] for j in range(6)] for k in range(6)]
animal = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
put_add = []
status = 1
cnt_stone = 0

random.shuffle(animal)
num = 0
for i in range(6):
    for j in range(6):
        board[i][j][0] = animal[num]
        num+=1

for i in range(6):
    print(board[i])

def change(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return n

def put_stone(x, y, z):
    board[x][y][1] = z
    return board

def release_three(x, y):
    board[x][y][0] = 0
    return board

def release_animal(n):
    for i in range(6):
        for j in range(6):
            if board[i][j][0] == n:
                board[i][j][0] = 0
    return board

def judge(x, y, z):
    global cnt_stone
    #----------------------------------------------------
    #↑方向の探索
    for i in range(x, max(-1,x-3), -1):
        if board[i][y][1] == z:
            cnt_stone += 1
        else:
            cnt_stone = 0
            break
    if cnt_stone == 3:
        for i in range(x, max(-1,x-3), -1):
            if board[i][y][0] == 0:
                return 3
            else:
                return 4
    cnt_stone = 0
    #-----------------------------------------------------
    #↓方向の探索
    for i in range(x, min(6,x+3), 1):
        if board[i][y][1] == z:
            cnt_stone += 1
        else:
            cnt_stone = 0
            break
    if cnt_stone == 3:
        for i in range(x, min(6,x+3), 1):
            if board[i][y][0] == 0:
                return 3
            else:
                return 4
    cnt_stone = 0
    #-----------------------------------------------------
    #→方向の探索
    for i in range(y, min(6,y+3), 1):
        if board[x][i][1] == z:
            cnt_stone += 1
        else:
            cnt_stone = 0
            break
    if cnt_stone == 3:
        for i in range(y, min(6,y+3), 1):
            if board[x][i][0] == 0:
                return 3
            else:
                return 4
    cnt_stone = 0
    #-----------------------------------------------------
    #←方向の探索
    for i in range(y, max(-1,y-3), -1):
        if board[x][i][1] == z:
            cnt_stone += 1
        else:
            cnt_stone = 0
            break
    if cnt_stone == 3:
        for i in range(y, max(-1,y-3), -1):
            if board[x][i][0] == 0:
                return 3
            else:
                return 4
    cnt_stone = 0
    #-----------------------------------------------------
    #↗方向の探索
    print(status)
    print(type(status))
    return z
    
while status < 3:
    print("")
    print("player" + str(status) + ": select option")
    print("1:put stone, 2:release three animals, 3:release one kind of animals")
    opt = int(input())
    if opt == 1:
        print("put stone")
        put_x, put_y = input().split()
        X = int(put_x)
        Y = int(put_y)
        board = put_stone(X, Y , status)
        status = judge(X, Y, status)

    elif opt == 2:
        print("choice release three point")
        release_x1, release_y1 = input().split()
        release_x2, release_y2 = input().split()
        release_x3, release_y3 = input().split()
        X1 = int(release_x1)
        Y1 = int(release_y1)
        X2 = int(release_x2)
        Y2 = int(release_y2)
        X3 = int(release_x3)
        Y3 = int(release_y3)
        board = release_three(X1, Y1)
        board = release_three(X2, Y2)
        board = release_three(X3, Y3)
        
    elif opt == 3:
        print("select release animal")
        select_animal = int(input())
        board = release_animal(select_animal)
    
    status = change(status)

    for i in range(6):
        print(board[i])

    print(type(status))
    print(status)

print("game end")
import random

board = [[[-1 for i in range(2)] for j in range(10)] for k in range(10)]
animal = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
put_add = []
status = 1
cnt_animal = 0
cnt_stone = 0
flag = True
check_animal = 0
check_stone = 1
num = 1
vector_h = 0
vector_w = 0
mode = 0
turn = 1


random.shuffle(animal)
num = 0
for i in range(2, 8):
    for j in range(2, 8):
        board[i][j][0] = animal[num]
        board[i][j][1] = 0
        num+=1

for i in range(2, 8):
    for j in range(2, 8):
        print(board[i][j], end='')
    print('')

# ---------------------関数------------------------------------
def hoge(n):
    for i in range(6):
        for j in range(6):
            if board[i][j][1] == 1:
                board[i][j][1] = n
    return board

def can_put(h, w):
    if (h <= 1 or h >= 8 or w <= 1 or w >= 8):
        print("馬鹿めそこには置けんぞ")
        return(False)
    elif board[h][w][1] != 0:
        print("おめぇ頭ママラスなんかぁ?")
        return(False)
    else:
        return(True)

def change(n):
    global turn
    turn += 1
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return n

def put_stone(x, y, z):
    board[x][y][1] = z
    return board

def vec(d):
    global vector_h
    global vector_w
    if d == 1:
        vector_h = -1
        vector_w = 0
    if d == 2:
        vector_h = -1
        vector_w = 1
    if d == 3:
        vector_h = 0
        vector_w = 1
    if d == 4:
        vector_h = 1
        vector_w = 1
    if d == 5:
        vector_h = 1
        vector_w = 0
    if d == 6:
        vector_h = 1
        vector_w = -1
    if d == 7:
        vector_h = 0
        vector_w = -1
    if d == 8:
        vector_h = -1
        vector_w = -1
    return vector_h, vector_w

def check_board(h, w, Vh, Vw, A, st):
    global cnt_animal
    global cnt_stone
    global num

    num = 1
    for i in range(3):
        #石判定ならA=0
        if A == 0:
            if board[(h + Vh * i)][w + Vw * i][1] == st:
                cnt_stone += 1
            else:
                cnt_stone = 0
            if cnt_stone != (i + 1):
                #3連続の探索中に1つでも石ナシならFalseを返す
                return False
        #勝利判定ならA=1
        if A == 1:
            if board[(h + Vh * i)][w + Vw * i][0] == 0:
                cnt_animal += 1
            else:
                cnt_animal = 0
            if cnt_animal != (i + 1):
                #3連続の探索中に1つでも動物アリならFalseを返す
                return False
        #解放判定ならA=2
        if A == 2:
            print("hoge")
            num *= board[(h + Vh * i)][w + Vw * i][0]
            if num <= 0:
                #3連続の探索中に1つでも動物ナシならFalseを返す
                return False
    #勝利or解放可能でTrueを返す
    return True

def release_3(h, w, Vh, Vw):
    for i in range(3):
        board[(h + Vh * i)][w + Vw * i][0] = 0
    return board

def release_three(x, y):
    board[x][y][0] = 0
    return board

def can_release_animal(n):
    for i in range(6):
        for i in range(6):
            if board[i][j][0] == n:
                return True
    return False

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

    print(status)
    print(type(status))
    return z
    
# ---------------------関数fin---------------------------------

while status < 3:
    print("turn", turn)
    print("player" + str(status) + ": select option")
    if turn == 2:
        print("0:change first put")
    print("1:put stone, 2:release three animals, 3:release one kind of animals")
    opt = int(input())
    if (turn == 2 and opt == 0):
        print("入れ替えます")
        board = hoge(status)
        status = change(status)
    if opt == 1:
        print("put stone")
        put_x, put_y = input().split()
        X = int(put_x) + 1
        Y = int(put_y) + 1
        if can_put(X, Y) == True:
            board = put_stone(X, Y, status)
            status = judge(X, Y, status)
            status = change(status)

    elif opt == 2:
        print("choice release three point")
        release_x1, release_y1 = input().split()
        release_x2, release_y2 = input().split()
        release_x3, release_y3 = input().split()
        X1 = int(release_x1) + 1
        Y1 = int(release_y1) + 1
        X2 = int(release_x2) + 1
        Y2 = int(release_y2) + 1
        X3 = int(release_x3) + 1
        Y3 = int(release_y3) + 1
        board = release_three(X1, Y1)
        board = release_three(X2, Y2)
        board = release_three(X3, Y3)
        status = change(status)
        
    elif opt == 3:
        print("select release animal")
        select_animal = int(input())
        if can_release_animal == True:
            board = release_animal(select_animal)
            status = change(status)
        else:
            print("中に誰もいませんよ")
        
    elif opt == 4:
        print("debug mode 3toukaihou")
        release_h, release_w = input().split()
        vector = input()
        H = int(release_h) + 1
        W = int(release_w) + 1
        Vector = int(vector)
        mode = 2
        V = vec(Vector)
        if check_board(H, W, V[0], V[1], mode, status) == True:
            board = release_3(H, W, V[0], V[1])
            status = change(status)
        else:
            print("むりだよ")
    
    elif opt == 5:
        print("debug mode judge")
        put_h, put_w = input().split()
        H = int(put_h) + 1
        W = int(put_w) + 1
        if can_put(H, W) == True:
            board = put_stone(H, W, status)
            mode = 0
            for i in range(1,9):
                V = vec(i)
                if check_board(H, W, V[0], V[1], mode, status) == True:
                    mode = 1
                    if check_board(H, W, V[0], V[1], mode, status) == True:
                        status = 3
                        print("厳しい..あまりに厳しい戦いだったが...よく頑張ったな")
                        break
                    else:
                        status = 4
                        print("お前の負けだ")
                        break
            status = change(status)
            
    for i in range(2, 8):
        for j in range(2, 8):
            print(board[i][j], end='')
        print('')

print("game end")

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
A, B, d = map(int, input().rstrip().split())

chart = []
for _ in range(N):
    chart.append(list(map(int, input().rstrip().split())))

da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

count = 1
chart[A][B] = 2

def turn_left():
    global d
    d = (d - 1) % 4

def go(n):
    global A, B, d
    A += da[d] * n
    B += db[d] * n
    chart[A][B] = 2

def is_exist_block():
    if chart[A + da[d]][B + db[d]] == 0:
        return True
    else:
        return False

def dont_move():
    for i in range(4):
        turn_left()
        if is_exist_block():
            return False
    return True

def back_sea():
    if chart[A - da[d]][B - db[d]] == 1:
        return True
    else:
        return False


while True:
    for _ in range(4):
        turn_left()
        
        if is_exist_block():
            go(1)
            count += 1
            break
    
    if dont_move():
        if back_sea():
            break
        else:
            go(-1)

print(count)

'''
N = int(input())
plans = input().split()
x, y = 1, 1
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x, y = nx, ny
print(x, y)
'''

N = int(input())
plans = input().split()
x, y = 1, 1
nx, ny = 0, 0

for plan in plans:
    nx = x
    ny = y
    if plan == 'L':
            ny = y - 1
    elif plan == 'R':
        ny = y + 1
    elif plan == 'U':
        nx = x - 1
    else:
        nx = x + 1
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x = nx
    y = ny

print(x, y)

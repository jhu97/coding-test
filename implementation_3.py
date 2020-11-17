import sys
input = sys.stdin.readline

knight = input()
horizontal_axis = list(map(chr, range(ord('a'), ord('h') + 1)))
vertical_axis = [str(i) for i in range(1, 9)]
steps = [[-2, -1], [-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]

x = horizontal_axis.index(knight[0])
y = vertical_axis.index(knight[1])
count = 0

for step in steps:
    X = x + step[0]
    Y = y + step[1] 
    if X < 0 or Y < 0 or X > 7 or Y > 7:
        continue
    count += 1

print(count)

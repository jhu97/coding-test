import sys
input = sys.stdin.readline

knight = input()
horizontal_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical_axis = ['1', '2', '3', '4', '5', '6', '7', '8']
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

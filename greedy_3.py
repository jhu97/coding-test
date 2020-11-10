import sys
input = sys.stdin.readline

N, M = map(int, input().split())
minimum = 0

for i in range(N):
    data = list(map(int, input().split()))
    minimum = max(minimum, min(data))

print(minimum)

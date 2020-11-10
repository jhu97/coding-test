import sys
input = sys.stdin.readline

N, M = map(int, input().split())
minimum = []

for i in range(N):
    data = list(map(int, input().split()))
    minimum.append(min(data))

print(max(minimum))

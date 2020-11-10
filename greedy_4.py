import sys
input = sys.stdin.readline

N, K = map(int, input().split())
i = 0

while True:
    if N % K == 0:
        N = N // K
    else:
        N -= 1
    i += 1
    if N == 1:
        break

print(i)

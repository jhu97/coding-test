import sys
input = sys.stdin.readline

N, K = map(int, input().split())
count = 0

while True:
    target = (N // K) * K
    count += (N - target)
    N = target
    if N < K:
        break
    count += 1
    N //= K

count += (N - 1)
print(count)

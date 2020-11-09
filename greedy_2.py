import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
first = max(numbers)
second = numbers[-2]
total = 0

if numbers.count(first) > 1:
    total = first * M

else:
    total += K * first * (M // K)
    total += (M % K) * second

print(total)

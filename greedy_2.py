import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
first = numbers[-1]
second = numbers[-2]

total = 0

count = (M // (K + 1)) * K + M % (K + 1)

total += count * first
total += (M - count) * second

print(total)

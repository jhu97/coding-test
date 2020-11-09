import sys
input = sys.stdin.readline
N = int(input())
coin_500 = N // 500
coin_100= (N % 500) // 100
coin_50 = ((N % 500) % 100) // 50
coin_10 = (((N % 500) % 100) % 50) // 10
minimum = coin_500 + coin_100 + coin_50 + coin_10
print(minimum)

```
list = [500, 100, 50, 10]
coin = 0
for i in list:
    coin += N // i
    N %= i
print(coin)
```

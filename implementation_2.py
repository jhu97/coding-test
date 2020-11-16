import sys 
input = sys.stdin.readline

N = int(input())
count = 0

for hour in range(N + 1):
    if '3' in str(hour):
        count += 60 * 60
    else:
        for minute in range(60):
            if '3' in str(minute):
                count += 60
            else:
                for sec in range(60):
                    if '3' in str(sec):
                        count += 1
                        
print(count)

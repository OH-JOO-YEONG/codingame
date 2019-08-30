import sys
import math

n = int(input())
temp = input()
temps = temp.split()
if n == 0:
    print("0")
else:
    min_t = 5527
    for i in range(n):
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(temps[i])
        if abs(t) < abs(min_t):
            min_t = t
        if abs(t) == abs(min_t):
            if t > 0:
                min_t = t
    print(min_t)
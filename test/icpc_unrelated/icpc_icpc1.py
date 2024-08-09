import math

x = int(input())

if x <= 100:
    print("99")
elif x%100 < 49:
    print(x-(x%100+1))
elif x%100 >= 49:
    print(x + (100-(x%100))-1)

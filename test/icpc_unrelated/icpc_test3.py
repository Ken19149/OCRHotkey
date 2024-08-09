n = int(input())

num = 1.5
for i in range(n+1):
    num = num*2 - 1

num = int(num**2)

if n == 0:
    num = 4

print(num)
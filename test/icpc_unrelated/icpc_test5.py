import math

grid = int(input())
a = input().split(" ")
b = input().split(" ")

for i in range(len(a)):
    a[i] = int(a[i])
    b[i] = int(b[i])


x1 = 0
x2 = 0
x3 = 0

y1 = 0
y2 = 0
y3 = 0

for i in range(math.floor(grid/3)):
    x1 += a[i*3]
    x2 += a[i*3+1]
    x3 += a[i*3+2]

    y1 += b[i*3]
    y2 += b[i*3+1]
    y3 += b[i*3+2]

if grid % 3 == 1:
    x1 += a[-1]
    y1 += b[-1]
elif grid % 3 == 2:
    x1 += a[-2]
    x2 += a[-1]
    y1 += b[-2]
    y2 += b[-1]

c1 = x2*y1 + x1*y2 + x3*y3
c2 = x3*y1 + x2*y2 + x1*y3
c3 = x1*y1 + x2*y3 + x3*y2

print(c1, c2, c3)
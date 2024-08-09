count = int(input())

stack = list(map(int, input().split(" ")))
next = ""

for i in range(count):
    current = stack[0]
    stack.pop()
    new_current = stack[0]
    if current > new_current:
        stack.pop()
    elif current < new_current[0]:
        next += new_current + " "
    
import time

# cal sqrt(a)

a = float(input("val: "))

L = 0
U = a

x = (L+U)/2

ans = [L,U]

def near(x, a):
    if abs(a-x**2) <= (10**-10)*max(a,x**2):
        return True
    else:
        return False

print(near(x,a))

i = 0
result = ""

while i <= 10000:
    if x**2 > a:
        ans = [L,x]
        print("x**2 > a")
    elif x**2 < a:
        ans = [x, U]
        print("x**2 < a")
    x = (ans[0]+ans[1])/2
    print(x)
    result += str(x) + "\n"
    i += 1
    # time.sleep(2)

file = open("result.txt", "w")
file.write(result)
file.close()
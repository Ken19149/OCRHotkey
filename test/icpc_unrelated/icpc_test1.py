# Reads two integers and prints their sum
def storage(input, array=[]):
    array.append(input)
    return [array.count(input)-1, input-(array.count(input)-1)]

def main():
    cases = int(input())
    array = []
    for i in range(0, cases):
        x = storage(int(input()), array)
        print(x[0], x[1])
main()

start = int(input())
branches = []
while True:
    branch = input()
    if branch == "-1":
        break
    branches.append(list(map(int, branch.split(" "))))

path = ""

def check(branches=branches):
    for i in range(len(branches)):
        if start == branches[i][0]:
            return False

for x in range(100):
    # ah = list(map(int, path.split(" ")))[::-1]
    '''
    ah = path.split(" ")[::-1]
    if ah[0] == ah[0]:
        ah.pop()
        ah = ah[::-1]
        path = ah
        break
    '''
    for i in range(len(branches)):
        for j in range(len(branches[i])):
            if start == branches[i][j]:
                path += " " + str(start)
                start = int(branches[i][0])

path = (list(dict.fromkeys(path.split(" "))))
ans = ""
for i in path:
    ans += i + " "
print(ans[::-1].replace("\n", "", 1)[::-1])
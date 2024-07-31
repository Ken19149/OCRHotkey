socks = int(input())

pair = list(map(int, input().split(" ")))
count = len(pair)
first = pair[0:int(len(pair)/2)]
last = pair[int(len(pair)/2):-1]
last = last[::-1]
last.append(pair[-1])
last = last[::-1]

def remove_pair(array):
    for j in range(len(array)):
        for i in range(len(array)):
            try:
                if array[i] == array[i+1]:
                    array.pop(i)
                    array.pop(i)
                    break
            except:
                pass
    return array

process = remove_pair(pair)
if remove_pair == []:
    print(count)
try:
    first_remove = process[0:int(len(process)/2)]
    last_remove = process[int(len(process)/2):-1]
    last_remove = last_remove[::-1]
    last_remove.append(process[-1])
    last_remove = last_remove[::-1]
except:
    pass

if count % 2 ==1:
    print("impossible")
elif first == last:
    print(count)
elif first_remove == last_remove:
    print(count)
else:
    print("impossible")


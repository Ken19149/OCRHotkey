enter = int(input())
leave = int(input())

in_list = list(map(int, input().split(" ")))
out_list = list(map(int, input().split(" ")))

occurence = []

for i in out_list:
    for j in in_list:
        if i-j > 0:
            occurence.append(i-j)

print(max(sorted(occurence),key=occurence.count))

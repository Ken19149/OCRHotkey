number = input()

collection = [[],[],[],[],[],[],[],[],[],[]]
no = [[],[],[],[],[],[],[],[],[],[]]

zero = False

for i in number:
    collection[int(i)].append(int(i))
for i in range(len(collection)):
    no[i] = collection[i].count(i)

if int(no[0]) > 0:
    zero = True

collection.pop(0)
no.pop(0)

lowest_loc = no.index(min(no))
lowest_count = (len(collection[lowest_loc]))

ans = ""

for i in range(lowest_count):
    ans += str(lowest_loc+1)
if not zero:
    ans += "0"
else:
    ans += str(lowest_loc+1)
if lowest_count == 0:
    ans = str(lowest_loc+1)

print(ans)
questions = int(input())
ans = ""
for i in range(questions):
    digits = input().split(",")
    for x in range(len(digits)):
        if digits[x] == "":
            digits[x] = "0"
    digits = list(map(int, digits))[::-1]
    
    no = 0
    for j in range(0, len(digits)):
        no += digits[j]*(60**j)
    ans += str(no) + "\n"

print(ans[::-1].replace("\n", "", 1)[::-1])
# Reads two integers and prints their sum
table = [2,4,5,8,6,9,11,16,18]
def next_onoroy(val):
    if 1 <= val < 10:
        return table[val-1]
    elif val >=10:
        binary = str(bin(val)).replace("0b", "0")
        binary = binary[::-1].split("10", 1)
        binary[1] = "01" + binary[1]
        if binary[0][0] == "0" and binary[0][-1] == "1":
            s = list(binary[0])
            s[0] = "1"
            s[-1] = "0"
            binary[0] = "".join(s)
        binary = str(binary[0] + binary[1])[::-1]

        
        return int(binary, 2)
        

def main():
    cases = int(input())
    for i in range(0, cases):
        print("Case",str(i+1) + ": " + str(next_onoroy(int(input()))))

main()

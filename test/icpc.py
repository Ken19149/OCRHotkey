import sys
input = sys.stdin.read
output = sys.stdout.write

def main():
    data = input()
    result = data
    output(str(result) + "\n")

if __name__ == "__main__":
    main()
import math

count = int(input())

prices = []

for _ in range(count):
    prices.append(int(input()))
prices.sort()

prices = prices[::-1]

discount = []

for i in range(math.floor(len(prices)/3)):
    discount.append(prices[(i+1)*3-1])

print(sum(prices)-sum(discount))
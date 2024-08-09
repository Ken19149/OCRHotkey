import random
import matplotlib.pyplot as plt

x = []
y = []

for i in range(0,24):
    x.append(i+1)
    y.append(random.randint(0,12))

print(y)
plt.bar(x,y, width=1)
plt.show()
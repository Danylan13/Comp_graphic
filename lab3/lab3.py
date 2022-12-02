import matplotlib.pyplot as plt
import math
p1 = []
p2 = []
text = []
x = []
y = []
print(math.radians(40))

file = open("DS7.txt")
with file as f:
    for line in f:
            text.append([int(x) for x in line.split()])

for i in range(len(text)):
    for j in range(1):
        p1.append(text[i][0])
        p2.append(960 - text[i][1])
        p1[i] -= 480
        p2[i] -= 480
        x.append(int(p1[i]) * math.cos(math.radians(40)) - int(p2[i]) * math.sin(math.radians(40)))
        y.append(int(p1[i]) * math.sin(math.radians(40)) + int(p2[i]) * math.cos(math.radians(40)))
        x[i] += 480
        y[i] += 480
        #p1[i] += 480
        #p2[i] += 480
plt.figure('Афінне перетворення малюнка за датасетом(DS7.txt)')
plt.scatter(x, y)
plt.show()
plt.close()
file.close()
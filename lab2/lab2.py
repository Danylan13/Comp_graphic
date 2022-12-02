import matplotlib.pyplot as plt

m1 = []
m2 = []
text =[]

my_file = open("DS7.txt")
with my_file as f:
    for line in f:
            text.append([int(x) for x in line.split()])

for i in range(len(text)):
    for j in range(1):
        m1.append(text[i][0])
        m2.append(960 - text[i][1])

plt.scatter(m1, m2)
plt.show()
plt.close()
my_file.close()
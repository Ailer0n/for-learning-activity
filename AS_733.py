f = open("D:/as20000102.txt", "r", encoding='utf-8').readlines()
list1 = []
summ = []


V_R = f[2].split()[2::2]

for i in range(4, len(f)):
    line = list(map(int, f[i].split('\t')))
    list1.append(line[0])


buf = 0
m = 0

for i in list1:
    if buf != i:
        buf_line = [m, i-1]
        summ.append(buf_line)
        m = 0
    m += 1
    buf = i


summ = sorted(summ, key=lambda x: x[0])
summ = summ[len(summ)-10:]
for i in range(len(summ)- 1,0,-1):
    print(summ[i][1], " вершина - ", summ[i][0], "св.")




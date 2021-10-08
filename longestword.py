str1 = " What is the longest word in this sequence of strings"
l1 = str1.split()
a=0
max_len = 0

for i in range(len(l1)):
    if len(l1[i]) > max_len:
        a = i
        max_len = len(l1[i])

print(l1[a])  
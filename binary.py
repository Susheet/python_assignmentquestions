n = int(input("Enter no.="))
temp = n
a = []
var = 1
while var==1:
    a.append(temp%2)
    temp = temp//2
    if temp == 0:
        break

num = 0
power = len(a)-1
for i in a:
    if i==1:
        num = num + pow(2,power)
    power = power-1
print(num)

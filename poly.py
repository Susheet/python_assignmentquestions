


degree = int(input("Enter the degree of polynomial="))
print("Enter coefficient in the order for equation ax^n + bx^n-1 +....")
n = degree
l=[]
for i in range(0,n+1):
    a = int(input("Enter coefficient:"))
    l.append(a)

value = int(input("Enter value to compute:"))
sum = 0
j = n
for i in range(0,n):
    sum = sum + l[i]*(value**j)
    j = j-1

sum = sum + l[-1]
print("The sum is : ",sum)

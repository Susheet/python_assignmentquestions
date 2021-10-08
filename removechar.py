str1 = "Hello this is a sample string."

n = int(input("enter the nth index ="))

str1 = str1[0:n] + str1[n+1:]
print(str1)
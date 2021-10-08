t1 = open("test.txt","r")
t2 = open("test2.txt","r")

A = t1.read()
B = t2.read()
flag = 0

A = A.splitlines()
B = B.splitlines()

for i in range(len(A)):
    print(A[i])
    print(B[i])
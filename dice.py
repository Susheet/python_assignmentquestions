
list = []
score = 0
t = ()
for i in range(3):
    t1 = int(input("Enter 1st dice number "))
    t2 = int(input("Enter 2nd dice number "))
    t = t + (t1,t2,)
    sum = t1+t2
    if sum == 12:
        score = 0
    else:
        score = score+sum
list.append(t)

print(list)
print("score is " + str(score) )

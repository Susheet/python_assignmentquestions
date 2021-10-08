students = {'Kumar':[50,90,100],'Srivastava':[100,100,100],'Verma':[100,100,100]}
passed = []
for i in students:
    if students[i].count(100) == 3:
        passed.append(i)
passed.sort()
print(passed)
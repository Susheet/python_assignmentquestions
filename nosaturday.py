list = [] 
count = 0
st = int(input("Enter no. of saturdays:"))
for i in range(0,st):
    n = (int)(input("Enter the progress for today"))
    list.append(n)

if len(list)==1:
    print("No previous entry")
else:
    k=len(list)-1
    for i in range(k):
        if(list[i+1]>list[i]):
            count += 1
    
print(count)
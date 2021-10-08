s=input("Enter the instruction")
li=[]
for i in s:
  if i.isdigit():
    li.append(i)
li.reverse()
  
print(li)
s.split()
for i in s:
  if i=='+':
    k=li.pop(-1)
    l=li.pop(-1)
    j=int(k)+int(l)
    li.append(j)
  elif i=='-':
    k=li.pop(-1)
    l=li.pop(-1)
    j=int(k)-int(l)
    li.append(j)
  elif i=='*':
    k=li.pop(-1)
    l=li.pop(-1)
    j=int(k)*int(l)
    li.append(j)
  elif i=='/':
    k=li.pop(-1)
    l=li.pop(-1)
    j=int(k)//int(l)
    li.append(j)
  elif i=='DUP':
    n=len(li)
    m=li[n-1]
    li.append(m)
  elif i=='POP':
    li.pop()  
print(li)

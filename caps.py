str ='PM Narendra Modi was born on 17th September 1950'
s = ' '
for i in str:
    if(i.isupper()):
        s = s+i+' '
    else:
        s = s+i

print(s)
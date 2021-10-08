list=[]
list=(input('Enter list'))

dictionary=dict()

for i in list:
  if not dictionary.get(i):
    dictionary[i]=0
  dictionary[i]+=1;
for k in dictionary.keys():
  if(dictionary[k]==1):
    print(k)

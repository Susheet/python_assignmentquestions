number=int(input("Enter any number :"))
temp=number

reverse_num=0
while(number>0):
    digit=number%10
    reverse_num=reverse_num*10+digit
    number=number//10

if(temp==reverse_num):
    print("The number is palindrome!")
else: 
    print("Not a palindrome!")
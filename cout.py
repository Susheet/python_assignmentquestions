str1 = input("Enter a string -")

count_digit = 0
count_letters = 0

for i in str1:
    if i.isdigit():
        count_digit += 1
    if i.isalpha():
        count_letters += 1

print(count_digit)
print(count_letters)
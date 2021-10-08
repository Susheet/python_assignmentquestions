original_string = "This is the original string."
new_string = ""
for i in range(len(original_string)):
    if i%2 == 0:
        new_string = new_string + original_string[i]
    
print(new_string)
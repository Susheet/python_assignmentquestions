test_string = "RandomString"

for i in range(len(test_string)):
    for j in range(i+1, len(test_string)+1):
        print(test_string[i:j])
        print(f" The string begins with: {test_string[i:j][0]}")

def minion_game(string):
    stuart = 0 
    kevin = 0

    vowels = ['A','E','I','O','U']

    for i in range(len(string)):
        for j in range(i+1, len(test_string)+1):
            if test_string[i:j][0] in vowels:
                stuart += 1
            else:
                kevin +=1
    
    if stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print(f"Kevin {kevin}")

# Optimized solution

def minion_game(string):
    stuart = 0 
    kevin = 0

    vowels = ['A','E','I','O','U']

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    
    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")

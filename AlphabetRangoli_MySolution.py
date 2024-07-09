n = int(input("Enter number of rows: "))

def reverse_string_in_place(input_str):
    # Convert the string to a list of characters
    char_list = list(input_str)
    # Reverse the list in place
    char_list.reverse()
    # Convert the list back to a string
    reversed_str = ''.join(char_list)

    return reversed_str

fillcharPrev = ""
fillcharNext = chr(96+n)   
l = []

for i in range(2*n-1//2):
    print((fillcharNext+"-"+fillcharPrev).center(4*n-3, '-'))
    l.append((fillcharNext+"-"+fillcharPrev).center(4*n-3, '-'))
    fillcharPrev = reverse_string_in_place(fillcharNext)
    fillcharNext = "-".join([fillcharNext, chr(95+n-i)])

    if i == n-1:
        break

l.reverse()
l.pop(0)
for i in range(len(l)):
    print(l[i])




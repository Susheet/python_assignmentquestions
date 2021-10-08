import re
def specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

# print(specific_char("SusheetKumar")) 
# print(specific_char("*&%@#!}{"))



def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

# a=text_match('abcbabbcs')
# print(a)


# import re
# s = input("Enter a string: ")
# if re.search(r'^[a-z]+_[a-z]+',s):
#     print("Match found")
# else:
#     print("match not found")

# import re
# s = input("Enter a string: ")
# if re.search(r'\Bz\B',s):
#     print("Match found")
# else:
#     print("match not found")

import re
myURLs ="https://www.google.com, google domain , https://www.yahoo.in, yahoo domain"
pattern = ('http[s]?://[a-z0-9A-Z]+\.[a-z0-9A-Z]+\.(com|edu|net|in)')

print(bool(re.findall(pattern,myURLs)))

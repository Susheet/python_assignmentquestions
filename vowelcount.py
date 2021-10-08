def isVowel(character): 
  character = character.lower() 
  vowels = "aeiou" 

  if character in vowels: 
    return 1
  else:
      return 0

def countVowels(string): 
	count = 0
	for i in range(len(string)): 
		if isVowel(string[i]) : 
			count += 1
	return count 


string = "Susheet Kumar"
print(countVowels(string)) 
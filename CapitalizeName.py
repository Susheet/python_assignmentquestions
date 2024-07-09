def solve(s):
    words = s.split()
    
    capitalized_words = [word.capitalize() for word in words]
    
    result = ' '.join(capitalized_words)
    print(result)


solve("132 456 Wq  m e")

if response.status_code == 200:
    print("Successfully set default branch")
else:
    print("Failed to set default branch")


if github_user_admin != '':
      data = {
             "permission": "admin"
            }
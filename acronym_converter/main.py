text = input("Enter phrase to generate an acronym : ")

acronym = ""

acronym+=text[0]    
for i in range(len(text)):
    if text[i] == " ":
        acronym+=text[i+1]
    

print(f"Acronym of your phrase is {acronym.upper()}")

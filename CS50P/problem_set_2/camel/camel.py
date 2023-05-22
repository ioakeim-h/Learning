

name = str(input("camelCase: "))

for character in name:
    if character == character.upper():
        snake_case = "_" + character.lower()
        name = name.replace(character, snake_case)

print(name)
        
        

        
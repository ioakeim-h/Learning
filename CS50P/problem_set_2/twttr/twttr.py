
vowels = ["a","e","i","o","u","A","E","I","O","U"]

text = str(input("Input: "))

for letter in text:
    if letter in vowels:
        text = text.replace(letter, "")

print(text)





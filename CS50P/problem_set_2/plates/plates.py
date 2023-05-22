
import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    requirements = [
        plate[0:2].isalpha(), # Start with at least two letters
        2 <= len(plate) <= 6, # Characters should range between 2 and 6  
        not_zero(plate), # First number cannot be zero
        nums_at_end(plate), # Numbers must all be at the end
        clean(plate) # No periods, spaces, or punctuation marks
    ]
    #print(requirements) # See where it goes wrong
    return all(requirements)


def not_zero(plate):
    for char in plate:
        if char.isdigit():
            return char != "0"
    return True


def nums_at_end(plate):
    numbers = []
    for char in plate:
        if char.isdigit():
            numbers.append(char)

    # After each number there must be a number
    if len(numbers) > 0:
        return True if plate[-1 : -len(numbers)-1 : -1].isdigit() else False
    else:
        return True    
   

def clean(plate):
    punc_marks = string.punctuation
    for char in plate:
        if char in punc_marks:
            return False
    return True
        

main()





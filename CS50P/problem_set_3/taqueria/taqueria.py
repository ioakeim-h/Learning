


menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    selection = order()
    


def order():
    selection = []
    try:
        while True:
            item = input("Item: ").casefold().title()
            if item in menu:
                selection.append(item)
                print(f"Total: ${cost(selection):.2f}")
    except EOFError:
        return selection
        

def cost(selection):
    price = 0
    for item in selection:
        price += menu[item]
    return price


main()





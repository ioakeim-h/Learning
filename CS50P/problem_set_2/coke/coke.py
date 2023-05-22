

amount = 50
denominations = [25, 10, 5]


while True:
    
    # Ensure correct denominations
    while True:
            coin = int(input("Insert Coin: "))
            if coin in denominations:
                break
            else:
                print(f"Amount Due: {amount}")
                continue

    # Owed
    amount -= coin
    if amount > 0:
        print(f"Amount Due: {amount}")
    
    # Get change
    if amount <= 0:
        print(f"Change Owed: {-amount}")
        break

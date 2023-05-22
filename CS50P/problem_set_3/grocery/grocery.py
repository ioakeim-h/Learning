

basket = []
count = []


while True:
    try:
        i = input().upper()
        basket.append(i)
    except EOFError:
        basket.sort()
        print()
        break


for i in basket:
    n_times = basket.count(i)
    count.append(n_times)


grocery = dict(zip(basket, count))


x = len(grocery)
while x != 0:
    for i in grocery:
        print(grocery[i], i) 
        x -= 1

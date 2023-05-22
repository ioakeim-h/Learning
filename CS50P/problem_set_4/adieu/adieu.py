from inflect import engine


names = []

while True:
    try:
        n = input("Name: ").strip().title()
        names.append(n)
    except EOFError:
        break

engine = engine()
print("\nAdieu, adieu, to " + engine.join(names))



greet = input("Greeting: ").casefold().strip()

if "hello" == greet[0:5]:
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")





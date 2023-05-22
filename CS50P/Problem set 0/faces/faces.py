
def main():
    text = str(input("Provide text: "))
    print(convert(text))

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()
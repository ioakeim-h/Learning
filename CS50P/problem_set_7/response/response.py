import validators


def main():
    email = input("What's your email address? ").strip().casefold()
    print(validate(email))


def validate(e):
    if validators.email(e):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()















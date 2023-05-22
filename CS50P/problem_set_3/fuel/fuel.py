

def main():
    n, d = prompt()
    print(convert(n, d))


def prompt():
    while True:
        numer, denom = input("Fraction: ").split("/")
        if int(numer) <= int(denom):
            return numer, denom


def convert(n, d):
    fuel = int(n) / int(d) * 100

    if fuel <= 1:
        return "E"
    elif fuel >= 99:
        return "F"
    else:
        fuel = str(round(fuel)) + "%"
        return fuel 

  
while True:
    try:
        main()
        break
    except (ValueError, ZeroDivisionError):
        pass










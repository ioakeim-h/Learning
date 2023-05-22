
import sys
# Raise exception without traceback
sys.tracebacklimit = 0

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(f):
    while True:
        if f.count("/") != 1 or len(f) < 3:
            f = input("Fraction: ")
        else: 
            break
    
    numer, denom = f.split("/")
    if not (str.isdigit(numer) or str.isdigit(denom)):
        raise ValueError("Provide a fraction (e.g. '1/2')")
    elif int(denom) == 0:
        raise ZeroDivisionError("Denominator cannot be '0'")
    elif (int(numer) > int(denom)):
        raise ValueError("Numerator cannot be larger than the denominator")
    elif int(numer) <= int(denom):
        return round(int(numer) / int(denom) * 100)
        


def gauge(n):
    if n <= 1:
        return "E"
    elif n >= 99:
        return "F"
    else:
        n = str(n) + "%"
        return n 


if __name__ == "__main__":
    main()









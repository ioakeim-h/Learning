import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    
    if matches:
        i = 1 
        while i < 5:
            if 0 <= int(matches.group(i)) <= 255:
                i += 1
            else:
                break
        return True if i == 5 else False
    else:
        return False


if __name__ == "__main__":
    main()



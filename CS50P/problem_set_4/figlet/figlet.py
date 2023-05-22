
import sys
import random 
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts() # List of fonts


def main():
    if len(sys.argv) > 1:
        validate()
    figlet.setFont(font = get_font())
    text = input("Input: ").strip()
    print(figlet.renderText(text))


def validate():
    arguments = ["-f", "--font"] 
    if len(sys.argv) != 3 or sys.argv[1] not in arguments or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")


def get_font():
    if len(sys.argv) == 1:
        f = random.choice(fonts) 
    else:
        f = sys.argv[2]
    return f

    
main()

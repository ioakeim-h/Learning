
import sys



if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

else:
    n_lines = []
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                line = line.lstrip()
                if len(line) != 0:
                    if not (line.startswith("#") or line.isspace()):
                        if not ((("\"" in line.lstrip()[0]) or ("'" in line.lstrip()[0])) and (line.lstrip()[1] == " ")):
                            n_lines.append(line)
                     
    except FileNotFoundError:
        sys.exit("File does not exist")

print(len(n_lines))




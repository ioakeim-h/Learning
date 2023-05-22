import sys
import csv
import tabulate as tb

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")
else:
    menu = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append({"Sicilian Pizza":row[0], "Small":row[1], "Large":row[2]})
    except FileNotFoundError:
        sys.exit("File does not exist")
    

print(tb.tabulate(menu, headers="firstrow", tablefmt="grid"))





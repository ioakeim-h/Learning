import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif (sys.argv[1][-4:] or sys.argv[2][-4:]) != ".csv":
    sys.exit("Not a CSV file")
else:

    try:
        students = []
        
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name":row["name"], "house":row["house"]})
        
        for st in students:
                st["last"], st["first"] = st["name"].split(", ")
                st.pop("name")

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first","last","house"])
            writer.writeheader()
            for st in students:
                writer.writerow({"first":st["first"], "last":st["last"], "house":st["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read \"{sys.argv[1]}\"")











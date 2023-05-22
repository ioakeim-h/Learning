

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

months_numeric = []
for i in months:
    months_numeric.append(months.index(i) + 1)

calendar = dict(zip(months, months_numeric))



def main():
    date = input("Date: ").strip()
    month, day, year = date_info(date)
    check_info(month, day, year)
    print(f"{year}-{month:0>2}-{day:0>2}")


def date_info(d):
    # Format: "9/8/1636"
    try:
        month, day, year = d.split("/")
        try:
            int(month)
        except ValueError:
            main()
        return month, day, year
    except ValueError:
        # Format: "September 8, 1636"
        try:
            month, day, year = d.split(" ")
            if day[-1] != ",":
                main()
            day = day.replace(",", "")
            try:
                month = calendar[month]
            except KeyError:
                main()
            return month, day, year
        except ValueError:
            main()
            
            
def check_info(m, d, y):
    # Check month
    try:
        if not (1 <= int(m) <= 12):
            main()
    except (TypeError, ValueError):
        if m not in months:
            main()
    # Check day
    if not (1 <= int(d) <= 31 and len(y) == 4):
        main()
    # Check year
    if len(y) != 4:
        main()
    
        
main()


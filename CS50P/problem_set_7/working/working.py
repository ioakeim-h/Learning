import re
import sys
sys.tracebacklimit = 0


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d?\d)(:\d\d)? (AM|PM) to (\d?\d)(:\d\d)? (AM|PM)$", s)
    #matches = re.search(r"^(\d?\d):?(\d\d)? (AM|PM) to (\d?\d):?(\d\d)? (AM|PM)$", s)


    try:
        start_h, start_m, start_am_pm, end_h, end_m, end_am_pm = matches.groups()
    except AttributeError:
        raise ValueError("""Time should be in 12-hour notation - Examples:
- '9:00 AM to 5:00 PM' or '9 AM to 5 PM'
- '9:00 PM to 5:00 AM' or '9 PM to 5 AM'""") from None

    # Adjust hours
    start_h = int(start_h)
    end_h = int(end_h)

    if 0 < start_h < 13:
        if "AM" in start_am_pm:
            if start_h < 10:
                start_h = "0" + str(start_h)
            elif start_h == 12:
                start_h = "00"
            else:
                start_h = str(start_h)
        else:
            if start_h < 12:
                start_h = str(start_h + 12)
            else:
                start_h = str(start_h)
    else:
        raise ValueError("Hours can only vary between '1' and '12'")

    if 0 < end_h < 13:
        if "AM" in end_am_pm:
            if end_h < 10:
                end_h = "0" + str(end_h)
            elif end_h == 12:
                end_h = "00"
            else:
                end_h = str(end_h)
        else:
            if end_h < 12:
                end_h = str(end_h + 12)
            else:
                end_h = str(end_h)
    else:
        raise ValueError("Hours can only vary between '1' and '12'")

    # Adjust minutes
    if start_m:
        start_m = int(start_m[1:3])
        if 0 <= start_m < 60:
            if start_m < 10:
                start_m = "0" + str(start_m)
            else:
                start_m = str(start_m)
        else:
            raise ValueError("Minutes can only vary between '00' and '59'")
    else:
        start_m = "00"

    if end_m:
        end_m = int(end_m[1:3])
        if 0 <= end_m < 60:
            if end_m < 10:
                end_m = "0" + str(end_m)
            else:
                end_m = str(end_m)
        else:
            raise ValueError("Minutes can only vary between '00' and '59'")
    else:
        end_m = "00"

    return start_h + ":" + start_m + " to " + end_h + ":" + end_m

if __name__ == "__main__":
    main()










    
    






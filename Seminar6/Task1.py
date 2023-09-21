def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def is_valid_date(date):
    try:
        day, month, year = map(int, date.split('.'))
        
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False

        days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if day < 1 or day > days_in_month[month - 1]:
            return False

        return True
    except ValueError:
        return False

def main():
    import sys

    if len(sys.argv) != 2:
        sys.exit(1)

    date = sys.argv[1]
    if is_valid_date(date):
        print(f"{date} - корректная дата")
    else:
        print(f"{date} - некорректная дата")

if __name__ == "__main__":
    main()
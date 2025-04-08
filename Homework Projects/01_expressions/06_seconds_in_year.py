# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # We can get the number of seconds per year by multiplying the handy constants above!
    total_seconds_in_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    print("There are " + str(total_seconds_in_year) + " seconds in a year!")

# This provided line is required at the end of a Python file to call the main() function.
if __name__ == '__main__':
    main()
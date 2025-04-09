def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Keep doubling until the value is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# This line is required to call the main() function
if __name__ == '__main__':
    main()

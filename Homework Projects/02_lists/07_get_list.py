def main():
    lst = []  # Initialize an empty list

    val = input("Enter a value: ")  # Ask the user for input
    while val:  # Continue as long as the input is not empty
        lst.append(val)  # Add the input to the list
        val = input("Enter a value: ")  # Prompt again

    print("Here's the list:", lst)


# This provided line is required at the end of the file
if __name__ == '__main__':
    main()

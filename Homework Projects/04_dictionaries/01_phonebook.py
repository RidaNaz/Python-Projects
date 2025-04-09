def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook dictionary

    while True:
        name = input("Name: ")
        if name == "":
            break  # Exit loop if an empty string is entered for the name
        number = input("Number: ")
        phonebook[name] = number  # Add name and number to the phonebook

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")  # Print each name with its corresponding phone number


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break  # Exit lookup loop if an empty string is entered
        if name not in phonebook:
            print(f"{name} is not in the phonebook")
        else:
            print(phonebook[name])  # Print the phone number associated with the name


def main():
    phonebook = read_phone_numbers()  # Read phone numbers from the user
    print_phonebook(phonebook)  # Print the phonebook
    lookup_numbers(phonebook)  # Allow user to lookup numbers


# Python boilerplate.
if __name__ == '__main__':
    main()

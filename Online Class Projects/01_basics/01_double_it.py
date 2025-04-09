def main():
    # Asking the user for an initial number
    curr_value = int(input("Enter a number: "))  # Converting the input to an integer

    # Loop to double the value until it reaches or exceeds 100
    while curr_value < 100:
        # Doubling the current value
        curr_value = curr_value * 2
        # Printing the updated value
        print(curr_value, end=" ")

# Ensuring that the main function is executed when the script is run directly
if __name__ == "__main__":
    main()

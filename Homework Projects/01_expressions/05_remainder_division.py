def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
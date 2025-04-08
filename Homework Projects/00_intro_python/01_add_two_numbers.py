def main():
    """This program adds two numbers entered by the user."""
    print("This program adds two numbers.")
    
    # Get user inputs and convert them to integers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Calculate sum
    total = num1 + num2
    
    # Display result
    print(f"The total sum is: {total}")

# Required to call the main function
if __name__ == '__main__':
    main()

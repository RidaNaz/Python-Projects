def main():
    """Prompts the user for a number and prints its square."""

    print("🔢 Square Calculator 🔢")

    try:
        # Get number from user
        num = float(input("Type a number to see its square: "))

        # Compute the square
        square = num ** 2

        # Display result with 2 decimal places
        print(f"{num:.2f} squared is {square:.2f}")

    except ValueError:
        print("⚠️ Please enter a valid number.")

# Required line to execute the main function
if __name__ == '__main__':
    main()
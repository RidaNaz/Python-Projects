def main():
    """Calculates and prints the perimeter of a triangle based on user input."""

    print("🔺 Triangle Perimeter Calculator 🔺")

    try:
        # Input side lengths as floats
        side1 = float(input("What is the length of side 1? "))
        side2 = float(input("What is the length of side 2? "))
        side3 = float(input("What is the length of side 3? "))

        # Calculate perimeter
        perimeter = side1 + side2 + side3

        # Display result formatted to 2 decimal places
        print(f"The perimeter of the triangle is {perimeter:.2f}")

    except ValueError:
        print("⚠️ Please enter valid numbers for side lengths.")

# Required line to execute the main function
if __name__ == '__main__':
    main()
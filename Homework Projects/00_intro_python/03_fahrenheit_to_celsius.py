
def main():
    """Converts temperature from Fahrenheit to Celsius with user input."""
    print("🌡️ Fahrenheit to Celsius Converter 🌡️")
    
    try:
        # Get temperature from user and convert to float
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        
        # Apply conversion formula
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        
        # Print the result rounded to 2 decimal places
        print(f"Temperature: {fahrenheit}°F = {celsius:.2f}°C")

    except ValueError:
        print("⚠️ Please enter a valid number (e.g., 98.6).")

# Required to call the main function
if __name__ == '__main__':
    main()
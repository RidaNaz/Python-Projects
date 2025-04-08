# Constant: Speed of light in meters per second
C: int = 299_792_458  # Using underscores for readability (Python allows this)

def main():
    # Ask the user to enter the mass in kilograms
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using the famous formula: E = m * c^2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display breakdown of the calculation
    print("\ne = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(f"\n{energy_in_joules} joules of energy!")

# Call the main function to run the program
if __name__ == '__main__':
    main()

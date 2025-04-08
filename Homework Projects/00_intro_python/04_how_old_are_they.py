def main():
    """Solves the age riddle by calculating and printing each friend's age."""
    
    # Step-by-step age calculation based on the riddle
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    # Print results exactly as expected
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

# Required line to execute the main function
if __name__ == '__main__':
    main()
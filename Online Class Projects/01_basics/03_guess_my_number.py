import random

def main():
    # Generate the secret number at random
    secret_number: int = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get the user's first guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the user guesses the secret number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Print an empty line to tidy up the console for new guesses
        
        # Get a new guess from the user
        guess = int(input("Enter a new guess: "))
    
    print(f"Congrats! The number was: {secret_number}")

# Ensure the main function is executed when the script is run directly
if __name__ == '__main__':
    main()

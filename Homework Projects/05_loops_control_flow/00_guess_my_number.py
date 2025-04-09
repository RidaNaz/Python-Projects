import random

def main():
    # Generate the secret number at random between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Get user's guess
    guess = int(input("Enter a guess: "))

    # Keep prompting until the guess matches the secret number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Print an empty line to tidy up the console for new guesses
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
    
    print("Congrats! The number was: " + str(secret_number))

# Python boilerplate to call the main function
if __name__ == '__main__':
    main()

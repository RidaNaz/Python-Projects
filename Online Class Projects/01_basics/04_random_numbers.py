import random

# Constants defining the number of random numbers, and their range
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

# Ensure the main function is executed when the script is run directly
if __name__ == '__main__':
    main()

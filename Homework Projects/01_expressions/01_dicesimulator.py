import random

# Constant representing number of sides on a die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints the values and their sum.
    This demonstrates local variable scope inside a function.
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2

    print(f"Rolled: Die1 = {die1}, Die2 = {die2} --> Total = {total}")

def main():
    # This die1 is local to main() and has no connection with die1 inside roll_dice()
    die1: int = 10
    print(f"[main()] Initial die1 value: {die1}\n")

    print("Rolling dice three times...\n")
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"\n[main()] Final die1 value: {die1} (unchanged, because of variable scope)")

# Entry point of the program
if __name__ == '__main__':
    main()
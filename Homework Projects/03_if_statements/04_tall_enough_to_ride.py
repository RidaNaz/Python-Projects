MINIMUM_HEIGHT : int = 50  # arbitrary units :)

def tall_enough_extension():
    while True:
        height_input = input("How tall are you? ")  # Prompt for height input
        if height_input == "":  # If the user enters nothing, stop the loop
            break
        height = float(height_input)  # Convert height to float
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

def main():
    tall_enough_extension()

# Ensure the main function is called
if __name__ == '__main__':
    main()

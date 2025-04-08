def main():
    """An interactive bot that agrees with your favorite animal choice."""
    print("🐾 Welcome to Agreement Bot! Let's talk animals 🐾")
    
    # Ask user for their favorite animal
    animal = input("What's your favorite animal? ").strip().capitalize()

    # Handle empty input
    if not animal:
        print("Oops! You didn't type anything 🐌")
    else:
        print(f"My favorite animal is also {animal}! 🐾")

# Call the main function
if __name__ == '__main__':
    main()
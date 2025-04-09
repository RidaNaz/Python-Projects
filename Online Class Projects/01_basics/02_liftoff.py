def main():
    # Countdown from 10 to 1 and print each number
    for i in range(10, 0, -1):
        print(i, end=" ")  # Print the countdown number, followed by a space
    
    # After the countdown, print 'Liftoff!'
    print("Liftoff!")

# Ensuring that the main function is executed when the script is run directly
if __name__ == "__main__":
    main()

def subtract_seven(num):
    # Subtract 7 from the given number
    num = num - 7
    return num

def main():
    # Initial number to subtract 7 from
    num = 7

    # Calling the subtract_seven function and updating the num variable
    num = subtract_seven(num)

    # Printing the result
    print("this should be zero:", num)

# Ensure the main function runs when the script is executed
if __name__ == '__main__':
    main()

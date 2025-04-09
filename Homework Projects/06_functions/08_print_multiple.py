def print_multiple(message: str, repeats: int):
    for _ in range(repeats):
        print(message)

# There is no need to edit code beyond this point
def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()

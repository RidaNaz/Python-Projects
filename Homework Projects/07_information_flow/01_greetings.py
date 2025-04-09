def greet(name):
    return "Greetings " + name + "!"

def main():
    name = input("What's your name? ")  # Get the user's name
    print(greet(name))  # Call greet function and print the result

if __name__ == '__main__':
    main()

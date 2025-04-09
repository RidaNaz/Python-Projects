def get_user_info():
    # Asking for user information and storing the input in variables
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")

    # Returning the user data as a tuple
    return first_name, last_name, email_address

# Main function to execute the program
def main():
    # Calling the get_user_info function and storing the returned data
    user_data = get_user_info()

    # Printing the received user data
    print("Received the following user data:", user_data)

# Running the main function
if __name__ == "__main__":
    main()

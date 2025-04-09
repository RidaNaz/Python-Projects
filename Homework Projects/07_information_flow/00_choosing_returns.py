ADULT_AGE = 18  # U.S. age to be considered an adult

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

########## No need to edit code beyond this point :) ##########

def main():
    age = int(input("How old is this person?: "))  # Prompt for the person's age
    print(is_adult(age))  # Print the result of is_adult

if __name__ == "__main__":
    main()

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ")

    # Get the number of fruit in stock
    stock = num_in_stock(fruit)

    # Check if the fruit is in stock and print the result
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit.lower() == 'apple':
        return 2
    if fruit.lower() == 'durian':
        return 4
    if fruit.lower() == 'pear':
        return 1000
    else:
        # this fruit is not in stock.
        return 0

# Run the main function
if __name__ == '__main__':
    main()

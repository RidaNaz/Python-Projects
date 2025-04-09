def main():
    # Dictionary storing fruit names as keys and their prices as values
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0  # Initialize the total cost to 0
    # Loop through each fruit in the dictionary
    for fruit_name in fruits:
        price = fruits[fruit_name]  # Get the price of the current fruit
        # Prompt the user for the quantity of the current fruit they want to buy
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
        # Add the cost of the current fruit to the total cost
        total_cost += (price * amount_bought)
    
    # Print the total cost
    print(f"Your total is ${total_cost}")

# Python boilerplate to call the main function
if __name__ == '__main__':
    main()

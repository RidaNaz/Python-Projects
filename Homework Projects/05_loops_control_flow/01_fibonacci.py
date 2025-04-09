MAX_TERM_VALUE = 10000  # Maximum value for the Fibonacci term

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number

    # Continue until the current term exceeds MAX_TERM_VALUE
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print the current term in the Fibonacci sequence
        term_after_next = curr_term + next_term  # Calculate the next Fibonacci term
        curr_term = next_term  # Move to the next term in the sequence
        next_term = term_after_next  # Update the next term

# Python boilerplate to call the main function
if __name__ == '__main__':
    main()

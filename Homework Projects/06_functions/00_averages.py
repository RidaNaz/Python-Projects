def average(a: float, b: float) -> float:
    """
    Returns the average (mean) of two numbers a and b.
    """
    return (a + b) / 2

def main():
    # Example calls to the average function
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    # Calculating the final average of the two previous averages
    final = average(avg_1, avg_2)

    # Display results
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

# Required call to run main()
if __name__ == '__main__':
    main()

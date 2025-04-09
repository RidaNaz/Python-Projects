def main():
    numbers: list[int] = [1, 2, 3, 4]  # Create a list of numbers

    for i in range(len(numbers)):  # Loop through each index of the list
        numbers[i] = numbers[i] * 2  # Double the value at each index

    print(numbers)  # Print the updated list


# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
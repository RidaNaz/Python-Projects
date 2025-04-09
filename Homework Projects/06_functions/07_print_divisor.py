def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")  # Print all on the same line with space

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()

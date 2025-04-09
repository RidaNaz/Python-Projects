def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    return value % 2 == 1

def main():
    for i in range(10, 20):
        if is_odd(i):
            print(f"{i} odd", end=" ")
        else:
            print(f"{i} even", end=" ")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

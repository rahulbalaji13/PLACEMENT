def count_valid_splits(gold):
    """
    Count the number of valid index positions that can split the gold array
    into northern and southern provinces.

    Args:
    gold (list of int): The array representing the amount of gold in each city.

    Returns:
    int: The number of valid split points.
    """
    total_gold = sum(gold)  # Total gold in the kingdom
    northern_sum = 0  # Sum of the northern province
    valid_splits = 0

    # Iterate through the array except for the last element
    for i in range(len(gold) - 1):
        northern_sum += gold[i]  # Update northern sum
        southern_sum = total_gold - northern_sum  # Calculate southern sum

        # Check for the validity of the split
        if northern_sum >= southern_sum:
            valid_splits += 1

    return valid_splits

def main():
    """
    Main function to take user input and count valid splits.
    """
    try:
        user_input = input("Enter the gold amounts separated by spaces: ")
        gold = list(map(int, user_input.split()))

        # Check if the input is valid (at least 2 cities)
        if len(gold) < 2:
            raise ValueError("The input should contain at least two cities.")

        result = count_valid_splits(gold)
        print(f"The number of valid splits is: {result}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print("Input string was not in a correct format")

if __name__ == "__main__":
    main()

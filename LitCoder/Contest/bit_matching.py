def count_matching_bits(x, y):
    """
    Count the number of matching bits in the binary representation of x and y.
    
    Args:
    x (int): First integer.
    y (int): Second integer.

    Returns:
    int: Number of matching bits.
    """
    # Count matching bits using bitwise XOR and bit length
    return 3 - bin(x ^ y).count('1')  # Since numbers are between 0 and 7 (3 bits)

def sum_matching_bits(arr):
    """
    Calculate the sum of matching bits for all ordered pairs (i, j).

    Args:
    arr (list of int): List of integers.

    Returns:
    int: Sum of matching bits for all ordered pairs.
    """
    total_sum = 0
    n = len(arr)
    
    # Iterate over all ordered pairs
    for i in range(n):
        for j in range(n):
            total_sum += count_matching_bits(arr[i], arr[j])
    
    return total_sum

def main():
    """
    Main function to accept user input and output the sum of matching bits.
    """
    input_data = input("Enter integers separated by spaces (0-7): ")
    # Convert input to a list of integers
    arr = list(map(int, input_data.split()))
    
    # Validate input
    if any(num < 0 or num > 7 for num in arr):
        print("Invalid Input")
        return
    
    # Calculate the result
    result = sum_matching_bits(arr)
    print(result)

if __name__ == "__main__":
    main()

def has_duplicates_within_distance(arr, k):
    """
    Check if there are duplicate elements within a specific distance k.

    Args:
    arr (list): List of integers (the array).
    k (int): Maximum allowed distance between duplicate elements.

    Returns:
    str: "Yes" if duplicates are found within distance k, otherwise "No".
    """
    index_map = {}  # Dictionary to store the last index of each element
    
    for index, value in enumerate(arr):
        if value in index_map:
            # Check the distance between current index and last index of the same value
            if index - index_map[value] <= k:
                return "Yes"
        # Update the last index of the current value
        index_map[value] = index
    
    return "No"

# Main module to take user input
if __name__ == "__main__":
    # Accept array input
    arr_input = input("Enter the array of integers (space-separated): ")
    arr = list(map(int, arr_input.split()))
    
    # Accept distance k input
    k = int(input("Enter the maximum distance k: "))
    
    # Check for duplicates and print the result
    result = has_duplicates_within_distance(arr, k)
    print(result)

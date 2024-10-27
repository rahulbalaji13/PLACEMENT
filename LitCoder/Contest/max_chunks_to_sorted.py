def max_chunks_to_make_sorted(arr):
    """
    Divide the array into chunks and print each chunk after sorting.

    Args:
    arr (list[int]): The input array representing a permutation of integers.
    """
    chunks = []
    current_max = 0
    start = 0
    
    for i in range(len(arr)):
        current_max = max(current_max, arr[i])
        
        # If the current index matches the current max, we can create a chunk
        if current_max == i:
            chunks.append(arr[start:i + 1])
            start = i + 1
            
    # Print each chunk
    for chunk in chunks:
        print(' '.join(map(str, chunk)))

if __name__ == "__main__":
    # Accepting input from the user
    user_input = input("Enter the permutation of integers (space-separated): ")
    arr = list(map(int, user_input.split()))
    max_chunks_to_make_sorted(arr)

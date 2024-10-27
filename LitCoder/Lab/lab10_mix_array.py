def array_manipulation(n, queries):
    # Initialize array of zeros with size n+1 for easier manipulation of indices
    arr = [0] * (n + 1)

    # Apply the range updates based on the queries
    for q in queries:
        start, end, value = q
        arr[start - 1] += value  # Add value at the start index
        if end <= n:
            arr[end] -= value  # Subtract value after the end index

    # Find the maximum value after processing all operations
    max_value = 0
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        max_value = max(max_value, current_sum)

    return max_value

# Driver code
if __name__ == "__main__":
    # Taking input from the user
    n = int(input("Enter array size: "))  # array size
    q_count = int(input("Enter the number of queries: "))  # number of queries
    queries = []

    print("Enter the queries in the format 'start end value':")
    for _ in range(q_count):
        queries.append(list(map(int, input().split())))

    # Get the maximum value after all operations
    result = array_manipulation(n, queries)
    print(result)
                                                                                                                            

def zigzag_sequence(arr):
    # Sort the array to find the smallest lexicographic order
    arr.sort()
    
    n = len(arr)
    k = (n + 1) // 2  # Calculate k

    # Create the zigzag pattern
    result = arr[:k] + arr[k:][::-1]  # First half increasing, second half decreasing

    # Swap to form the zigzag
    for i in range(1, k):
        result[i], result[n - i] = result[n - i], result[i]
    
    return result

def main():
    # Take input from the user
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements separated by space: ").strip().split()))

    # Generate the zigzag sequence
    result = zigzag_sequence(arr)

    # Print the result
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()

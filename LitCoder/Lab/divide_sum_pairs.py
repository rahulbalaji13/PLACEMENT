def divisible_sum_pairs():
    # Input: first line is the divisor, second line is the array
    divisor = int(input("Enter the divisor: "))
    ar = list(map(int, input("Enter the array elements: ").split()))

    # Initialize counter for pairs
    count = 0

    # Check all pairs
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            # Check if the sum of ar[i] and ar[j] is divisible by the divisor
            if (ar[i] + ar[j]) % divisor == 0:
                count += 1

    # Output the count of divisible sum pairs
    print(count)

# Example usage:
divisible_sum_pairs()
                                                                                                                            

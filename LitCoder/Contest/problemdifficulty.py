def max_total_difficulty():
    # Input: Difficulty levels, time limits, and queries
    try:
        # Read and process input data
        difficulties = list(map(int, input("Enter difficulty levels (space-separated): ").strip().split()))
        time_limits = list(map(int, input("Enter time limits (space-separated): ").strip().split()))
        queries = list(map(int, input("Enter queries (space-separated): ").strip().split()))

        N = len(difficulties)
        Q = len(queries)

        # Validate constraints
        if not (1 <= N <= 10 and 1 <= Q <= 10):
            print("Invalid")
            return

        if len(time_limits) != N:
            print("Invalid")
            return

        for d, l in zip(difficulties, time_limits):
            if not (1 <= d <= 50 and 1 <= l <= 50):
                print("Invalid")
                return

        results = []

        for K in queries:
            if not (1 <= K <= N):
                print("Invalid")
                return

            # Pair difficulties with their corresponding time limits
            paired = list(zip(time_limits, difficulties))

            # Sort by time limits in descending order
            paired.sort(reverse=True, key=lambda x: x[0])

            # Select the top K problems based on time limits
            top_k = paired[:K]

            # Sum the corresponding difficulty values
            total_difficulty = sum(difficulty for _, difficulty in top_k)

            # Store the result for the query
            results.append(total_difficulty)

        # Output the results for each query
        for result in results:
            print(result)

    except ValueError:
        print("Invalid")

# Run the function
max_total_difficulty()

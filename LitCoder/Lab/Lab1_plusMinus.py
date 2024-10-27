def count_ratios(arr):
    total_elements = len(arr)
    if total_elements == 0:
        return
    
    # Initialize counts
    positives = 0
    negatives = 0
    zeros = 0
    
    # Count positive, negative, and zero elements
    for num in arr:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += 1
        else:
            zeros += 1
    
    # Calculate ratios and print with three decimal places
    print(f"{positives / total_elements:.3f}")
    print(f"{negatives / total_elements:.3f}")
    print(f"{zeros / total_elements:.3f}")

# Input handling and function call
n = input()  # Number of elements
arr = list(map(int, input().split()))  # Input array of integers
count_ratios(arr)
                                                                                                                            

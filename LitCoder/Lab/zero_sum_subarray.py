def check_zero_sum_subarray(arr):
    # Check if all elements are integers
    if not all(isinstance(i, int) for i in arr):
        print("Array elements must be integers")
        return
    
    # Check the size of the array
    n = len(arr)
    if n < 1 or n > 10:
        print("Array size must be between 1 and 10")
        return
    
    # Check if all elements are within the range -10 to 10
    if not all(-10 <= i <= 10 for i in arr):
        print("Array elements must be from -10 to 10")
        return
    
    # Initialize an empty set to track cumulative sums
    cum_sum_set = set()
    cum_sum = 0

    for num in arr:
        cum_sum += num
        # If cumulative sum is zero or we've seen this sum before, a zero-sum subarray exists
        if cum_sum == 0 or cum_sum in cum_sum_set:
            print("True")
            print(n)  # Total number of elements in the array
            return
        cum_sum_set.add(cum_sum)

    # If no subarray with zero-sum is found
    print("False")
    print(n)  # Total number of elements in the array

# Input processing (single line of space-separated integers)
try:
    arr = list(map(int, input().split()))
    check_zero_sum_subarray(arr)
except ValueError:
    print("Array elements must be integers")
                                                                                                                            

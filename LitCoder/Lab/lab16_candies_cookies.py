import heapq

def combine_candies(target, candies):
    # Initialize a min-heap from the candies list
    heapq.heapify(candies)
    
    steps = 0
    
    # Continue combining candies until the least sweet candy meets or exceeds the target
    while len(candies) > 1 and candies[0] < target:
        # Extract the two least sweet candies
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)
        
        # Combine them to create a new candy
        new_sweetness = least_sweet + 2 * second_least_sweet
        
        # Add the new candy back into the heap
        heapq.heappush(candies, new_sweetness)
        
        # Increment the step counter
        steps += 1
    
    # Check if we've met or exceeded the target sweetness
    if candies[0] >= target:
        return steps
    else:
        return -1  # If it's not possible to reach the target

# Input and Output
if __name__ == "__main__":
    target = int(input("Enter the target sweetness: "))  # First line: target sweetness
    candies = list(map(int, input("Enter the sweetness levels of the candies: ").split()))  # Second line: list of candies sweetness
    
    result = combine_candies(target, candies)
    print(f"Steps to reach the target sweetness: {result}")
                                                                                                                            

# Function to compare scores of Charlie and Dave
def compare_triplets(c, d):
    # Initialize points for Charlie and Dave
    charlie_points = 0
    dave_points = 0
    
    # Iterate over the scores and compare them
    for i in range(len(c)):
        if c[i] > d[i]:
            charlie_points += 1
        elif c[i] < d[i]:
            dave_points += 1
        # No points are awarded if scores are equal
    
    # Return the comparison points as a tuple
    return charlie_points, dave_points

# Taking input from the user
def get_scores():
    # Input Charlie's and Dave's scores
    c = list(map(int, input("Enter Charlie's scores (space-separated): ").split()))
    d = list(map(int, input("Enter Dave's scores (space-separated): ").split()))
    
    # Check if both inputs have equal lengths
    if len(c) != len(d):
        print("Charlie and Dave must have the same number of scores.")
        return
    
    # Call the comparison function
    result = compare_triplets(c, d)
    
    # Print the result in the required format
    print(result[0], result[1])

# Run the function
get_scores()
                                                                                                                            

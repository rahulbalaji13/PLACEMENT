MOD = 1000000007

def legoWall(n, m):
    # Step 1: Calculate the number of ways to build a single row of width m
    def row_combinations(m):
        # ways[i] will store the number of ways to fill a row of width i
        ways = [0] * (m + 1)
        ways[0] = 1  # One way to build a row of width 0 (do nothing)
        
        for i in range(1, m + 1):
            ways[i] += ways[i - 1]  # Add a 1x1 block
            if i >= 2:
                ways[i] += ways[i - 2]  # Add a 1x2 block
            if i >= 3:
                ways[i] += ways[i - 3]  # Add a 1x3 block
            if i >= 4:
                ways[i] += ways[i - 4]  # Add a 1x4 block
            
            ways[i] %= MOD  # Apply modulo operation
        
        return ways
    
    # Step 2: Calculate total ways to build a full wall of height n and width m
    # Calculate number of ways to build a single row of width m
    ways_per_row = row_combinations(m)
    
    # For a wall of height n, total_ways_per_wall = (ways_per_row[m]) ** n (since each row can be independent)
    total_ways_per_wall = [1] * (m + 1)
    for i in range(1, m + 1):
        total_ways_per_wall[i] = pow(ways_per_row[i], n, MOD)  # Raise to the power of n, mod MOD
    
    # Step 3: Remove the invalid walls that have straight vertical breaks (solid wall condition)
    # invalid_walls[i] will store the number of invalid ways to build a wall of width i
    invalid_walls = [0] * (m + 1)
    
    for i in range(1, m + 1):
        invalid_walls[i] = total_ways_per_wall[i]
        for j in range(1, i):
            invalid_walls[i] -= (invalid_walls[j] * total_ways_per_wall[i - j]) % MOD
            invalid_walls[i] %= MOD
    
    # The result for the full wall is the number of valid ways to build a wall of width m
    return invalid_walls[m]

# Reading input from the user
n = int(input("Enter the height of the wall (n): "))
m = int(input("Enter the width of the wall (m): "))

# Output the result
result = legoWall(n, m)
print(f"The number of ways to build the wall is: {result}")
                                                                                                                            

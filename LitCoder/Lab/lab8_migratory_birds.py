from collections import Counter

def most_common_plant(sightings):
    # Count the occurrences of each plant ID
    plant_count = Counter(sightings)
    
    # Find the most common plant with the smallest ID in case of a tie
    most_common = min(plant_count, key=lambda x: (-plant_count[x], x))
    
    # Print the result
    print(most_common)

# Taking input from the user
if __name__ == "__main__":
    # Example input: "3 1 3 7 2 1 2"
    user_input = input("Enter plant sightings (space-separated integers): ")
    
    # Converting the input string to a list of integers
    sightings = list(map(int, user_input.split()))
    
    # Call the function to find and print the most common plant
    most_common_plant(sightings)
                                                                                                                            

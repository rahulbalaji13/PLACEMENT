def maxActivities(start_times, end_times):
    # Pair the start and end times into a list of tuples
    activities = list(zip(start_times, end_times))
    
    # Sort the activities based on their finish time (second value of tuple)
    activities.sort(key=lambda x: x[1])

    # List to store selected activities
    selected_activities = []

    # Initialize the last finish time to 0
    last_finish_time = 0

    # Iterate through the sorted activities and select non-overlapping ones
    for activity in activities:
        start, finish = activity
        if start >= last_finish_time:  # If the activity starts after the last finish time
            selected_activities.append(activity)  # Select the activity
            last_finish_time = finish  # Update the last finish time

    # Return the selected activities
    return selected_activities

# Function to accept input from the user
def input_activities():
    n = int(input("Enter the number of activities: "))  # Number of activities
    start_times = list(map(int, input("Enter the start times: ").split()))  # List of start times
    end_times = list(map(int, input("Enter the end times: ").split()))  # List of end times
    
    # Get the selected activities
    selected_activities = maxActivities(start_times, end_times)

    # Output the selected activities in the desired format
    for activity in selected_activities:
        print(activity[0], activity[1])

# Call the function to execute the program
input_activities()

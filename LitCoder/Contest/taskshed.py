def is_feasible(tasks, workers, max_time):
    """Check if it's feasible to complete tasks within max_time using the given number of workers."""
    current_sum = 0
    required_workers = 1

    for task in tasks:
        if task > max_time:
            return False  # Single task exceeds max_time, not feasible.

        if current_sum + task <= max_time:
            current_sum += task
        else:
            required_workers += 1
            current_sum = task
            if required_workers > workers:
                return False

    return True

def min_time_to_complete_tasks(tasks, workers):
    """Find the minimum time required to complete all tasks using binary search."""
    low, high = max(tasks), sum(tasks)
    best_time = high

    while low <= high:
        mid = (low + high) // 2

        if is_feasible(tasks, workers, mid):
            best_time = mid
            high = mid - 1
        else:
            low = mid + 1

    return best_time

def main():
    # Input handling
    n = int(input("Enter the number of tasks: "))
    tasks = list(map(int, input(f"Enter the durations of {n} tasks (space-separated): ").split()))
    workers = int(input("Enter the number of workers: "))

    # Validate input
    if len(tasks) != n or workers <= 0:
        print("Invalid input. Ensure task count matches and workers are positive.")
        return

    # Compute and display the minimum time
    result = min_time_to_complete_tasks(tasks, workers)
    print(f"Minimum time required to complete all tasks: {result}")

if __name__ == "__main__":
    main()

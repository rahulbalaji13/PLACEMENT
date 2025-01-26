def find_highest_mountain_peaks(heights):
    """
    Finds the total number of peaks on the highest mountains and their peak heights.

    Args:
        heights (list): List of integers representing mountain heights.

    Returns:
        int: Total number of peaks on the highest mountains.
        list: Heights of the peaks.
    """
    # Edge case: List should have at least 3 elements
    if len(heights) < 3:
        return 0, []

    # Find peaks
    peaks = []
    for i in range(1, len(heights) - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            peaks.append(heights[i])

    # If no peaks are found
    if not peaks:
        return 0, []

    # Determine the highest peak value
    highest_peak = max(peaks)

    # Filter only the highest peaks
    highest_peaks = [peak for peak in peaks if peak == highest_peak]

    return len(highest_peaks), highest_peaks

def main():
    try:
        # Read user input
        user_input = input("Enter mountain heights separated by spaces: ").strip()

        # Convert input into a list of integers
        heights = list(map(int, user_input.split()))

        # Validate constraints
        if any(h < 1 or h > 10**5 for h in heights):
            print("Input was not in a correct format")
            return

        # Find peaks and display results
        count, peak_heights = find_highest_mountain_peaks(heights)
        print(count)
        if count > 0:
            print(" ".join(map(str, peak_heights)))
    except ValueError:
        # Handle invalid input
        print("Input was not in a correct format")

if __name__ == "__main__":
    main()
